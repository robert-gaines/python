#!/usr/bin/env python3

from pynput.keyboard import Key,Controller
from Manifesto import ContainManifesto
import pygetwindow as gw
import subprocess
import time

def ActivateEditor():
    #
    subprocess.Popen(['notepad.exe'])
    #
    time.sleep(5)
    #
    editor = gw.getWindowsWithTitle('Untitled')[0]
    #
    editor.activate()

def WriteText(keyboard,text):
    #
    while(True):
        #
        i = 0
        #
        while(i < len(text)):
            #
            for t in text:
                #
                for character in t:
                    #
                    keyboard.press(character)
                    #
                    keyboard.release(character)
                    #
                    time.sleep(.125)
                    #
                keyboard.press(Key.space)
                #
                keyboard.release(Key.space)
                #
                time.sleep(1)
                #
                keyboard.press(Key.enter)
                #
                keyboard.release(Key.enter)
                #
                i += 1
                #
        keyboard.press(Key.ctrl)
        #
        keyboard.press('a')
        #
        keyboard.release(Key.ctrl)
        #
        keyboard.release('a')
        #
        keyboard.press(Key.backspace)
        #
        keyboard.release(Key.backspace)

def main():
    #
    keyboard = Controller()
    #
    ActivateEditor()
    #
    book_text = ContainManifesto()
    #
    WriteText(keyboard,book_text)

if(__name__ == '__main__'):
    #
    main()
