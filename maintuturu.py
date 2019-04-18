import browser_cookie3
import requests
from bs4 import BeautifulSoup
# it'll be removed
f = open('password.txt')
passlog = [];
for i in f:
    passlog.append(i)
# 

urls = ['https://kwork.ru/api/user/login'] #site urls
s = requests.Session() 
data = {'track_client_id': '2131145171.1548624821', 'l_username': passlog[0],'l_password':passlog[1]} #makin' request data
r = s.post(urls[0], data=data)
z = requests.get('https://kwork.ru/projects', cookies=s.cookies)
fss = open('answer.html','w', encoding='utf-8') #just for check the answer
soup = BeautifulSoup(z.text, 'html.parser')
text = str(soup.find("div", {"class": "card"}))
print(text)