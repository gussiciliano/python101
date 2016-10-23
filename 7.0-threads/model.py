#!/usr/bin/python
class UserModel:
	def __init__(self, username, email):
		self.username = username
		self.email = email
		self.groups = []

	def getUserDictionary(self):
		return {"username" : self.username, "email": self.email, "groups": self.groups} 
