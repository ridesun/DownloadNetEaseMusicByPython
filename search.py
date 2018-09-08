import fileinput 
import os
import json
import urllib
import urllib.request
from urllib.request import urlopen
from urllib.parse import quote
import re
def search():
	b='http://144.202.5.144:3000/search?keywords='+ quote(a) + '&limit=1&type=1'
	c=str(urlopen(b).read(),encoding=('utf-8'))
	d=json.loads(c)
	id=d['result']['songs'][0]['id']
	print(id)
	return id
def geturl():
	f='http://music.163.com/song/media/outer/url?id='+str(id)+'.mp3'
	return f
file = open("list.txt") 
while 1:
    lines = file.readlines(100000)
    if not lines:
        break
    for y in lines:
        a=y.strip() 
        id=search()
        url=geturl()
        print(url)
        com='wget -O /home/pi/Music/'+a+'.mp3 '+url 
        z=os.system(com)
        if z==0:
         print('已下载歌曲.',a)
        else: print('下载失败')
file.close()



