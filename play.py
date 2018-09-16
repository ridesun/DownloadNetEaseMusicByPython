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
          a=list1[b]
          music_name='/home/pi/Music/' + a 
          a=eyed3.load(music_name)
          music_time=a.info.time_secs
          pygame.mixer.music.load(music_name)
          pygame.mixer.music.play()
          time.sleep(music_time)
          pygame.mixer.music.stop()
          b=b+1
          if b>len(list1):
             break
def pause_music():
    play_music()
    str=input('输入命令')
    if str=='z':
       pygame.mixer.music.pause()
       print('暂停')
    elif str=='b':
       pygame.mixer.music.unpause()
       print('播放')
    else:
       print('未知指令')
pause_music()
