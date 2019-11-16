#! python3
# simpleTimer.py - very obscure, crude and simple timer. Working only on Windows.

import winsound
import time


def beep_alarm():
    for repeats in range(7):
        winsound.Beep(3000, 500)
        winsound.Beep(6000, 300)


timerDuration = int(input("Please, provide duration for the timer in seconds: "))

hours, minutes, seconds = 0, 0, 0
for i in range(timerDuration):
    print('\n' * 100)

    seconds += 1
    if seconds == 60:
        minutes += 1
        seconds = 0
    if minutes == 60:
        hours += 1
        minutes = 0

    print(str(hours) + ':' + str(minutes) + ':' + str(seconds))
    time.sleep(1)


beep_alarm()
