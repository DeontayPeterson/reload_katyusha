import time
import pyautogui
import keyboard
import threading

driver = (1055, 510)
gunner = (1055, 530)
rocket = (1180, 324) #255, 255, 255

truck_invo = (508, 476) #255,255,255

foxhole = pyautogui.getWindowsWithTitle('War  ')[0]
foxhole.activate()

exit_script = False
start_stop = False


def take_exit():
    time.sleep(.4)
    pyautogui.click(rocket)
    time.sleep(6.3)
    keyboard.press_and_release('e')
    time.sleep(.02)
    keyboard.press_and_release('q')
    time.sleep(.2)

def enter_gunner():
    keyboard.press('shift')
    time.sleep(.07)
    keyboard.press_and_release('q')
    time.sleep(.02)
    keyboard.release('shift')
    pyautogui.click(gunner)
    time.sleep(.2)

def reload_enter_driver():
    keyboard.press_and_release('r')
    time.sleep(3.9)
    keyboard.press_and_release('q')
    time.sleep(.2)
    keyboard.press('shift')
    time.sleep(.2)
    keyboard.press_and_release('q')
    time.sleep(.09)
    keyboard.release('shift')
    time.sleep(.1)
    pyautogui.click(driver)
    time.sleep(.2)
    keyboard.press_and_release('e')
    time.sleep(.09)




def ss_listener():
    global start_stop
    global exit_script

    while not exit_script:
        if not start_stop and keyboard.is_pressed('-'):
            start_stop = True
            print('Starting to load')
            time.sleep(.1)
        elif start_stop and keyboard.is_pressed('-'):
            start_stop = False
            print('Stopping loading after this shell..')
            time.sleep(.1)
        if not exit_script and keyboard.is_pressed('5'):
            exit_script = True
            quit()
        time.sleep(.001)
    
listen_thread = threading.Thread(target=ss_listener)
listen_thread.start()

def reloader():
    global start_stop
    global exit_script
    while not exit_script:
        if start_stop:
            take_exit()
            enter_gunner()
            reload_enter_driver()
            time.sleep(.1)
        time.sleep(.01)

reloader()

