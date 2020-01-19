""" Script du serveur KeyRemote v1"""
import sys

from flask import request

from Server.server import KeyRemote
from Server.web.keyrooms import KeyRoomsHandler
from Server.core.Protocols import P2CB, PCB

server = KeyRemote(__name__)
pcb = PCB.PCB(server)

KeyRooms = KeyRoomsHandler()

""" server remote """

#Clavier
server.route("/PCB/keytouch/<string:touch>/",defaults={'special':None})(pcb.pcb_keytouch)
server.route("/PCB/keytouch/<string:special>/<string:touch>/")(pcb.pcb_keytouch)


#Sourie
server.route("/PCB/mouse/<string:action>/",methods=['GET','POST'])(pcb.pcb_mouse)

""" Interfaces web """
server.context_processor(KeyRooms.context)
server.route("/")(KeyRooms.hub)

server.route("/joy")(KeyRooms.joy)
server.route("/<string:mode_tag>/")(KeyRooms.mode)
server.route("/<string:mode_tag>/<string:app_tag>/")(KeyRooms.app)


if __name__ == '__main__':
	server.secret_key = "yosh"
	server.run(host='0.0.0.0',debug=False)
	print(sys.path)