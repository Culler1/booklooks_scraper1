import requests
from bs4 import BeautifulSoup
import pandas as pd
import pdb
from datetime import date
import warnings
warnings.filterwarnings('ignore')

today=date.today()
url = 'http://booklooks.org/book-reports-a-1'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
r = requests.get(url=url, headers=headers)
soup = BeautifulSoup(r.content,'html')
caption = soup.find_all("td")
title = []
n=0
while n <200:
    string1 = caption[n].text
    n=n+4
    title.append(string1)
author = []
n=1
while n <200:
    string1 = caption[n].text
    n=n+4
    author.append(string1)
rating = []
n=2
while n <200:
    string1 = caption[n].text
    n=n+4
    rating.append(string1)
slick_sheet = []
n=3
while n <200:
    string1 = caption[n].text
    n=n+4
    slick_sheet.append(string1)
d = {'title':title, 'author':author, 'rating':rating, 'slick_sheet':slick_sheet}
df = pd.DataFrame(data=d)
url = 'http://booklooks.org/book-reports-1'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
r = requests.get(url=url, headers=headers)
soup = BeautifulSoup(r.content,'html')
caption = soup.find_all("td")
title = []
n=0
while n <len(caption):
    string1 = caption[n].text
    n=n+4
    title.append(string1)
author = []
n=1
while n <len(caption):
    string1 = caption[n].text
    n=n+4
    author.append(string1)
rating = []
n=2
while n <len(caption):
    string1 = caption[n].text
    n=n+4
    rating.append(string1)
slick_sheet = []
n=3
while n <len(caption):
    string1 = caption[n].text
    n=n+4
    slick_sheet.append(string1)
d = {'title':title, 'author':author, 'rating':rating, 'slick_sheet':slick_sheet}
df1 = pd.DataFrame(data=d)
df1 = pd.concat([df,df1])
title = []
author = []
rating = []
slick_sheet=[]
d = {'title':[],'author':[],"rating":[],"slick_sheet":[]}
l1=soup.find_all("th")
for i in range(1,27):
    url = f"http://booklooks.org/book-reports-"+l1[i].text.lower()
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.content,'html')
    caption = soup.find_all("td")
    n=0
    while n <len(caption):
        string1 = caption[n].text
        n=n+4
        title.append(string1)
    n=1
    while n <len(caption):
        string1 = caption[n].text
        n=n+4
        author.append(string1)
    n=2
    while n <len(caption):
        string1 = caption[n].text
        n=n+4
        rating.append(string1)
    n=3
    while n <len(caption):
        string1 = caption[n].text
        n=n+4
        slick_sheet.append(string1)
d = {'title':title, 'author':author, 'rating':rating, 'slick_sheet':slick_sheet}
df2 = pd.DataFrame(data=d)
df1=pd.concat([df1,df2])
    #df2=pd.concat([df1,df])
# df2 = pd.concat(df)
df1=df1[df1.title!='---']
df1.to_csv("bookLooks_"+str(today.strftime("%m_%d_%Y")+".csv"),index=None)
pct_over3=((df1[df1.rating.astype(int)>=3].title.count())/(df1.title.count())).round(2)*100
print("There are "+str(len(df1.title))+" books listed on BookLooks as of "+str(today.strftime("%m/%d/%Y"))+".")
print("Roughly "+str(pct_over3)+"% of those titles are rated three or higher.")
print(str(df1.author.value_counts().index[0])+" is the most frequently mentioned author with "+str(df1.author.value_counts()[0])+" titles in this list. \n")
