""" Script du serveur KeyRemote v1"""

from flask import request

from Server.server import KeyRemote
from KeyTerminal.Terminals.Remote.Errors import ErrorCode 
from Server.Protocols import P2CB, PCB

server = KeyRemote(__name__)

""" Protocoles """
p2cb = P2CB.P2CB(server)
pcb = PCB.PCB(server)

""" Routes de base """
server.route('/infos')(server.infos)
server.route('/test')(server.test)
server.route('/disconnect')(server.disconnect)

""" P2CB """
server.route('/P2CB/connect',methods=['POST'])(p2cb.P2CB_login)
server.route('/P2CB/run_kmap/slot/<int:slot>',methods=['POST'])(p2cb.P2CB_run_kmap)

""" PCB """
server.route("/PCB/test")(pcb.pcb_test)
server.route("/PCB/keytouch")(pcb.pcb_keytouch)

if __name__ == '__main__':
	server.secret_key = "yosh"
	server.run(host='0.0.0.0',debug=False)