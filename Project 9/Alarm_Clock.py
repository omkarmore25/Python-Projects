from playsound import playsound
import time
import os

def clear():
    os.system("cls")  

# CLEAR = "\033[2J"
# CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed = 0
    clear()

   # print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        clear()
        print(f"Alarm is set for = {minutes_left:02d}:{seconds_left:02d}")

    playsound("Project 9/alarm.mp3")     

     
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))
Total_seconds = minutes *60 + seconds
alarm (Total_seconds)
