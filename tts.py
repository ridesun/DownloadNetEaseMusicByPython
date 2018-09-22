import urllib,time,urllib.request,re,pygame,eyed3,os
from urllib.request import urlopen
from urllib.parse import quote
from urllib.request import urlretrieve

def playmusic(tex):
    api_token='24.8e94eac433b69d64441eee318222ac9b.2592000.1540171599.282335-11791530'
    url='http://tsn.baidu.com/text2audio?lan=zh&ctp=1&cuid=pi&tok='+api_token +'&tex='+ quote(tex) + '&vol=9&spd=4&pit=4&aue=3&per=0'
    urlretrieve(url,'tts.mp3')
    a=eyed3.load('tts.mp3')
    music_time=a.info.time_secs
    pygame.mixer.init()
    pygame.mixer.music.load('tts.mp3')
    pygame.mixer.music.play()
    time.sleep(music_time)
    pygame.mixer.music.stop()
    os.remove('tts.mp3')
