#coding=utf-8
import requests
from bs4 import BeautifulSoup

home_url = 'https://mp.weixin.qq.com/s/noOJMlPBMDQKe50rdmNVOw'

def getbsFromUrl(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html5lib')
    return soup

soup = getbsFromUrl(home_url)
tds_arr = soup.find_all('td')
data_links = []
for td in tds_arr:
    if(td.a != None):
        temp_arr = []
        temp_arr.append(td.a.get_text())
        temp_arr.append(td.a.get('href'))
        
        
        data_links.append(temp_arr)
    elif(td.strong != None):
        data_links.append(td.get_text())
        
print(data_links)
