import datetime

import requests
import execjs
with open('btb.js','r',encoding='utf8') as f:
    content=f.read()
code=execjs.compile(content).call('get_code')


headers = {
    'authority': 'api.mytokenapi.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/x-www-form-urlencoded;charset=utf-8',
    'origin': 'https://mytokencap.com',
    'referer': 'https://mytokencap.com/',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}

params = {
    'pages': '1,1',
    'sizes': '100,100',
    'subject': 'market_cap',
    'language': 'zh_CN',
    'timestamp': '1701780921160',
    'code': code,
    'platform': 'web_pc',
    'v': '0.1.0',
    'legal_currency': 'USD',
    'international': '1',
}

response = requests.get('https://api.mytokenapi.com/ticker/currencylistforall', params=params, headers=headers)
print(response.json())