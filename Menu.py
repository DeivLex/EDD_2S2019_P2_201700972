import socket
import select
import sys

import curses #import the curses library
import time
import csv
import curses.textpad
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN #import special KEYS from the curses library

from ListaEnlazadaDoble import ListaDoble

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
	print ("Correct usage: script, IP address, port number")
	exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.connect((IP_address, Port))

def ServerC():
	while True:
		read_sockets = select.select([server], [], [], 1)[0]
		import msvcrt
		if msvcrt.kbhit(): read_sockets.append(sys.stdin)
		for socks in read_sockets:
			if socks == server:
				message = socks.recv(2048)
				print (message.decode('utf-8'))
			else:
				message = sys.stdin.readline()
				texto_a_enviar = message
				server.sendall(texto_a_enviar.encode('utf-8'))	
				sys.stdout.write("<You>")
				sys.stdout.write(message)
				sys.stdout.flush()
	server.close()


holahola = ""

datos = ListaDoble()

def CargaMasiva(direccion):
    with open('E:\\Back Up Charles\\Davis\\Usac\\Semestre 6\\Estructuras\\Practica 2\\ejemplo.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print (row[1])

def textpadCarga():
    inp = curses.newwin(8,55, 0,0)
    inp.addstr(1,1, "Ingrese direccion archivo csv: ")
    sub = inp.subwin(3, 41, 2, 1)
    sub.border()
    sub2 = sub.subwin(1, 20, 3, 2)
    tb = curses.textpad.Textbox(sub2)
    inp.refresh()
    tb.edit()
    return tb.gather()

def OpcionUser():
    node = datos.head

    def paint_menu(win,dato):
        paint_title(win,' USER SELECTION ')          #paint title
        win.addstr(23,20,'Elegir usuario con doble barra espaciadora')
        win.addstr(11,30,dato)             #paint option 1
        win.timeout(-1)                         #wait for an input thru the getch() function

    def paint_title(win,var):
        win.clear()                         #it's important to clear the screen because of new functionality everytime we call this function
        win.border(0)                       #after clearing the screen we need to repaint the border to keep track of our working area
        x_start = round((60-len(var))/2)    #center the new title to be painted
        win.addstr(0,x_start,var)           #paint the title on the screen

    stdscr = curses.initscr() #initialize console
    window = curses.newwin(25,80,0,0) #create a new curses window
    window.keypad(True)     #enable Keypad mode
    curses.noecho()         #prevent input from displaying in the screen
    curses.curs_set(0)      #cursor invisible (0)
    paint_menu(window,'<-- '+node.dato+' -->')      #paint menu

    keystroke = -1
    while(keystroke==-1):
        keystroke = window.getch()  #get current key being pressed
        if(keystroke==KEY_RIGHT): #1
            node = node.siguiente
            paint_menu(window,'<-- '+node.dato+' -->')
            keystroke=-1
        elif(keystroke==KEY_LEFT):
            node = node.anterior
            paint_menu(window,'<-- '+node.dato+' -->')
            keystroke=-1
        elif(keystroke==32):
            NombreUser=node.dato
            return NombreUser
        elif(keystroke==27):
            pass
        else:
            keystroke=-1

    curses.endwin() #return terminal to previous state

def paint_menu(win):
    paint_title(win,' MAIN MENU ')          #paint title
    win.addstr(7,21, '1. Insert Block')             #paint option 1
    win.addstr(8,21, '2. Select Block')       #paint option 2
    win.addstr(9,21, '3. Reports')   #paint option 3
    win.addstr(10,21, '4. Receive Block')         #paint option 4
    win.addstr(11,21, '5. Exit')
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
    if(keystroke==49): 
        hola = textpadCarga()
        holas = str(hola.split())
        k=2
        hoho=''
        while k < len(holas)-2:
            hoho+=str(holas[k])
            k+=1
        CargaMasiva(hoho)
        paint_title(window, ' INSERT BLOCK ')
        window.addstr(8,22,'Carga con exito')
        wait_esc(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==50):
        paint_title(window, ' SELECT BLOCK ')
        window.addstr(5,22,holahola)
        wait_esc(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==51):
        paint_title(window, ' REPORTS ')
        ServerC()
        wait_esc(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==52):
        paint_title(window, ' RECEIVE BLOCK ')
        wait_esc(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==53):
        pass
    else:
        keystroke=-1

curses.endwin() #return terminal to previous state

