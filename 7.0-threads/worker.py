from threading import Thread
from model import UserModel
import time
import requests

class Worker(Thread):
	
	def __init__(self, callback = None):
		Thread.__init__(self)
		self.__callback = callback
	
	def run(self):
		print("working ...")
		user = UserModel("nombre", "nombre@apellido.com")
		r = requests.post(url='http://localhost:8000/users/', data = user.getUserDictionary(), auth = ("zehemz","isveckson"))	
		self.__callback.threadFinished(r)
		print("Termine! ...")
		
class Callback:
	
	def __init__(self):
		self.__status = False
		self.result = None
	
	def threadFinished(self, result = None):
		self.__result = result
		self.__status = True
	
	def hasFinished(self):
		return self.__status
	
	def getResult(self):
		return self.__result