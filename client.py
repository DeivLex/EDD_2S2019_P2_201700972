# Python program to implement client side of chat room.
import socket
import select
import sys
import os

def menu():
	
	#os.system('cls') # NOTA para windows tienes que cambiar clear por cls
	print ("Selecciona una opción")
	print ("\t1 - Insert Block")
	print ("\t2 - Select Block")
	print ("\t3 - Reports")
	print ("\t4 - Receive Block")
	print ("\t5 - Exit")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
	print ("Correct usage: script, IP address, port number")
	exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.connect((IP_address, Port))

while True:
	read_sockets = select.select([server], [], [], 1)[0]
	import msvcrt
	if msvcrt.kbhit(): read_sockets.append(sys.stdin)
	for socks in read_sockets:
		menu()
		ans = input('\nElegir una opcion :') 
		if ans=="1":
			print("Has pulsado la opción 1...")
		elif ans=="2":
			print("Has pulsado la opción 2...")
		elif ans=="3":
			print("Has pulsado la opción 3...")
		elif ans=="4":
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
		elif ans=="5":
			server.close()
		else:
			print("No has pulsado ninguna opción correcta...")
server.close()




