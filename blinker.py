from Blinker import *
import tts,play_music

BUTTON_1 = ('ButtonKey')

Blinker.setMode(BLINKER_WIFI)
Blinker.begin()
Blinker.wInit('play', W_BUTTON) 

if __name__ == '__main__':
    while True:
        Blinker.run()

        if Blinker.available() == True:
            data = Blinker.readString()
            tts.playmusic(data)
        if Blinker.button('play'):
           Blinker.notify("!播放")
           play_music.play_music()
        if Blinker.button('pause'):
           play_music.pause()
Blinker.delay(2000)
