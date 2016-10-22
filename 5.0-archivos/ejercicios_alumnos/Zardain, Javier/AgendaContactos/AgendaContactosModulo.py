'''
Created on Sep 10, 2016

@author: python
'''
import Contacto
import Email
import datetime
import pickle
import os

def listarContacto(contacto):
    print("------------")
    print("Nombre: " + contacto.nombre)
    print("Apellido: " + contacto.apellido)
    print("DNI: " + str(contacto.dni))
    print("------------")

def age(fechaNacimiento):
    diff = datetime.date.today() - datetime.date(int(fechaNacimiento.split("-")[2]),int(fechaNacimiento.split("-")[1]),int(fechaNacimiento.split("-")[0]))
    years = str(diff/365).split(' ')[0]
    return years

class AgendaContactos:
    def __init__(self):
        self.listaContactos = []
        try:
            with open('agenda.pkl', 'rb') as input:
                self.listaContactos = pickle.load(input)
        except Exception as ex:
            print(ex)
    def agregarContacto(self):
        contacto = Contacto.recoleccionDeDatos()
        self.listaContactos.append(contacto)
        self.persistirListaContactos()
    def addContact(self, contacto):
        self.listaContactos.append(contacto)
        self.persistirListaContactos()
    def borrarContacto(self):
        email = input("Ingrese el email del contacto a borrar: ")
        for contacto in filter(lambda x: x.email == email,self.listaContactos):
            self.listaContactos.remove(contacto)
            self.persistirListaContactos()
    def editarContacto(self):
        email = input("Ingrese el email del contacto a editar: ")
        for contactoAux in filter(lambda x:x.email == email,self.listaContactos):
            listarContacto(contactoAux)
            self.listaContactos[contactoAux] = Contacto.recoleccionDeDatos()
            self.persistirListaContactos()
    def mostrarContactos(self):
        for contacto in self.listaContactos:
            listarContacto(contacto)
    def mostrarContactosDespuesDe(self):
        fecha = input("Ingrese el year para filtrar: ")
        for contacto in filter(lambda x: int(x.fechaNacimiento.split("-")[2]) >= int(fecha), self.listaContactos):  
            listarContacto(contacto)
    def buscarPorIniciales(self):
        nombre = input("Ingrese iniciales del nombre: ")
        apellido = input("Ingrese iniciales del apellido: ")
        for contacto in filter(lambda x:x.nombre[0:1].lower() == nombre.lower() and x.apellido[0:1].lower() == apellido.lower(),self.listaContactos):              
            listarContacto(contacto)
    def enviarMail(self):
        Email.Email.enviarMails(self.listaContactos)
    def enviarMailsDespuesDe(self):
        Email.Email.enviarMails(filter(lambda x: int(x.fechaNacimiento.split("-")[2]) >= 1993), self.listaContactos)
    def edadDespuesDe10(self):
        for contacto in [x.nombre + " " + x.apellido + " " + str(int(age(x.fechaNacimiento))+10) for x in self.listaContactos]:              
            print(contacto)
    def cargarDeArchivoTxt(self):
        try:
            path = os.path.join(os.getcwd(),"archivo.txt")
            with open(path,"r") as file:
                contactos = file.read().split(";")
                if(len(contactos)> 0):
                    if(input("Se han hallado contactos en el archivo, desea agregarlos a la agenda? s/n: ") == 's'):
                        for contacto in contactos:
                            contact = contacto.split(",")
                            print(contact)
                            if(len(contact) > 1):
                                self.addContact(Contacto.Contacto(contact[0],contact[1],contact[2],contact[3],contact[4],contact[5],contact[6]))
        except Exception as ex:
            print("No se ha podido cargar un archivo de texto con contactos")
            print(ex)
    def persistirListaContactos(self):
        try:
            with open('agenda.pkl', 'wb') as output:
                pickle.dump(self.listaContactos, output, pickle.HIGHEST_PROTOCOL)
        except Exception as ex:
            print(ex)