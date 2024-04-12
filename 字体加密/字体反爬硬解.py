import requests
from bs4 import BeautifulSoup

url = 'https://www.shixiseng.com/interns'
params = {
    'page': '1',
    'type': 'intern',
    'keyword': 'Python',
    'city': '全国'
}
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}
response = requests.get(url, params=params, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
pics = soup.select('div.primary-content.f-l div div div.intern-wrap.interns-point.intern-item div div.f-l p a')
for pic in pics:
    print("职位：" + pic['title']。replace('&#xedb4', 'p')
          。replace('&#xe6f2', 'y')
          。replace('&#xf4b2', 't')
          。replace('&#xf66d', 'h')
          。replace('&#xf53e', 'o')
          。replace('&#xf00f', 'n')
          。replace('&#xef8c', '生')
          。replace('&#xf7af', 'P')
          。replace('&#xedaa', '工')
          。replace('&#xeaff', '程')
          。replace('&#xe669', '师')
          。replace('&#xf573', '端'))
