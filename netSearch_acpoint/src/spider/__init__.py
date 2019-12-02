#coding=utf-8
import requests
from bs4 import BeautifulSoup
r = requests.get('https://mp.weixin.qq.com/s/noOJMlPBMDQKe50rdmNVOw')
# print(r.text)
soup = BeautifulSoup(r.text,'html5lib')
tds_arr = soup.find_all('td')
data_links = []
for td in tds_arr:
    if(td.a != None):
        temp_arr = []
        temp_arr.append(td.a.get_text())
        temp_arr.append(td.a.get('href'))
        
        #todo: 点击小项进去 爬 页面内容
        
        data_links.append(temp_arr)
    elif(td.strong != None):
        data_links.append(td.get_text())
        
print(data_links)
