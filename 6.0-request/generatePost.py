import requests
import time
from model import UserModel



if __name__ == '__main__':
	user = UserModel("nombre", "nombre@apellido.com")
	now = time.time()
	r = requests.post(url='http://localhost:8000/users/', data = user.getUserDictionary(), auth = ("XXX","XXX"))
	after = time.time()
	print(r.status_code, " Tardo...", after-now)
