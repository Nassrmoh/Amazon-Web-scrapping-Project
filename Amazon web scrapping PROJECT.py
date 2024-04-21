#!/usr/bin/env python
# coding: utf-8

# In[4]:


from bs4 import BeautifulSoup 
import requests
import smtplib
import time 
import datetime


# In[21]:


URL = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&customId=B0752XJYNL&th=1'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id='productTitle').get_text()
Rating = soup2.find(id='acrCustomerReviewText').get_text()

print (title)
print(Rating)


# In[22]:


Rating = Rating.strip()[:3]
title = title.strip()

print(title)
print(Rating)


# In[30]:


import datetime

today = datetime.date.today()

print(today)


# In[ ]:





# In[31]:


import csv 
header = ['title', 'Rating','today']
data = [title,Rating,today]
with open ('Amazon dataset.csv','w', newline = '', encoding = 'UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)
    


# In[41]:


with open ('Amazon dataset.csv','a+', newline = '', encoding = 'UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[42]:


import pandas as pd
df = pd.read_csv(r"C:\Users\user\Amazon dataset.csv")
df


# In[44]:


def check_rating () :
    URL = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&customId=B0752XJYNL&th=1'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id='productTitle').get_text()
    Rating = soup2.find(id='acrCustomerReviewText').get_text()
    Rating = Rating.strip()[:3]
    title = title.strip()
    import datetime
    today = datetime.date.today()
    import csv 
    header = ['title', 'Rating','today']
    data = [title,Rating,today]
    with open ('Amazon dataset.csv','a+', newline = '', encoding = 'UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)


# In[45]:


while(True):
    check_rating()
    time.sleep(218000)


# In[46]:


import pandas as pd
df = pd.read_csv(r"C:\Users\user\Amazon dataset.csv")
df


# In[ ]:




