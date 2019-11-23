import requests
import runidx
import sys
user_id=""
password=""
problem_id=""
'''
action.php
user_id 
problem_id 1000
language:
G++ 1
GCC 2
JAVA 3
PASCAL 4
PYTHON 5

source

'''
code=open(sys.argv[1], "r")
code1=code.read()
url="http://ybt.ssoier.cn:8088/action.php" 

'''
headers = {'origin': 'http://ybt.ssoier.cn:8088',
'referer': 'http://ybt.ssoier.cn:8088/login.php',
'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2526.80 Safari/537.36 Core/1.45.933.400 QQBrowser/9.0.8699.400',
'Accept-Encoding' : 'gzip, deflate, sdch',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'
}
'''
r = requests.session()

r.post('http://ybt.ssoier.cn:8088/login.php', {'username': user_id, 'password': password})



body={"user_id":user_id,
"problem_id":sys.argv[2],
"language":'1',
"source":code1,
"submit":"提交"
}

a=r.post(url,data=body)

print(a.content.decode().split("runidx=")[1].split("';")[0])
runid=a.content.decode().split("runidx=")[1].split("';")[0]
runidx.run(user_id,password,str(runid))