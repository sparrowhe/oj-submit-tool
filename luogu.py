import requests
import json
import sys
csrf_token=""

c="COOKIES_HERE"
cookies = dict(map(lambda x:x.split('='),c.split(";")))

problemSubmit="https://www.luogu.org/api/problem/submit/"+sys.argv[2]

headers = {'origin': 'https://www.luogu.org',
'referer': 'https://www.luogu.org/',
'x-csrf-token': csrf_token,
'x-requested-with': 'XMLHttpRequest',
'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2526.80 Safari/537.36 Core/1.45.933.400 QQBrowser/9.0.8699.400',
'Accept-Encoding' : 'gzip, deflate, sdch'}

code=open(sys.argv[1], "r")

body={"verify":"",
"enableO2":0,
"lang":3,
"code":code.read()
}

re=requests.post(problemSubmit,cookies=cookies,headers=headers,data=body).json()
print(re.get("data"))

