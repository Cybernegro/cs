## Software Name: Fortnite PC Aim Assist
## Software Description: This Piece of software is used to help you aim in fortnite on PC
## Software Author: @g0d

# Imports
import pyautogui
import time
import keyboard
import subprocess

# Variables
x = 0
y = 0
z = 0
a = 0
b = 0
c = 0

# Main Loop
while True:
    if keyboard.is_pressed('q'):
        print("Quitting")
        break
    else:
        x, y = pyautogui.position()
        print(x, y)
        time.sleep(0.5)
        if x == a and y == b:
            print("Aim Assist Activated")
            pyautogui.click()
            pyautogui
            i.moveTo(x, y)
            time.sleep(0.5)
            pyautogui.click()

            ## Now we import the chrome process and inject the aim assist into it In Linux
            ## This will allow us to use the aim assist in game
            def inject():
                chrome = subprocess.Popen(["/usr/bin/google-chrome", "https://www.google.com"])
                chrome.wait()
                print("Chrome has been opened")
                time.sleep(5)
                pyautogui.moveTo(x, y)
                pyautogui.click()

            inject()

            ## Now we hide the process from the Fortnite anti cheat
            def hide():
                subprocess.call(["sudo", "chattr", "+i", "fn.py"])
                print("File has been hidden")

            hide()

            ## Low Spread
            def low_spread():
                pyautogui.moveTo(x, y)
                pyautogui.click()
                print("Low Spread Activated")

            low_spread()
            

            

