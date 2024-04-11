import requests

url = "https://i.news.qq.com/web_feed/getHotModuleList"
for i in range (1, 5):
    payload = "{\"qimei36\":\"0_cabdcbcca5883\",\"base_req\":{\"from\":\"pc\"},\"flush_num\":{{i}},\"channel_id\":\"news_news_top\",\"device_id\":\"0_cabdcbcca5883\",\"item_count\":20,\"forward\":\"2\"}"
    payload = payload.replace("{{i}}", str(i))
    headers = {
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json;charset=UTF-8',
        'cookie': 'pac_uid=0_cabdcbcca5883; iip=0; _qimei_uuid42=1830f0b002e100a14bc08900d927d8138110ab5b97; _qimei_fingerprint=06e0bbe33eb4a4a2ba6634acaa4d3b80; _qimei_q36=; _qimei_h38=2db83c044bc08900d927d8130200000611830f; lcad_appuser=058AA102D21D0AFB; lcad_o_minduid=m3fdZoHrwsNrqwWliqRMU9cHztpumza4; RK=YRmlk4tm2a; ptcz=1ec8fef515e41f783d21a9d61cd7e4b6e270860eb5c7c54f224eae549af39ec5; pgv_pvid=1056270045; _clck=1dsjawk|1|fkm|0; qq_domain_video_guid_verify=7ed66e1fe3325cff; pgv_info=ssid=s38749530; vversion_name=8.2.95; video_omgid=7ed66e1fe3325cff; suid=ek171047164639685569; current-city-name=sxty; lcad_Lturn=134; lcad_LKBturn=124; lcad_LPVLturn=553; lcad_LPLFturn=435; lcad_LPSJturn=628; lcad_LBSturn=445; lcad_LVINturn=554; lcad_LDERturn=331'，
        'origin': 'https://news.qq.com',
        'pragma': 'no-cache',
        'referer': 'https://news.qq.com/',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    for n in response.json()['data']:
        print(n['title'])
