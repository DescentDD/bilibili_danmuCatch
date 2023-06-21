import json
import time
from urllib import request

sec=3#芝士刷新频率
uid = 25667694#芝士直播间号码
url = 'http://api.live.bilibili.com/ajax/msg?roomid='+ str(uid)
last=[]
def search():
    global last
    req = request.Request(url)
    req= request.urlopen(req).read()
    req=json.loads(req)
    req=req['data']['room']
    i=0
    for j in range(len(last)):
        if(req[i]==last[j]):
            i=len(last)-j
            break
    while(i<len(req)):
        message=req[i]
        with open('log.txt','a',encoding='utf-8')as f:
            f.write(message['timeline']+'\t')
            print(message['timeline']+'\t',end='')
            if message['medal']!=[]:
                print('粉丝牌:'+str(message['medal'][1]),end='')
                f.write('粉丝牌:'+str(message['medal'][1]))
            else:
                print('没有粉丝牌')
                f.write('没有粉丝牌')
            print('\t'+message['nickname']+':'+message['text'])
            f.write('\t'+message['nickname']+':'+message['text']+'\n')
        i+=1

    last=req


while True:
    #now = time.strftime("%m月%d日%H:%M:%S", time.localtime())
    #print('记录时间:'+now)#这两个可能会很吵可以注释掉
    search()
    time.sleep(int(sec))
