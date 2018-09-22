import os,pygame,time,eyed3
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
    while c==1: 
          z=list1[b]
          musicname='/home/pi/Music/' + z 
          pygame.mixer.music.load(musicname)
          q=eyed3.load(musicname)
          atime=q.info.time_secs
          print(atime)
          pygame.mixer.music.play()
          time.sleep(atime)
          pygame.mixer.music.stop()
          b=b+1
          if b>len(list1):
             break
play_music()

