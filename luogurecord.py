import json
import requests
import sys
csrf_token=""

c="cookies_here"
cookies = dict(map(lambda x:x.split('='),c.split(";")))

rid="https://www.luogu.org/record/"+"%s?_contentOnly=1"%sys.argv[1]

headers = {'origin': 'https://www.luogu.org',
'referer': 'https://www.luogu.org/',
'x-csrf-token': csrf_token,
'x-requested-with': 'XMLHttpRequest',
'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2526.80 Safari/537.36 Core/1.45.933.400 QQBrowser/9.0.8699.400',
'Accept-Encoding' : 'gzip, deflate, sdch'}

re=requests.post(rid,cookies=cookies,headers=headers).json()

print("Score: %d"%re.get("currentData")['record']['score'])