from flask import Flask, request, session
import random

try:
	from .core.Slot.handler import SlotHandler
except ModuleNotFoundError:
	from core.Slot.handler import SlotHandler


"""
" Remote
"""
class KeyRemote(Flask):
	def __init__(self,name):
		super().__init__(name)
		self.remote_name = "KeyRemote-" + str(random.randint(1,10))
		self.type = "public"

		#Gestionnaire des connexions
		self.slotHandler = SlotHandler()

	def infos(self):
		""" Retourne les informations sur le serveur """
		return ';'.join([self.remote_name,self.type])

	def get_infos(self):
		""" Retourne le tableau contenant les infos sur le serveur """
		return [self.remote_name,self.type,]

	def terminal_is_already_connected(self,req):

		if req.remote_addr in self.slotHandler.slots_list.keys():
			return True

		return False

	def login(self,request):
		""" Procède à la connection """
		data = request.form.to_dict()
		data['ip'] = request.remote_addr
		# Création d'un nouveau slot
		return self.slotHandler.new_slot(data)

	"""
	" Routes
	"""
	def info(self):
		return self.infos()

	def test(self):
		return "Serveur OK !"

	def disconnect(self):
		ip = request.remote_addr

		if ip in self.slotHandler.slots_list.keys():
			del self.slotHandler.slots_list[ip]
		
		return ""