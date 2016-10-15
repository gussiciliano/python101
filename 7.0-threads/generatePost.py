import requests
from worker import Callback
from worker import Worker
import time



if __name__ == '__main__':
	
	callback = Callback()
	worker = Worker(callback)
	worker.start()
	
	while not callback.hasFinished():
		print(time.time())
		
	print(callback.getResult())
	
	
	
