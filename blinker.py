from Blinker import *
import tts,play_music,pygame,search

BUTTON_1 = ('ButtonKey')

Blinker.setMode(BLINKER_WIFI)
Blinker.begin()
Blinker.wInit('play', W_BUTTON) 
a=0
if __name__ == '__main__':
    while True:
        Blinker.run()

        if Blinker.available() == True:
           data = Blinker.readString()
#              search.download(data[2:])
           tts.playmusic(data)
        if Blinker.button('play'):
           Blinker.notify("!播放")
           tts.playmusic('开始播放')
           play_music.play_music()
        if Blinker.button('pause'):
           a=not a
           if a:
              pygame.mixer.music.pause()
           else:
              pygame.mixer.music.unpause()
Blinker.delay(2000)
