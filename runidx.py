import requests

def run(user_id="",password="",runid1=""):
    url="http://ybt.ssoier.cn:8088/statusx1.php?runidx="+runid1
    r = requests.session()

    r.post('http://ybt.ssoier.cn:8088/login.php', {'username': user_id, 'password': password})

    body={"runidx":runid1}

    runidx=str(r.get(url).content)
    inf=runidx.split("|")[0]
    inf=inf.split(":") #0: user_id 1: problem_id 2: run_id 3: code_length 4: Status
    if inf[4].find("Judging")!=-1:
        return run(user_id,password,runid1)
    print("题    号：%s \n运行编号：%s \n代码长度：%s Bytes \n状    态：%s"
            %(inf[1],inf[2],inf[3],inf[4]))
    try:
        tasknum=len(runidx.split("|"))-2
        print("测试点数量："+str(tasknum))
        taskinf=runidx.split(":")[5].split(",")
        for i in range(tasknum):
            taskstatus=taskinf[i].split("|")[0]
            memory=taskinf[i].split("|")[1][0]
            time=taskinf[i].split("|")[1][1]
            print("测试点ID：%s 状态：%s 空间：%s kb 时间：%s ms"%(str(i+1),taskstatus, memory, time))
    except:
        print("出问题了，请手动查看提交状态")

