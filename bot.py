import random,time
from pyautogui import *
e='enter'
trabalhos=['bowsaw', 'boat', 'pickaxe']
escolha=random.choice(trabalhos)
PAUSE=0.5
hotkey('alt', 'tab')
for c in range(30000):
    for j in range(6):
        for h in range(2):
            for b in range(5):
                time.sleep(61)
                write('rpg hunt')
                press(e)
            time.sleep(1)
            write('rpg bowsaw')
            press(e)
        time.sleep(1)
        pwrite('rpg withdraw 2000')
        press(e)
        write('rpg buy seed')
        press(e)
        write('rpg farm')
        press(e)
    time.sleep(5)
    write('rpg adv')
    press(e)
    time.sleep(1)
    write('rpg heal')
    press(e)