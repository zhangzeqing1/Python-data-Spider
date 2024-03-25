import requests
from fake_useragent import UserAgent
from lxml import etree
from chaojiying_Python.chaojiying import Chaojiying_Client


class pome(object):
    def __init__(self):
        self.url = "https://so.gushiwen.cn/user/login.aspx"
        self.ua = UserAgent().chrome
        self.headers = {'User-Agent': self.ua}
        self.params = {'from': 'http://so.gushiwen.cn/user/collect.aspx?type=s'}
        self.data = {
            '__VIEWSTATE': 'ZBg22wKCzVGikNAkIE74MSzFP3GiEU/8AchCeOskoSUDJHsTPr0yx03pLw1yT0ucnnBxXdoVIOM/jfR2nwBxOUoC6IA7IxbPDa/aqvNm/3PL1DHJLOVt7mJXsE7F04rbS+qSLOsFARzNPWCIg+P4nMJrS3A=',
            '__VIEWSTATEGENERATOR': 'C93BE1AE',  # 添加这一行
            'from':'http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx%3ftype%3ds',

            'email': '你的',
            'pwd': '你的',
            'code': 'f0a9',
            'denglu': '登录'
        }
        self.session = requests.session()
        self.login_url = 'https://so.gushiwen.cn/user/login.aspx'

    def get_poem(self):
        req = requests.get(self.url, headers=self.headers, params=self.params)
        xml_data = etree.HTML(req.text)
        return xml_data

    def post_poem(self, code):
        self.data["code"] = code
        req = self.session.post(self.url, headers=self.headers, data=self.data)
        print(req.text)

    def parse_poem(self, data):
        code_url = 'https://so.gushiwen.cn' + data.xpath('//*[@id="imgCode"]/@src')[0]
        req = self.session.get(code_url, headers=self.headers, params=self.params).content
        with open("code.jpg", 'wb') as f:
            f.write(req)
        chaojiying = Chaojiying_Client('2660855126', '52013zzq', '	940042')
        im = open('code.jpg', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
        print(chaojiying.PostPic(im, 1004)["pic_str"])
        return chaojiying.PostPic(im, 1004)["pic_str"]

    def run(self):
        data = self.get_poem()
        code = self.parse_poem(data)
        self.post_poem(code)


if __name__ == '__main__':
    pome = pome()
    pome.run()




