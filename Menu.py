import curses #import the curses library
import time
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN #import special KEYS from the curses library

import curses.textpad
from ListaEnlazadaDoble import ListaDoble

datos = ListaDoble()

def test_textpad():
    inp = curses.newwin(8,55, 0,0)
    inp.addstr(1,1, "Ingrese nombre del archivo:")
    sub = inp.subwin(3, 41, 2, 1)
    sub.border()
    sub2 = sub.subwin(1, 20, 3, 2)
    tb = curses.textpad.Textbox(sub2)
    inp.refresh()
    tb.edit()
    return tb.gather()

def paint_menu(win):
    paint_title(win,' MAIN MENU ')          #paint title
    win.addstr(7,21, '1. Insert Block')             #paint option 1
    win.addstr(8,21, '2. Select Block')       #paint option 2
    win.addstr(9,21, '3. Reports')   #paint option 3
    win.addstr(10,21, '4. Exit')         #paint option 4
    win.timeout(-1)                         #wait for an input thru the getch() function

def paint_title(win,var):
    win.clear()                         #it's important to clear the screen because of new functionality everytime we call this function
    win.border(0)                       #after clearing the screen we need to repaint the border to keep track of our working area
    x_start = round((60-len(var))/2)    #center the new title to be painted
    win.addstr(0,x_start,var)           #paint the title on the screen

def wait_esc(win):
    key = window.getch()
    while key!=27:
        key = window.getch()


stdscr = curses.initscr() #initialize console
window = curses.newwin(20,60,0,0) #create a new curses window
window.keypad(True)     #enable Keypad mode
curses.noecho()         #prevent input from displaying in the screen
curses.curs_set(0)      #cursor invisible (0)
paint_menu(window)      #paint menu

keystroke = -1
while(keystroke==-1):
    keystroke = window.getch()  #get current key being pressed
    if(keystroke==49): #1
        paint_title(window, ' INSERT BLOCK ')
        wait_esc(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==50):
        paint_title(window, ' SELECT BLOCK ')
        wait_esc(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==51):
        paint_title(window, ' REPORTS ')
        wait_esc(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==52):
        pass
    else:
        keystroke=-1

curses.endwin() #return terminal to previous state

