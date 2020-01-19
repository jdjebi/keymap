from flask import request
from KeyTerminal.Terminals.Remote.Errors import ErrorCode 

""" P2CB: Protocole Public de Connexion Basique."""

"""
	*Pour se connecter au serveur le client envoye 3 informations:
	-Nom du terminal
	-Type du terminal
	-Le nom du protocole utilisé
	-slot utilisé
"""

class P2CB:
	""" Classe vérifiant que les interactions entre le client et serveur respecte le protocole P2CB """
	def __init__(self,server):
		self.server = server
		self.type = "public"
		self.P2CB_required_data = ['name','type','protocol']

	def check_data_integrity(self,form):
		""" Vérifcation des informations """
		data = form.to_dict()

		for key in data.keys():
			if not key in self.P2CB_required_data:
				return False

		return True	

	def P2CB_login(self):
		post_data = request.form
		if not self.server.terminal_is_already_connected(request):
			if not self.check_data_integrity(post_data):
				return str(ErrorCode.ConnectionError)
			else:
				return self.server.login(request)
		else:
			return str(ErrorCode.ConnectionAlreadyStart)

	def P2CB_run_kmap(self,slot):
		return "Oh yes !"