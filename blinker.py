from Blinker import *
import tts

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

Blinker.delay(2000)
