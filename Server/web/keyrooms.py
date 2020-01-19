
from flask import render_template, url_for, redirect

#Done a 404 page

def view(filename):
		return "KeyRooms/" + filename + ".html"

class KeyRoomsHandler:
	def __init__(self):

		self.plateform_name = "KeyRooms"

		self.hub_data = {
			"jeux":{
				"name":"Jeux",
				"tag":"jeux",
				"ico":"videogame_asset",
				"apps":{
					"google_dino":{"tag":"google_dino","name":"Google Dino"}
				}
			},
			"presensation":{
				"name":"Présentation",
				"tag":"presensation",
				"ico":"picture_in_picture",
			 	"apps":{
			 		"ppt":{"tag":"ppt","name":"POWERPOINT"}
			 	}
			},
			"controleur":{
				"name":"Controleurs",
				"tag":"controleur",
				"ico":"mouse",
				"apps":{
					"mouse-pad":{"tag":"mouse-pad","name":"Souris"}				}
				}
		}

	def context(self):
		return dict(main_title=self.plateform_name, gl_data=self.hub_data.values())

	def check_mode(self,mode):
		if mode in self.hub_data.keys():
			return True
		return False
                  
	def get_modes(self):
		return self.hub_data.values()

	def get_modes_data(self, mode_tag):

		apps = self.hub_data[mode_tag]["apps"]

		if apps == None:
			apps = {}


		data = {
			"name":self.hub_data[mode_tag]["name"],
			"tag":mode_tag,
			"apps":apps.values()
		}
		return data

	"""
	" Views
	"""
	def joy(self):
		return render_template("KeyRooms/pads/joystick.html")
	
	def hub(self):
		data = self.get_modes()
		return render_template(view("hub"),data=data)

	def mode(self,mode_tag):
		if self.check_mode(mode_tag):
			data = self.get_modes_data(mode_tag)
			return render_template(view("mode"),mode=data)
		else:
			return "Mode {} non pris en charge.".format(mode_tag)

	def app(self,mode_tag, app_tag):
		if self.check_mode(mode_tag):
			if app_tag in self.hub_data[mode_tag]["apps"].keys():
				data = self.hub_data[mode_tag]["apps"][app_tag]
				return render_template(view("pads"),app=data)
			else:
				return "{} n'est pas pris en charge".format(app_tag) 
		else:
			return "Mode {} non pris en charge.".format(mode_tag)