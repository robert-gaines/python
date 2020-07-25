from pynput.mouse import Controller
import random
import time

def RandomMouse():
    #
    mouse = Controller()
    #
    mouse.position = (1500,1500)
    #
    mouse.position = (random.randint(-1000,1000),random.randint(-1000,1000))
    #
    time.sleep(1)


while(True):
    #
    RandomMouse()

