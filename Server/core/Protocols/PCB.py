import os
from flask import request

class PCB:
	def __init__(self,server):
		self.server = server

	def pcb_test(self):
		return "ok"

	def pcb_keytouch(self,special,touch):

		if special == "special":
			os.system("AutoIt3 /AutoIt3ExecuteLine Send('{"+touch+"}')")
		elif special == None :
			os.system("AutoIt3 /AutoIt3ExecuteLine Send('"+touch+"')")

		return ''

	def pcb_mouse(self,action):
		mouse_data = request.form.to_dict()

		print(mouse_data['dx'], mouse_data['dy'])
		return ''
