import requests
from bs4 import BeautifulSoup
import os
#  https://img.tuguaishou.com/ips_templ_preview/c0/91/ff/lg_5854325_1712628817_6614a45122810.jpg!w216_webp?auth_key=1713051000-0-0-38e68449808358de0d8f23a6835e4d39

url = 'https://818ps.com/search-subscribe/1-250-0-0-0-0-qingmingjie-null-10_0_0_0-0-0-0-0-0.html?route_id=17107283807425&route=1,187_1_187_1_187&after_route=1_187,1_187,1_187,1_187&top_id=5854325,5854321,5825677'
headers = {
    'Referer': 'https://818ps.com/index?route_id=17128179372102&route=1,&after_route=1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'Cookie':'acw_tc=2f624a3817128179374717159e33d3d39a4ce0e571162c38a6c1deb8cd1e54; IPSSESSION=c2ppekvbnrciq7fkiume76nu55; ui_818ps=dWlkPTAmdWM9JnY9MSZ1cz1iYWlkdSZ0PWU0NzY4YTI0MTIwM2Y3N2IyNmQ1Y2U1ZGMyNGY0NDViMTcxMjgxNzkzNy41Mzg3NzQ3NCZncj1HUkFZX1JFTEVBU0UmdXJzPQ%3D%3D; track_id=a6155de864e1b3e78b86ec4fa0e03b663fff3e83a61b5b6e413a56d8148b55afa%3A2%3A%7Bi%3A0%3Bs%3A8%3A%22track_id%22%3Bi%3A1%3Bs%3A51%3A%22e4768a241203f77b26d5ce5dc24f445b1712817937.53877474%22%3B%7D; _csrf=80fc0b1319097be26b8cc98586f02e39fe27f88425563998a56b1541c55c8da6a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22%ECA%2A%BA%AA%01%0B%FD%8E%81%10%E9%3D%8D%1A%BFKi%3A8i%23%84%A4M%BF%98%96%21Zr%8B%22%3B%7D; _clck=1eoavir%7C2%7Cfku%7C0%7C1562; AGL_USER_ID=9a5392dc-c9db-4a4d-a794-8a0030bbe76f; Hm_lvt_68ba0271f600f1146717e15ebd6337d1=1712817941; FIRSTVISITED=1712817941.517; _clsk=1cyrkl1%7C1712817997636%7C2%7C1%7Cf.clarity.ms%2Fcollect; 1152_cookie=a%3A3%3A%7Bi%3A0%3Bs%3A15%3A%22818ps.com%2Findex%22%3Bi%3A1%3Bs%3A28%3A%22818ps.com%2Fsubscribe-all.html%22%3Bi%3A2%3Bs%3A196%3A%22818ps.com%2Fsearch-subscribe%2F1-250-0-0-0-0-qingmingjie-null-10_0_0_0-0-0-0-0-0.html%3Froute_id%3D17107283807425%26route%3D1%2C187_1_187_1_187%26after_route%3D1_187%2C1_187%2C1_187%2C1_187%26top_id%3D5854325%2C5854321%2C5825677%22%3B%7D; Hm_lpvt_68ba0271f600f1146717e15ebd6337d1=1712818000; 1520cae3ba303f4352446635c4f1aed1=eyJzZXNzaW9uX2lkIjoiYzJwcGVrdmJucmNpcTdma2l1bWU3Nm51NTUiLCJpcCI6IjE4My4yMDMuMjIzLjUiLCJ0b2tlbiI6IjNlNTZlZGYyNGVkOGQ3OTA0ODIzMGYyZmU1NzAzZjc4In0%3D; 4e8c7c443b427f7cd897f8ff028d909a=eyJzZXNzaW9uX2lkIjoiYzJwcGVrdmJucmNpcTdma2l1bWU3Nm51NTUiLCJpcCI6IjE4My4yMDMuMjIzLjUiLCJ0b2tlbiI6IjI4ZWY5Zjk5ZDk1Mjk4OTI5YjhlOTllMGUyNjE5ZTk0In0%3D; b9e88e60463e46acffe56356b4c38f44=eyJzZXNzaW9uX2lkIjoiYzJwcGVrdmJucmNpcTdma2l1bWU3Nm51NTUiLCJpcCI6IjE4My4yMDMuMjIzLjUiLCJ0b2tlbiI6IjUxYzIzOGYxMDM2OWM0ZWEwZjQ4NDg3NTEwMzFlMDc1In0%3D; nps_pv=4'
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
pics = soup.select('div.box img')
for pic in pics:
    if 'tps://js.' in pic.attrs['src']:
        url = 'https:' + pic['data-original']
    else:
        url = 'https:' + pic['src']

    if not os.path.exists('./img'):
        os.mkdir('./img')
    with open('./img/{}.jpg'.format(pic['title']), 'wb') as f:
        f.write(requests.get(url).content)
        print("正在下载：" + pic['title'] + "src: " + url)

