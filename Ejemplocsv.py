import csv
import json
import hashlib
import time

INDEX=0
TIMESTAMP=''
CLASS=''
DATA=''
PREVIOUSHASH='0000'
HASH=''
UnionBytes=''
jsonEnvio =''
dia = time.strftime("%d-%m-%y")
hora = time.strftime("%I:%M:%S")

with open('C:\\Users\\Davis\\Desktop\\ejemplo.csv') as f:
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
            UnionBytes=str(INDEX)+TIMESTAMP+CLASS+DATA+PREVIOUSHASH
            bs = bytes(UnionBytes, 'utf-8')
            HASH=hashlib.new('sha256',bs)
            HashString = HASH.hexdigest()
            jsonEnvio= '{ "INDEX": "'+str(INDEX)+'", "TIMESTAMP": "'+TIMESTAMP+'", "CLASS": "'+CLASS+'", "DATA": '+DATA+', "PREVIOUSHASH": "'+PREVIOUSHASH+'", "HASH": "'+HashString+'"'
            print (jsonEnvio)
            PREVIOUSHASH=HASH
        i=1
    INDEX += 1
