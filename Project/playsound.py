import  vlc
import time

p = vlc.MediaPlayer("D:\coding\code program\python program\Project\Satisfya_Imran_Khan.mp3")
p.play()
time.sleep(60)
print("**** Now---stop******")
p.stop()