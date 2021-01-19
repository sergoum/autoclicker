import mouse
import keyboard
import time
while True:
    thing = True
    while thing == True:
        while not keyboard.is_pressed('c'):
            pass
        while not keyboard.is_pressed('l'):
            pass
        while not keyboard.is_pressed('i'):
            pass
        while not keyboard.is_pressed('c'):
            pass
        while not keyboard.is_pressed('k'):
            pass
        while thing == True:
            mouse.click()
            time.sleep(0.01)
            if keyboard.is_pressed('s'):
                thing = False
