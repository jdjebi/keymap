class Slot:
	def __init__(self,slot,ip,name,type,protocol):
		self.id = slot
		self.client_ip = ip
		self.client_protocol = protocol
		self.terminal_name = name
		self.terminal_type = type

	def __str__(self):
		return """Nom du terminal: {}\nip: {}\nprotocole: {}\nType: {}\nSlot: {}
		""".format(self.terminal_name,self.client_ip,self.client_protocol,self.terminal_type,self.id)
