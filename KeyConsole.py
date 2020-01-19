""" Teste l'envoie des touches à un serveur """
#version 0
import os
from KeyTerminal.Terminals import *
from KeyTerminal.Terminals.Remote.Errors import ErrorCode, ErrorHandler

class KeyConsole:
	def __init__(self):
		self.run_ = True
		self.terminal = None

		self.terminals = {
			"simple": SimpleTerminal
		}

		self.command = {
			"use": (1,self.use),
			"unuse":(0,self.unuse),
			"post": (1,self.post),
			"exit": (0, self.exit),
			"cls": (0,self.cls),
			"test": (0,self.testRemote),
			"history": (0, self.history),
			"lconnect": (0, self.local_connect)
		}

	def run(self):
		return self.run_

	def shell(self):
		print('KeyConsole')
		while self.run():
			cmd = self.prompt()
			self.execute(cmd)
			print("\n")

	def prompt(self):

		indicator = ''

		if self.terminal != None:
			indicator += ':{}'.format(self.terminal.name)

			if self.terminal.slot != None:
				indicator += '@{}:slot{}'.format(self.terminal.remoteInfo["name"],self.terminal.slot)

		expression = '$'+ indicator +'>' 

		return input(expression)

	def execute(self,cmd):
		partials = cmd.split()

		try:
			action = partials[0]

			if action in self.command.keys():
				params = partials[1:]
				cmd_data = self.command[action]

				if cmd_data[0] == len(params):
					cmd_data[1](*params)
				else:
					print("Nombre de paramètre incorrecte. {} paramètre réquis.".format(cmd_data[0]))
			else:
				print("Commande inconnue.")
		except IndexError:
			pass
		except TypeError:
			print("Cette commande n'a pas été définie.")

	"""
	" Commandes
	"""
	def exit(self):
		self.run_ = False

	def cls(self):
		os.system("cls")

	def unuse(self):
		self.terminal = None
		print("Déconnexion non éffectuée.")

	def use(self,terminal_name):
		try:
			termios = self.terminals[terminal_name]()
			self.terminal = termios
		except KeyError:
			print("Terminal {} inconnue.".format(terminal_name))

	def history(self):
		if self.terminal == None:
			print("Aucun terminal utilisé.")
		else:
			for entry in self.terminal.remote.history:
				print(entry)

	def post(self,touch):
		if self.terminal == None:			
			print("Aucun terminal utilisé.")
		
		elif self.terminal.slot == None:
			print("Envoie impossible.Le terminal n'est pas connecté un a serveur KeyRemote.")
		
		else:
			self.terminal.KeyTouch(touch)
			status, response = self.terminal.send_kmap("POST")

			if status == ErrorCode.Success:
				print("Touche envoyée")
			else:
				ErrorHandler.decode(status)


	def local_connect(self):
		if self.terminal == None:
			print("Aucun terminal utilisé.")
		else:
			status = self.terminal.remoteConnect()

			if status == ErrorCode.ConnectionSuccess:
				print("Connexion réussie.")
				
			elif status == ErrorCode.ConnectionAlreadyStart:
				
				if self.terminal.slot != None:
					print("Terminal déjà connecté.")

				elif self.terminal.slot == None:
					status, response = self.terminal.kclient.request("GET","disconnect")
					if status == ErrorCode.Success:
						print("Paramètre de connexion invalide. Veuiller réesayer.")
					else:
						ErrorHandler.decode(status)

			else:
				print("Connexion impossible.")
				print("Code d'erreur:",status)

	def connect(self):
		if self.terminal == None:
			print("Aucun terminal utilisé.")
		else:
			print("Connection2")

	def testRemote(self):
		if self.terminal == None:
			print("Aucun terminal utilisé.")
		else:
			data = self.terminal.remote.request()

			err_code = data[0]

			if err_code == ErrorCode.RemoteAddressNotDefined:
				print("Le terminal n'est connecté à aucun serveur remote.")
			elif err_code != ErrorCode.Success:
				print("Impossible de récupérer les informations du serveur remote")
			elif err_code == ErrorCode.Success:
				print("Information du serveur récupéré")
				response = data[1]
				print(response.text)
			else:
				print("Une érreur inconnue est c'est produite")
				

if __name__ == '__main__':
	KeyConsole().shell()