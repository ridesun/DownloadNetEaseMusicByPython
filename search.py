import os
import json
import urllib
import urllib.request
from urllib.request import urlopen
from urllib.parse import quote
import re
def download(name):
	url='http://127.0.0.1:3000/search?keywords='+ quote(name) + '&limit=1&type=1'
	json=str(urlopen(url).read(),encoding=('utf-8'))
	get_dict=json.loads(json)
	music_id=get_dict['result']['songs'][0]['id']
	music_url='http://music.163.com/song/media/outer/url?id='+str(music_id)+'.mp3' 
        com='wget -O /home/pi/Music/'+a+'.mp3 '+music_url 
        z=os.system(com)


