import os,pygame,time
def file_name(file_dir):
    list1=[];
    for files in os.walk(file_dir):
        for a in files:
            list1.append(a)
    return list1[2]

 
def play_music():
    pygame.mixer.init()
    b=0
    c=1
    list1=file_name('/home/pi/Music')
#    while c==1: 
    a=list1[b]
    music_name='/home/pi/Music/' + a 
    pygame.mixer.music.load(music_name)
    pygame.mixer.music.play()
#          pygame.mixer.music.stop()
#          b=b+1
#          if b>len(list1):
#             break

def pause():
    pause= not pause
    if pause==0:
       pygame.mixer.music.pause()
    else:
       pygame.mixer.music.unpause()
