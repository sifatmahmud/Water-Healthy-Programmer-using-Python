from pygame import mixer
import datetime
import time


def musicon(file, stopper):
    """this function is use to play mp3 file and to stop this mp3 file you have to write the same text which has in the function"""
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        drank_input = input("type to stop : ")
        if drank_input == stopper:
            mixer.music.stop()
            break
        else:
            continue


c = 0
while (c < 14):  
    a = time.sleep(2280)
    musicon("DJ.mp3", "drank")
    water_activity = open("water_activity_file.txt", "a")
    water_activity.write(f"\n{datetime.datetime.now()} : drank")
    water_activity.close()
    c += 1
