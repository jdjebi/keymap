try:
	from .Errors import *
except ModuleNotFoundError:
	from Errors import *

import requests

class KeyRemoteClient:
	""" 
		Gestionnaire de la comminication avec un KeyRemote 

		Procédure de connexion
		----------------------
		1- Récupération des informations sur le serveur
		2- Etablissement de la connexion avec le serveur
		3- Communication client-serveur
	"""

	def __init__(self):
		self.protocol = 'P2CB' # Protocole de connexion 
		self.history = [] # Historique des requêtes
		self.remote_address = None # Element de l'adresse du serveur
		self.host = None # Hôte du serveur remote
		self.type = "public"

	def status(self):
		if self.remote_address != None:
			return True
		else:
			return False

	def connection(self,address=('127.0.0.1',5000)):
		""" Définie les éléments de de connexion au serveur remote """
		try:
			cible = "/test"
			host = "{}:{}".format(address[0],address[1]) # Hôte du serveur
			x = requests.get("http://"+host+cible)
		except requests.exceptions.ConnectionError:
			return ErrorCode.ConnectionError
		else:
			self.host = host
			self.remote_address = address
			return ErrorCode.ConnectionSuccess

	def deconnection(self):
		self.host = None
		self.remote_address = None
	
	def request(self,method="GET",cible="",data={},url_show=False):
		""" Methode d'envoye de requête """
		response = None

		if self.remote_address == None:
			return ErrorCode.RemoteAddressNotDefined, response
		else:
			http_adapter = "http://"
			http_request = "{}{}/{}".format(http_adapter,self.host,cible)
			
			error_code = ErrorCode.Success

			if url_show:
				print(http_request)

			self.history.append(http_request)

			try:
				if method == "GET":
					response = requests.get(http_request)
				elif method == "POST":
					response = requests.post(http_request,data=data)


			except requests.exceptions.ConnectionError as e:
				error_code = ErrorCode.ConnectionError

			if error_code != ErrorCode.ConnectionError and response.status_code != ErrorCode.Success:
				error_code = response.status_code

			return error_code, response

if __name__ == '__main__':
	client = KeyRemoteClient()

	status = client.connection()

	response_data = client.request(cible="infos")

	if response_data[0] == ErrorCode.Success:
		print(response_data[1].text)
	else:
		print("Impossiblde Récupérer les informations du serveur remote")
