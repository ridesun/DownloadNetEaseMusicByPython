#-*-coding:UTF-8-*-
import os
from pygame import mixer #从pygame里面导入我们的音乐播放器
from socket import *


host = ''
port =5679	#设备接收端口一会填到手机
bufsize = 1024
addr = (host,port) 
udpServer = socket(AF_INET,SOCK_DGRAM)
udpServer.bind(addr)



def findmus(): #找当前目录下的音乐，mp3和flac格式，aac不支持
    L=[]
    l=os.listdir()
    for f in l:
        if f.find(".mp3")==len(f)-4 or f.find(".flac")==len(f)-5:
            L.append(f)  
    return(L)

def play(x): #播放函数，防止无法载入造成奔溃，这里用了try和except
    try:
        mixer.music.load(x)
        mixer.music.play()
        return 0
    except:
        return 1


def send(sdata): #向手机发送消息的函数
    sdata = sdata.encode()
    udpServer.sendto(sdata,addr)

def Is_Int(s): #判断str是否可以转换为int
    try: 
        int(s)
        return True
    except ValueError:
        return False

L=findmus() #创建一个空的列表用来存放所有找到的音乐
mixer.init() #启动播放器
nowplaying=0 #用来定位当前正在播放的歌曲
print("播放器已启动")
print("找到以下歌曲：")
n=0
for i in L: #列一个歌单
    n=n+1
    print(str(n)+"."+i)

while 1: #熟悉的循环，大家可以自定义对接收到的命令的处理
    data,addr = udpServer.recvfrom(bufsize)
    data=data.decode()
    if data=="退出":
        udpServer.close()
        mixer.quit()
        exit(0)
        
    elif data=="有什么歌":
        n=0
        for i in L:
            n=n+1
            send(str(n)+"."+i)
            
    elif Is_Int(data):
        if play(L[int(data)-1])==0:
            nowplaying=int(data)-1
            send("正在播放:"+L[nowplaying])
        
    elif data=="播放":
        try:
            mixer.music.play()
        except:
            play(L[nowplaying])
            send("正在播放"+L[nowplaying])

    elif data=="暂停":
        mixer.music.pause()

    elif data=="停":
        mixer.music.stop()

    elif data=="下一首":
        nowplaying=nowplaying+1
        if nowplaying>len(L):
            nowplaying=0
        play(L[nowplaying])
        send("正在播放"+L[nowplaying])

    elif data=="上一首":
        nowplaying=nowplaying-1
        if nowplaying<0:
            nowplaying=len(L)
        play(L[nowplaying])
        send("正在播放"+L[nowplaying])  
    else:
        send("对不起，现在只支持这些指令：有什么歌，数字点播，播放，暂停，停，下一首，上一首,退出")
