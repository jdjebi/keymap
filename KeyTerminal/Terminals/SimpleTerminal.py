try:
	from .BaseKeymapTerminal import BaseKeymapTerminal
	from .Remote import P2CB
	from .Remote.Errors import *

except ModuleNotFoundError:
	from BaseKeymapTerminal import BaseKeymapTerminal
	from Remote import P2CB
	from Remote.Errors import *

# Empecher plusieurs connexions
# Vérifier la nature de la reponse

class SimpleTerminal(BaseKeymapTerminal):
	""" 
		Terminal des touches directionnelles: HAUT, BAS, GAUCHE, DROITE.
		Règles:
		Une seule touches peut-être enfoncée à la fois.
	"""

	""" Constantes """
	K_UP = "UP"
	K_DOWN = "DOWN"
	K_LEFT = "LEFT"
	K_RIGHT = "RIGHT"

	kmap = {
		K_UP: 0,
		K_DOWN: 0,
		K_LEFT: 0,
		K_RIGHT: 0
	}

	def __init__(self):
		super().__init__()

		#Initialisation du terminal
		self.name = "SimTermios"
		self.type = "SimpleTerminal"
		self.kmap = SimpleTerminal.kmap
		self.slot = None
		self.init()

	def init(self):
		self.kclient = P2CB.KeyRemoteClient() # Client du serveur remote²

		# Information sur le serveur remote
		self.remoteInfo = {
			"name": None,
			"type": None,
		}


	def remoteConnect(self,ip='127.0.0.1',port=5000):

		status_code = self.kclient.connection((ip,port))

		if status_code == ErrorCode.ConnectionSuccess:
			response = self.kclient.request(cible="infos")[1]
			data = response.text.split(";")

			if data[1] != self.kclient.type:
				return ErrorCode.ClientTypeError
			else:
				# Réception des infos du serveur
				self.remoteInfo["name"]	= data[0]
				self.remoteInfo["type"]	= data[1]

				#Création de la session
				post = {
					"name": self.name,
					"type":self.type,
					"protocol":self.kclient.protocol				}

				# Envoye de la requête
				error_code, response = self.kclient.request('POST','P2CB/connect',post)

				# Gestion des codes d'erreurs
				if response.text  == str(ErrorCode.ConnectionAlreadyStart):
					return ErrorCode.ConnectionAlreadyStart

				elif error_code != ErrorCode.Success:
					return ErrorCode.ConnectionError

				else:
					if response.text == ErrorCode.ConnectionError:
						return ErrorCode.ConnectionError

					elif response.text == ErrorCode.ConnectionAlreadyStart:
						return ErrorCode.ConnectionAlreadyStart

					else:
						self.slot = response.text

		return status_code

	def KeyTouch(self,code):
		if not code in self.kmap.keys():
			print("Le terminal ne possède aucune touche dont le code est '{}'.".format(code))
			print("Codes disponibles",",".join(self.kmap.keys()))
		else:
			self.kmap[code] = 1
			self.KeyPush.append(code)

	def send_kmap(self,method="POST"):
		if method not in ["POST","GET"]:
			print("Méthode {} non reconnue.(POST|GET)".format(method))
		else:
			kmap_to_send = self.filter_kmap()

			cible = self.kclient.protocol + "/run_kmap/slot/" + self.slot

			status, response = self.kclient.request("POST",cible,kmap_to_send)

			self.reset_kmap()

			return status, response

		

if __name__ == "__main__":
	terminal = SimpleTerminal()
	
	status = terminal.remoteConnect()

	#Test de connexion
	""" 
	if status == ErrorCode.ConnectionSuccess:
		print("Terminal:",terminal.name)
		print("Type",terminal.type)
		print("Connecté au remote:",terminal.remoteInfo["name"])
		print("Type de connexion:",terminal.remoteInfo["type"])
		print("Slot:",terminal.slot)
		print("Id: {}@{}:slot{}".format(terminal.name,terminal.remoteInfo["name"],terminal.slot))

	elif status == ErrorCode.ClientTypeError:
		ErrorHandler.decode(ErrorCode.ClientTypeError)

	else:
		ErrorHandler.decode(status)
	"""

	#Test d'envoye
	if status == ErrorCode.ConnectionSuccess:
		terminal.KeyTouch("RIGHT")
		status, reponse = terminal.send_kmap()

		if status == ErrorCode.Success:
			print("Touches envoyée.")
		else:
			print("Touches non envoyé. Code d'erreur:",status)
	else:
		ErrorHandler.decode(status)