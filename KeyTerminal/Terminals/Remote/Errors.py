class ErrorCode:
	Success = 200 # Requête réussie
	ConnectionSuccess = 201 # Connexion au serveur remote réussie
	ConnectionAlreadyStart = 302 # Connexion au serveur déjà établie

	PageNotFound = 404 # La page demandée est introuvable
	ConnectionError = 501 # Connexion au serveur réfusée
	RemoteAddressNotDefined = 502 # Adresse du serveur remote non définie	
	ClientTypeError = 503 # Le client ne supporte ce type de de connexion


class ErrorHandler:
	""" Gestionnaire des erreurs """

	errors = {
		ErrorCode.Success: "Requête réussie.",
		ErrorCode.PageNotFound: "Page introuvable.",
		ErrorCode.RemoteAddressNotDefined: "Adresse du serveur remote non définie.",
		ErrorCode.ConnectionError: "Connexion au serveur impossible.",
		ErrorCode.ConnectionSuccess: "Connexion au serveur réussie.",
		ErrorCode.ConnectionAlreadyStart:"Connexion au serveur déjà établie.",
		ErrorCode.ClientTypeError: "Incompatibilé de type entre le client Remote et serveur Remote."
	}

	@classmethod
	def decode(self, code):
		try:
			print(ErrorHandler.errors[code])
		except KeyError:
			print("Code d'erreur {} inconnu".format(code))

	@classmethod
	def error(self):
		try:
			return ErrorHandler.errors[code]
		except KeyError:
			print("Code d'erreur {} inconnu".format(code))