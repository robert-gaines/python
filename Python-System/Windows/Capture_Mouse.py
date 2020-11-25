from pynput import mouse, keyboard
import time

strokes = []
handler = open("mouse.txt",'w')


def Movement(x,y):
    #
    print("[*] Movement: X: %s | Y: %s " % (x,y))
    #
    handler.write("[*] Movement: X: %s | Y: %s \n" % (x,y))

def Click(x,y,button,pressed):
    #
    if(pressed):
        #
        print("[*] Button click at: %s " % (pressed))
        #
        handler.write("[*] Button click at: %s \n" % (pressed))
        #
    elif(not pressed):
        #
        print("[*] Released ")
        #
        print("[*] X: %s | Y: %s " % (x,y))
        #
        handler.write("[*] X: %s | Y: %s \n" % (x,y))
        #
    else:
        #
        print("[!] Unknown Input ")
        #
        handler.write("[!] Unknown Input \n")

def Scroll(x,y,dx,dy):
    #
    if(dy < 0):
        #
        print("[*] Scrolled down: %s | %s " % (x,y))
        #
        handler.write("[*] Scrolled down: %s | %s \n" % (x,y))
        #
    else:
        #
        print("[*] Scrolled up: %s | %s " % (x,y))
        #
        handler.write("[*] Scrolled up: %s | %s \n" % (x,y))

def main():
    #
    listener = mouse.Listener(on_move=Movement,
                              on_click=Click,
                              on_scroll=Scroll)
    #
    listener.start()
    
if(__name__ == '__main__'):
    #
    main()
