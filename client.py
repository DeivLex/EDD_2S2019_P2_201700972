# Python program to implement client side of chat room.
import pydot
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
from ArbolAvl import AVL

class UniformDictList(list):
    def __getitem__(self, key):
        if isinstance(key, slice):
            return DictView(self, key)
        return super().__getitem__(key)

Arbol = AVL()
datos = ListaDoble()

IndexSelect=''
INDEX=0
TIMESTAMP=''
CLASS=''
DATA=''
PREVIOUSHASH='0000'
HASH=''
HashString=''

def ReporteBlockes():
	node = datos.head()
	graph = pydot.Dot(graph_type='digraph',rankdir="LR",)
	it=0
	while node != datos.final():
		NodeStr='Class: '+node.CLASS+'\n'+'TimeStamp: '+node.TIMESTAMP+'\n'+'PSHASH: '+node.PREVIOUSHASH+'\n'+'HASH: '+node.HASH
		node_temp = pydot.Node(str(it), style="filled", fillcolor="white",shape="box",label=NodeStr)
		graph.add_node(node_temp)
		NextStr='Class: '+node.pSig.CLASS+'\n'+'TimeStamp: '+node.pSig.TIMESTAMP+'\n'+'PSHASH: '+node.pSig.PREVIOUSHASH+'\n'+'HASH: '+node.pSig.HASH
		node_temp2 = pydot.Node(str(it+1), style="filled", fillcolor="white",shape="box",label=NextStr)
		graph.add_node(node_temp2)
		graph.add_edge(pydot.Edge(node_temp, node_temp2,dir="both"))
		node = node.pSig
		it+=1


	graph.write_jpg('ReporteBlockes.jpg')
	os.system('ReporteBlockes.jpg')

def OpcionUser():
	global INDEX
	node = datos.head()
	for i in range(INDEX):
		print('INDEX: '+str(node.INDEX)+', "TIMESTAMP": "'+node.TIMESTAMP+'", "CLASS": "'+node.CLASS+'", "DATA": '+'Datos'+', "PREVIOUSHASH": "'+node.PREVIOUSHASH+'", "HASH": "'+node.HASH)
		print('------------------------------\n------------------------------')
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
				jsonEnvio= '{ "INDEX": "'+str(INDEX)+'", "TIMESTAMP": "'+TIMESTAMP+'", "CLASS": "'+CLASS+'", "DATA": '+DATA+', "PREVIOUSHASH": "'+PREVIOUSHASH+'", "HASH": "'+HashString+'"}'
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
			Arbol.Clear()
			OpcionUser()
			IndexSelect=input('\nSeleccionar: ')
			node = datos.head()
			for i in range(int(IndexSelect)):
				node = node.pSig
			Sad = json.loads(node.DATA)
			Sad1=Sad['value']
			print(Sad1)

		elif ans=="3":
			ReporteBlockes()
		elif ans=="4":
			if socks == server:
				message = socks.recv(2048)
				bloque = message.decode('utf-8').replace("\n","")
				if(bloque=='true' or bloque=='True'):
					datos.AddFinal((INDEX-1),TIMESTAMP, CLASS, DATA, PREVIOUSHASH, HashString)
					print("Archivo Insertado")
				elif(bloque=='false' or bloque=='False'):
					print("Archivo no aceptado")
					INDEX=INDEX-1
				elif(bloque=="Welcome to [EDD]Blockchain Project!"):
					print(message.decode('utf-8'))
				else:
					print(message.decode('utf-8'))
					bloque2 = message.decode('utf-8')
					data= json.loads(bloque2)
					obIndex = data['INDEX']
					INDEX=int(obIndex)
					obTime = data['TIMESTAMP']
					obClass = data['CLASS']
					obData = data['DATA']
					obPre = data['PREVIOUSHASH']
					obHash = data['HASH']
					PREVIOUSHASH=obHash
					Res=input('\nTrue or False: ')
					if Res=='true' or Res=='True':
						datos.AddFinal(obIndex,obTime,obClass,obData,obPre,obHash)
						INDEX+=1
						print("Archivo Insertado")
					else:
						print("Archivo no aceptado")
		elif ans=="5":
			server.close()
		elif ans=="true":
			server.sendall('true'.encode('utf-8'))
			sys.stdout.flush()
		elif ans=="false":
			server.sendall('false'.encode('utf-8'))
			sys.stdout.flush()
		else:
			print("No has pulsado ninguna opción correcta...")
server.close()




