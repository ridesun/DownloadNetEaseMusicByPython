import urllib,time,urllib.request,re,pygame,eyed3,os
from urllib.request import urlopen
from urllib.parse import quote
from urllib.request import urlretrieve

def playmusic(tex):
    url='http://tsn.baidu.com/text2audio?lan=zh&ctp=1&cuid=pi&tok=25.43a4d340316196639f8f2b9ab9b912f5.315360000.1852381218.282335-11791530&tex=' + quote(tex) + '&vol=9&spd=4&pit=4&aue=3&per=0'
    urlretrieve(url,'tts.mp3')
    a=eyed3.load('tts.mp3')
    music_time=a.info.time_secs
    pygame.mixer.init()
    pygame.mixer.music.load('tts.mp3')
    pygame.mixer.music.play()
    time.sleep(music_time)
    pygame.mixer.music.stop()
    os.remove('tts.mp3')

