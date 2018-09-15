from Blinker import *

BUTTON_1 = ('ButtonKey')

Blinker.setMode(BLINKER_WIFI)
Blinker.begin()
Blinker.wInit(BUTTON_1, W_BUTTON) 
Blinker.wInit(tooggle_1, W_TOGGLE)

if __name__ == '__main__':
    while True:
        Blinker.run()

        if Blinker.available() == True:
            data = Blinker.readString()
            
        if Blinker.button(BUTTON_1):
            

Blinker.delay(2000)
