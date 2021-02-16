from pygame import mixer
import datetime
import time


def musicon(file, stopper):
    """this function is use to play mp3 file ,
    and to stop this mp3 file you have to write the same text which has in the function"""
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        drank_input = input("Type drank to stop : ")
        if drank_input == stopper:
            mixer.music.stop()
            break
        else:
            continue


drank_time = datetime.datetime.now()

loop_count = 0
while loop_count < 14:
    program_sleeper = time.sleep(2280)
    musicon("DJ.mp3", "drank")
    print(f"you have drank water at : {drank_time}")
    loop_count += 1

water_activity = open("water_activity_file.txt", "a")
water_activity.write(f"\n{drank_time} : drank")
water_activity.close()
