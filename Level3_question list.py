#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import json
import pandas as pd


# In[2]:


target_path_r = "C:/Users/Administrator/Downloads/data/"


# In[3]:


# AI-hub 주제별 일상 대화 데이터셋 구성 확인
target_path_list_r = os.listdir(target_path_r)
target_path_list_r


# In[4]:


target_path = "C:/Users/Administrator/Desktop/data/"


# In[5]:


# 데이터 개수가 충분해서 KAKAO(1)만 사용
target_path_list = os.listdir(target_path)
target_path_list


# In[6]:


# 첫 번째 입력 문장을 출력하는지 확인
ex = open(f"C:/Users/Administrator/Desktop/data/TL_01. KAKAO(1)/KAKAO_1000_01.json", encoding="UTF-8")
ex = json.loads(ex.read())


# In[7]:


ex['info'][0]['annotations']['lines'][0]['norm_text']


# In[8]:


files = os.listdir(target_path+target_path_list[0])


# In[9]:


# 모든 파일에서 첫 번째 문장 출력하여 리스트에 저장
daily_conversations = []
for i in range(len(target_path_list)):
    files = os.listdir(target_path+target_path_list[i])
    for k in range(len(files)):
        final_path = str(target_path)+str(target_path_list[i])+"/"+str(files[k])
        try:
            target_file = open(f"{final_path}", encoding="UTF-8")
            target_file = json.loads(target_file.read())
            daily_conversations.append(target_file['info'][0]['annotations']['lines'][0]['norm_text'])
        except:
            print(f"error! {final_path}")


# In[10]:


df = pd.DataFrame({'text':daily_conversations})


# In[11]:


df.head()


# In[12]:


# 질문 문장만 추출하기 위해 "?"이 포함되어 있는지 데이터만 추출
question = []
for ct in range(len(df)):
  if "?" in df.text[ct]:
    question.append(df.text[ct])


# In[13]:


question = pd.DataFrame({'text':question})


# In[14]:


question


# In[15]:


question['q_len'] = question['text'].str.len()
question


# In[16]:


que_list = question[question['q_len']<15]
que_list


# In[5]:


pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 100)


# In[18]:


final_list = que_list['text'].sample(n=100)
final_list


# In[19]:


# 인칭대명사 필터링
filter = final_list['text'].str.contains('아빠|오빠|너희|너네|언니|다들')
final_list = final_list[~filter]
final_list

