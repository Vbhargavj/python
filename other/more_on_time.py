import time
import vlc
t = int(input())


def teye(s):
    while s > 0:
        # os.system('cls') this line is clean our output
        # print ( s, 'Seconds')
        # time.sleep(s*6)
        s -= 1
        p = vlc.MediaPlayer("Bewafa_-_Unforgettable.mp3")
        p.play()
        input("Enter any key to stop this song")
        print("**** Now---stop******")
        p.stop()


def physical(s):
    # while s > 0:
    #     # os.system('cls') this line is clean our output
    #     # print ( s, 'Seconds')
    #     # time.sleep(s*6)
    #     s -= 1
        p = vlc.MediaPlayer(
            "Imran_Khan_-_Imaginary_(Official_Music_Video)_HD.m4a")
        p.play()
        input("Enter any key to stop this song")
        print("**** Now---stop******")
        p.stop()


def water(s):
    # time.sleep(s*6)
    s -= 1
    p = vlc.MediaPlayer("Satisfya_Imran_Khan.mp3")
    p.play()
    input("Enter any key to stop this song")
    print("**** Now---stop******")
    p.stop()


while t:
    t -= 1
    print(t)
    if t % 30 == 0:
        teye(1)
    elif t % 45 == 0:
        physical(1)
    elif t % 10 == 0:
        water(1)
    time.sleep(1)