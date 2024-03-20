import requests
from fake_useragent import UserAgent
from lxml import etree
from pymysql import connect


def get_page(url):
    ua = UserAgent().chrome
    headers = {"User-Agent": ua}
    response = requests.get(url, headers=headers)
    parse_data = etree.HTML(response.text)
    return parse_data


def parse_page(parse_data, cs):
    paths = parse_data.xpath('//ul[@class="list2"]/li/h3/a/@href')
    titles = parse_data.xpath('//ul[@class="list2"]/li/h3/a/text()')
    # parse_data = parse_data.xpath('/html/body/div[6]/div[1]/div/ul/li[1]/h3/a')
    for path, title in zip(paths, titles):
        parse_detail(path, title, cs)


def parse_detail(path, title, cs):
    parse_data = get_page(path)
    data = parse_data.xpath('//div[@class="con"]/div//text()')[2: -4]
    # data = parse_data.xpath('/html/body/div[6]/div[1]/div/div[3]/div[1]/p/text()')
    data = ''.join(data)
    print(title)
    save_html(title, data, cs)


def save_html(title, data ,cs):
    sql = "insert into xpath_demo(title, con) values (%s, %s)"
    cs.execute(sql, (title, data))
    conn.commit()


if __name__ == '__main__':
    conn = connect(
        user= 'root',
        password='root',
        host='127.0.0.1',
        port=3306,
        database="spider0306",
        charset='utf8mb4'
    )
    cs = conn.cursor()
    url = "http://www.hnbitebi.com/hlist-7-1.html"
    parse_data = get_page(url)
    parse_page(parse_data, cs)
