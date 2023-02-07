#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install PyPDF2


# In[1]:


from tika import parser
pdf_path = "C:/Users/minjuKim/Desktop/CUAI_2022/Winter Conference/언어발전소_연습어휘목록1.pdf" 
parsed = parser.from_file(pdf_path)

txt = open('C:/Users/minjuKim/Desktop/CUAI_2022/Winter Conference/nlp_voca.txt', 'w', encoding = 'utf-8')
# nlp_voca.txt에 pdf파일 내용을 write
print(parsed['content'], file = txt)
txt.close()


# In[ ]:


from PyPDF2 import PdfFileReader, PdfFileWriter

원본 = PdfFileReader(open("./files/예시.pdf", 'rb'))

# writer라는 이름의 pdf작성기를 준비
writer = PdfFileWriter()

# 원본 pdf파일에서 원하는 페이지를 추출해서 writer에 추가
writer.addPage(원본.getPage(0))
writer.addPage(원본.getPage(1))
writer.addPage(원본.getPage(4))

# writer가 새 pdf파일로 저장
writer.write(open("./files/output.pdf", 'wb'))

