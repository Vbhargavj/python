# # from asyncore import read
# from datetime import date, datetime
# import time
# import  vlc
# # this all function are use in future  
# # wa = py = ey = 0  


# # # this function is use to read detail in file
# # def showDetail():
# #     with open('another.txt','r') as f :
# #         a = f.read()
# #         print(a)

# # # this function is use to change music
# # # use in future  
# # def music_edit(s):
# #     if s=='w' :
# #         print("Enter the path of file")
# #         so = input()
# #         return so
        

# # # this function is use to show option to edit 
# # def Showedit():
# #     print("Enter the water in Litre")
# #     print("Enter the time to take an physical activities")
# #     print("Enter the time to rest your eye ")
    

# # this is function use to play water sound
# def water():
#     p = vlc.MediaPlayer("Imran_Khan_-_Imaginary_(Official_Music_Video)_HD.m4a")
#     p.play()    
#     input("Enter any key to stop this song")
#     print("**** Now---stop******")
#     p.stop()

# # this is function use to play physical sound
# def Physical():
#     p = vlc.MediaPlayer("Satisfya_Imran_Khan.mp3")
#     p.play()
#     input("Enter any key to stop this song")
#     print("**** Now---stop******")
#     p.stop()

# # this is function use to play eye sound
# def Eye():
#     p = vlc.MediaPlayer("Bewafa_-_Unforgettable.mp3")
#     p.play()  
#     input("Enter any key to stop this song")
#     print("**** Now---stop******")
#     p.stop()
# t = 1     
# while t!=0:
#     Eye()   
#     time.sleep(5*11)
#     Physical()
#     time.sleep(5*5)
#     water()
#     t = int(input("Enter the 0 to stop")) 
# # time.sleep(5*11)
from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    # musiconloop("water.mp3", "stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 4*6
    exsecs = 3*6
    eyessecs = 4.5*6

    while True:
        if time() - init_water > watersecs:
            print("Water Drinking time. Enter 'drank' to stop the alarm.")
            musiconloop('Satisfya_Imran_Khan.mp3', 'drank')
            init_water = time()
            log_now("Drank Water at")

        if time() - init_eyes >eyessecs:
            print("Eye exercise time. Enter 'doneeyes' to stop the alarm.")
            musiconloop("D:\\coding\\code program\\python program\\Charly Black - You_re Perfect (TikTok Remix)(Lyrics) perfect body with a perfect smile(MP3_160K).mp3", 'doneeyes')
            init_eyes = time()
            log_now("Eyes Relaxed at")

        if time() - init_exercise > exsecs:
            print("Physical Activity Time. Enter 'donephy' to stop the alarm.")
            musiconloop("Bewafa_-_Unforgettable.mp3", 'donephy')
            init_exercise = time()
            log_now("Physical Activity done at")
