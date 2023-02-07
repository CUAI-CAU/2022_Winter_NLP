#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().system('pip install SpeechRecognition')


# In[10]:


get_ipython().system('pip install pyaudio')


# #### 한글 사용이 가능하고 무료인 라이브러리는 google의 speech recognition

# In[1]:


import speech_recognition as sr
#import sys 텍스트 저장시 사용

# 발화 내용 저장
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say Something")
    speech = r.listen(source)

#sys.stdout = open('audio_output.txt', 'w') 텍스트 저장시 사용

# 예외 처리 구문으로 인식한 음성 출력
try:
    audio = r.recognize_google(speech, language="ko-KR")
    print("Your speech thinks like\n " + audio)
except sr.UnknownValueError:
    print("Your speech can not understand")
except sr.RequestError as e:
    print("Request Error!; {0}".format(e))

