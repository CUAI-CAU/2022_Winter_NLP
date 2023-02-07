#!/usr/bin/env python
# coding: utf-8

# In[5]:


#pip install wikipedia-api


# In[1]:


import pandas as pd
 
meaning = pd.read_table('C:/Users/minjuKim/Desktop/CUAI_2022/Winter Conference/nlp_voca_cleaned.txt',sep=',')


# In[2]:


import wikipediaapi


# In[3]:


wiki=wikipediaapi.Wikipedia('ko')


# In[5]:


meaning


# In[6]:


for i in meaning:
    page_py = wiki.page(i)
    print(i)
    print("Page - Summary: %s" % page_py.summary[0:1000])


# In[ ]:


#데이터 출력
'''
with open("파이썬.txt", "w") as f:
    f.write(p_wiki.text)
'''    

