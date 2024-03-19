import requests
import json
import re
from fake_useragent import UserAgent
from jsonpath import jsonpath
from openpyxl import workbook


def get_html(page):
    url = 'https://i.news.qq.com/web_feed/getHotModuleList'
    data_dict = {
        "qimei36": "0_cabdcbcca5883",
        "base_req": {
            "from": "pc"
        },
        "channel_id": "news_news_top",
        "device_id": "0_cabdcbcca5883",
        "item_count": 20,
        "forward": "2"
    }

    data_dict["flush_num"] = page  # 设置 flush_num 的值为 page

    data = json.dumps(data_dict)
    ua = UserAgent().chrome
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Content-Type': 'application/json;charset=UTF-8',
        'Content-Length': '157',

    }
    response = requests.post(url, headers=headers, data=data)
    return response.json()


def parse_page(data):
    data_title = jsonpath(data, '$..title')
    data_url = jsonpath(data, '$..url')
    data_media = data["data"]
    print(len(data_media))
    media_name = []
    for data1 in data_media:
        try:
            chl_name = data1["media_info"]["chl_name"]
            media_name.append(chl_name)
        except:
            media_name.append("没有来源")
    print(len(data_url), len(data_title), len(media_name))
    for url, title, name in zip(data_url, data_title, media_name):
        print(url, title, name)
        save_page(url, title, name)
        print("=======")


def save_page(url, title, name):
    pass
    ws.append([title, url, name])
    wb.save("Tencent.xlsx")


if __name__ == '__main__':
    wb = workbook.Workbook()
    ws = wb.active
    ws.append(["文章", "链接", "来源"])
    for i in range(1, 12):
        json_data = get_html(i)
        parse_page(json_data)

# with open('tencent.html', 'w', encoding='utf-8') as f:
#     f.write(response.json())

