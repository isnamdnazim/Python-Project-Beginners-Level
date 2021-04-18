import pyautogui
import time


comments = ["Hi", "Hello","5k comments!!!","Okey","waiting for 5k comments!!! ", "Nothing else","you will make the video"]


time.sleep(5)

for i in range(5000):
    pyautogui.typewrite(comments[i%7])
    pyautogui.typewrite("\n")
    time.sleep(2)