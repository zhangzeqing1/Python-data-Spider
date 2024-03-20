import json
from jsonpath import jsonpath
import requests
from fake_useragent import UserAgent
import csv


class Wangyi(object):
    def __init__(self):

        self.ua = UserAgent().chrome
        self.headers = {'User-Agent': self.ua}
        self.file = open('wangyi.csv', 'w', encoding='utf-8', newline='')
        self.file_csv = csv.writer(self.file)
        self.file_csv.writerow(['标题', '链接'])

    def get_data(self, url):
        response = requests.get(url, headers=self.headers)
        data = response.text
        data = data[14:-1]
        # 还可以使用正则或则replace
        json_data = json.loads(data)
        return json_data

    def parse_data(self, json_data):
        titles = jsonpath(json_data, '$..title')
        tlinks = jsonpath(json_data, '$..tlink')
        for title, tlink in zip(titles, tlinks):
            self.save_data(title, tlink)

    def save_data(self, title, tlink):
        self.file_csv.writerow([title, tlink])

    def run(self):
        url = 'https://news.163.com/special/cm_yaowen20200213/?callback=data_callback'
        json_data = self.get_data(url)
        self.parse_data(json_data)
        for i in range(2,5):
            url = 'https://news.163.com/special/cm_yaowen20200213_0{}/?callback=data_callback'.format(i)
            json_data = self.get_data(url)
            self.parse_data(json_data)


if __name__ == '__main__':
    wy = Wangyi()
    wy.run()
