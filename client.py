# Python program to implement client side of chat room.
import socket
import select
import sys
import os
import csv
import json
import hashlib
import time
import curses #import the curses library
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN #import special KEYS from the curses library

from ListaEnlazadaDoble import ListaDoble
datos = ListaDoble()

INDEX=0
TIMESTAMP=''
CLASS=''
DATA=''
PREVIOUSHASH='0000'
HASH=''
HashString=''

def OpcionUser():
	global INDEX
	node = datos.head()
	for i in range(INDEX):
		print('INDEX: '+str(node.INDEX)+', "TIMESTAMP": "'+node.TIMESTAMP+'", "CLASS": "'+node.CLASS+'", "DATA": '+'Datos'+', "PREVIOUSHASH": "'+node.PREVIOUSHASH+'", "HASH": "'+node.HASH)
		node=node.pSig

def CargaMasiva(direccion):
	global INDEX,TIMESTAMP,CLASS,DATA,PREVIOUSHASH,HASH,HashString
	UnionBytes=''
	jsonEnvio =''
	dia = time.strftime("%d-%m-%y")
	hora = time.strftime("%I:%M:%S")
	with open('C:\\Users\\Davis\\Desktop\\'+direccion) as f:
		reader = csv.reader(f)
		i = 0
		for row in reader:
			if(i==0):
				CLASS = row[1]
			if(i==1):
				TIMESTAMP=dia+'-::'+hora
				DATA = row[1]
				if(INDEX==0):
					PREVIOUSHASH='0000'
				else:
					PREVIOUSHASH=HashString
				UnionBytes=str(INDEX)+TIMESTAMP+CLASS+DATA+PREVIOUSHASH
				bs = bytes(UnionBytes, 'utf-8')
				HASH=hashlib.new('sha256',bs)
				HashString = HASH.hexdigest()
				jsonEnvio= '{ "INDEX": "'+str(INDEX)+'", "TIMESTAMP": "'+TIMESTAMP+'", "CLASS": "'+CLASS+'", "DATA": '+DATA+', "PREVIOUSHASH": "'+PREVIOUSHASH+'", "HASH": "'+HashString+'"'
				#print (jsonEnvio)
			i=1
		INDEX += 1
	return jsonEnvio

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
			rutacsv = input('\nnombre del archivo csv :')
			CadenaJson = CargaMasiva(rutacsv)
			server.sendall(CadenaJson.encode('utf-8'))
			sys.stdout.write("<You>")
			sys.stdout.write(CadenaJson)
			input('\nEsperando respuesta...')
		elif ans=="2":
			OpcionUser()
		elif ans=="3":
			print("Has pulsado la opción 3...")
		elif ans=="4":
			if socks == server:
				message = socks.recv(2048)
				bloque = message.decode('utf-8').replace("\n","")
				if(bloque=='true' or bloque=='True'):
					datos.AddInicio((INDEX-1),TIMESTAMP, CLASS, DATA, PREVIOUSHASH, HashString)
					print("Archivo Insertado")
				elif(bloque=='false' or bloque=='False'):
					print("Archivo no aceptado")
				elif(bloque=="Welcome to [EDD]Blockchain Project!"):
					print(message.decode('utf-8'))
				else:
					print('leer')
			else:
				'''message = sys.stdin.readline()
				texto_a_enviar = message
				server.sendall(texto_a_enviar.encode('utf-8'))	
				sys.stdout.write("<You>")
				sys.stdout.write(message)
				sys.stdout.flush()'''
		elif ans=="5":
			server.close()
		else:
			print("No has pulsado ninguna opción correcta...")
server.close()




