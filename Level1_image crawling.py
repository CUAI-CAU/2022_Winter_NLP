#!/usr/bin/env python
# coding: utf-8

# In[15]:


pip install selenium


# In[18]:


pip install webdriver-manager


# In[19]:


import numpy as np
import pandas as pd
import os
import sys
import urllib.request
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# In[29]:


# 크롤링한 낱말 dataset 불러오기
voca_list = pd.read_csv('C:/Users/Administrator/Desktop/voca.txt', sep =",", header=None, encoding = "utf-8")
voca_list = voca_list.transpose()
voca_list.columns = ['word']


# In[28]:


for voca in voca_list['word']:
    keyword = voca   
    maxImages = 1 

# crawled_img폴더 안에 하위 폴더 생성
# 폴더명에는 입력한 키워드, 이미지 수 정보를 표시
    path = 'crawled_img/'+keyword+'_'+str(maxImages)

    try:
        # 중복되는 폴더 명이 없다면 생성
        if not os.path.exists(path):
            os.makedirs(path)
        # 중복된다면 문구 출력 후 프로그램 종료
        else:
            print('이전에 같은 [검색어, 이미지 수]로 다운로드한 폴더가 존재합니다.')
            sys.exit(0)
    except OSError:
        print ('os error')
        sys.exit(0)
    
    pages = int((maxImages-1)/100)+1 #한 페이지당 표시되는 이미지 수(100)을 참고하여 확인할 페이지 수 계산
    imgCount = 0 # 추출 시도 이미지 수
    success = 0 # 추출 성공 이미지 수
    finish = False # 이미지에 모두 접근했는지 여부

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('lang=ko_KR')
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    

    for i in range(1,int(pages)+1):
        driver.get('https://pixabay.com/images/search/'+keyword+'/?pagi='+str(i))
        sleep(1)

        html = driver.page_source
        soup = BeautifulSoup(html,'html.parser')

        imgs = soup.select('div.row-masonry.search-results img')

        lastPage=False
        if len(imgs)!=100:
            lastPage=True

        for img in imgs:
            srcset = ""
            if img.get('srcset')==None:
                srcset = img.get('data-lazy-srcset')
            else: 
                srcset = img.get('srcset')


            src = ""
            if len(srcset):
                src = str(srcset).split()[0] 
                print(src)
                filename = src.split('/')[-1] 
                print(filename)
                saveUrl = path+'/'+filename 
                print(saveUrl)

                #파일 저장
                req = urllib.request.Request(src, headers={'User-Agent': 'Mozilla/5.0'})
                try:
                    imgUrl = urllib.request.urlopen(req).read() 
                    with open(saveUrl,"wb") as f: 
                        f.write(imgUrl) 
                    success+=1
                except urllib.error.HTTPError:
                    print('에러')
                    sys.exit(0)

            imgCount+=1

            if imgCount==maxImages:
                finish = True #입력한 이미지 수 만큼 모두 접근했음을 알림
                break
    
        #finish가 참이거나 더 이상 접근할 이미지가 없을 경우 크롤링 종료
        if finish or lastPage:
            break

    print('성공 : '+str(success)+', 실패 : '+str(maxImages-success))

