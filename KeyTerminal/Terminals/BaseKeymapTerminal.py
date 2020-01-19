class BaseKeymapTerminal:
	""" Classe de base d'un terminal keymap """
	def __init__(self):
		self.name = None # Nom du terminal
		self.kmap = {} # Contient l'état de toutes les touches
		self.KeyPush = [] # Liste des codes des touches enfoncées

	""" 
	" Methodes
	"""
	def KeyTouch(self, code):
		""" Donne la valeur d'une touche enfoncée à la touche à laquelle correspond le code """
		pass

	def filter_kmap(self):
		""" Filtre la map de touche pour envoyer uniquement les touches préssées"""
		kmap_to_send = {}
		for key in self.kmap:
			if self.kmap[key] == 1:
				kmap_to_send[key] = 1
		return kmap_to_send

	def send_kmap(self,method=None):
		""" Envoye le les touches enfoncé au serveur selon la method précisée """
		pass


	"""
	" Methodes utilitaire
	"""
	def reset_kmap(self):
		""" Remet toutes les valeurs de la Keymap à 0 """
		for code in self.KeyPush:
			self.kmap[code] = 0
	
	def kmap(self):
		""" Affiche le contenu de la keymap """
		pass

	
	"""
	" Debug
	"""
	def show_kmap(self):
		for code in self.kmap:
			print(code,':',self.kmap[code])

	def debug(self):
		self.show_kmap()
		self.reset_kmap()
		self.show_kmap()

	def __repr__(self):
		return str(self.Keymap);

