# # import the time module
# import time
import vlc


def Eye():
    p = vlc.MediaPlayer("Bewafa_-_Unforgettable.mp3")
    p.play()
    input("Enter any key to stop this song")
    print("**** Now---stop******")
    p.stop()
# # define the countdown func.


# def countdown(t):

#     while t:
#         mins, secs = divmod(t, 60)
#         timer = '{:02d}:{:02d}'.format(mins, secs)
#         print(timer, end="\r")
#         time.sleep(1)
#         t -= 1
    
#     Eye()
#     print('Fire in the hole!!')


# # input time in seconds
# t = input("Enter the time in seconds: ")

# # function call
# countdown(int(t))
import os
import time

s=60
# m=0
s = int(input("Enter the time in second"))
while s>=0:
    os.system('cls')
    print ( s, 'Seconds')
    time.sleep(1)
    s-=1
    # if s==60:
    #     m+=1
    #     s=60
Eye()    