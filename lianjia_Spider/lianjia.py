import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from openpyxl import workbook


def get_html(url):
    ua = UserAgent().chrome
    response = requests.get(url, headers={'User-Agent': ua})
    return response.text


def parse_html(data):
    soup = BeautifulSoup(data, 'lxml')
    all_data = soup.find_all(class_='content__list--item--aside')
    prices = soup.find_all(class_='content__list--item-price')
    details = soup.find_all(class_='content__list--item--des')
    for price, data, detail in zip(prices, all_data, details):
        title = data.get("title")
        href = 'https://ty.lianjia.com/zufang/' + data.get("href")
        price = price.em.string
        detail = detail.get_text().replace("    ", "").replace("\n", "")
        save_html(title, href, price, detail)


def save_html(title, href, price, detail):
    ws.append([title, href, price, detail])
    wb.save('链家.xlsx')


if __name__ == '__main__':
    wb = workbook.Workbook()
    ws = wb.active
    ws.append(["标题", '链接', '价格', '详情'])
    for i in range(5):
        url = 'https://ty.lianjia.com/zufang/pg{}'.format(i)
        data = get_html(url)
        parse_html(data)
