import requests
from bs4 import BeautifulSoup
import hashlib
import time

def get_data(date, music_id):
    s = [
    "NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt",
    "appid=1014",
    f"clienttime={date}",
    "clientver=20000",
    "dfid=2C7VDM4SKzyc0hw0b14939GC",
    f"encode_album_audio_id={music_id}",
    "mid=e0509f45a1a8840c90e66511360e5a82",
    "platid=4",
    "srcappid=2919",
    "token=",
    "userid=0",
    "uuid=e0509f45a1a8840c90e66511360e5a82",
    "NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt"
]
    string = ''.join(s)
    MD5 = hashlib.md5()
    MD5.update(string.encode('utf-8'))
    signature = MD5.hexdigest()
    print(signature)
    return signature


def get_response(html, params):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Cookie': 'kg_mid=e0509f45a1a8840c90e66511360e5a82; kg_dfid=2C7VDM4SKzyc0hw0b14939GC; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; KuGooRandom=66661712840582948; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1712840563,1712882298; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22gzverifycode.service.kugou.com%22%5D%5D%7D; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22gzlogin-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22gzreg-user.kugou.com%22%5D%5D%7D; kg_mid_temp=e0509f45a1a8840c90e66511360e5a82; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1712882323'
    }
    response = requests.get(html, headers=headers, params=params)
    return response



def get_info(music_id):
    """获取歌名&音频链接"""
    timestamp_ms = int(time.time() * 1000)
    url_detail = 'https://wwwapi.kugou.com/play/songinfo'
    signature = get_data(timestamp_ms, music_id)
    params = {
        'srcappid': '2919',
        'clientver': '20000',
        'clienttime': timestamp_ms,
        'mid': 'e0509f45a1a8840c90e66511360e5a82',
        'uuid': 'e0509f45a1a8840c90e66511360e5a82',
        'dfid': '2C7VDM4SKzyc0hw0b14939GC',
        'appid': '1014',
        'platid': '4',
        'token': '',
        'encode_album_audio_id': music_id,
        'userid': '0',
        'signature': signature
    }
    # print(get_response(url_detail, params).text)
    json_data = get_response(url_detail,params).json()
    # 歌名
    music_name = json_data['data']['song_name']
    # 音频链接
    music_data = json_data['data']['play_url']
    print(music_name, music_data)
    return music_name,music_data

def save_song(music_name,music_data):
    with open('music/'+music_name+'.mp3', 'wb')as f:
        content = get_response(music_data).content
        f.write(content)



url = 'https://www.kugou.com/yy/rank/home/1-49223.html?from=rank'
t = {}
response = get_response(url, t)
soup = BeautifulSoup(response.text, 'lxml')

pics = soup.select('div.pc_temp_songlist ul li')
imgs = soup.select('div.pc_temp_songlist ul li a.pc_temp_songname')
for pic, img in zip(pics, imgs):
    name, url = get_info(pic['data-eid'])
    save_song(name, img)


