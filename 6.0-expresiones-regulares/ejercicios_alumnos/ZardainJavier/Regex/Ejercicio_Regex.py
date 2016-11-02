'''
Created on 21/10/2016

@author: javier_zardain
'''
import os
import re
import urllib2
import pickle



with open(os.path.join(os.getcwd(), "texto.txt")) as file:
    texto = file.read()

opcion = int(input("Ingrese el numero de ejercicio: "))

if(opcion == 1):
    print(re.findall("(abcdefg|abcde|abc)", texto))
elif(opcion == 2):
    print(re.findall('(abc123xyz|define "123"|var g = 123;)', texto))
elif(opcion == 3):
    print(re.findall('(cat.|896.|\\?\\=\\+.)', texto))
elif(opcion == 4):
    print(re.findall('([^d|p|r]an)', texto))
elif(opcion == 5):
    print(re.findall('([A|B|C].[a|b|c])', texto))
elif(opcion == 6):
    print(re.findall('(wa[z]{3,5}up)', texto))
elif(opcion == 7):
    print(re.findall('([a]{2,4}[b]{0,4}[c]{1,2})', texto))
elif(opcion == 8):
    print(re.findall('([\d]?\d file[s]? found\\?)', texto))
elif(opcion == 9):
    print(re.findall('([1,2,3]\\.[\s]*abc[\s]*)', texto))
elif(opcion == 10):
    print(re.findall('(Mission: successful)', texto))
elif(opcion == 11):
    print(re.findall('(file.*\\.pdf[^\\.tmp])', texto))
elif(opcion == 12):
    with open(os.path.join(os.getcwd(), "telefonos.txt")) as file:
        telefonos = file.read()
    telefonosLimpios = re.findall('114[\d]{7}', telefonos)
    print(telefonosLimpios)
    with open(os.path.join(os.getcwd(), "telefonos-limpio.txt"), "w") as file:
        file.write(str(telefonosLimpios))
    with open('telefonos.pkl', 'wb') as output:
        pickle.dump(telefonosLimpios, output, pickle.HIGHEST_PROTOCOL)
elif(opcion == 13):
    page = urllib2.urlopen('http://free-email-database.blogspot.com.ar/2008/12/welcome-to-free-e-mail-database.html')
    emails = page.read()
    emailsLimpios = re.findall('.{1,20}@.{1,20}\\..{1,5}', emails)
    print(emailsLimpios)
elif(opcion == 14):
    page = urllib2.urlopen('http://money.cnn.com/data/markets/')
    dinero = page.read()
    dineroSucio = re.findall('\\$[\d]{1,10}.[\d]{1,10}', dinero)
    print(dineroSucio)
    with open(os.path.join(os.getcwd(), "dinero-sucio.txt"), "w") as file:
        file.write(str(dineroSucio))
    with open('dinero.pkl', 'wb') as output:
        pickle.dump(dineroSucio, output, pickle.HIGHEST_PROTOCOL)