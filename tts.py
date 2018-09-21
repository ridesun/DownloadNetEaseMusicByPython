import urllib,time,urllib.request,re,pygame,eyed3,os,api_key_get
from urllib.request import urlopen
from urllib.parse import quote
from urllib.request import urlretrieve

def playmusic(tex):
    url='http://tsn.baidu.com/text2audio?lan=zh&ctp=1&cuid=pi&tok='+api_key_get.get_api() +'&tex='+ quote(tex) + '&vol=9&spd=4&pit=4&aue=3&per=0'
    urlretrieve(url,'tts.mp3')
    a=eyed3.load('tts.mp3')
    music_time=a.info.time_secs
    pygame.mixer.init()
    pygame.mixer.music.load('tts.mp3')
    pygame.mixer.music.play()
    time.sleep(music_time)
    pygame.mixer.music.stop()
    os.remove('tts.mp3')
