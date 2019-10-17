import csv
import json
import hashlib

INDEX=0
TIMESTAMP=''
CLASS=''
DATA=''
PREVIOUSHASH='0000'
HASH=''
jsonEnvio =''

with open('E:\\Back Up Charles\\Davis\\Usac\\Semestre 6\\Estructuras\\Practica 2\\ejemplo.csv') as f:
    reader = csv.reader(f)
    i = 0
    for row in reader:
        if(i==0):
            CLASS = row[1]
        if(i==1):
            TIMESTAMP=''
            DATA = row[1]
            if(INDEX==0):
                PREVIOUSHASH='0000'
            bs = bytes(DATA, 'utf-8')
            HASH=hashlib.new('sha256',bs)
            HashString = HASH.hexdigest()
            jsonEnvio= '{ "INDEX": '+str(INDEX)+', "TIMESTAMP": '+TIMESTAMP+', "CLASS": '+CLASS+', "DATA": '+DATA+', "PREVIOUSHASH": '+PREVIOUSHASH+', "HASH": '+HashString
            print (jsonEnvio)
            PREVIOUSHASH=HASH
        i=1
    INDEX += 1
