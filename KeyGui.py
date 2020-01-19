from tkinter import *
from tkinter import ttk

class Win(Tk):
	WIN_WIDTH = 500
	WIN_HEIGHT = 400
	WIN_SIZE = '{}x{}'.format(WIN_WIDTH,WIN_HEIGHT)
	WIN_TITLE = 'Keymap - Remote'

	def __init__(self):
		super().__init__()
		self.WinInit()
		self.init_ui()

	def WinInit(self):
		self.title(self.WIN_TITLE)
		self.geometry(self.WIN_SIZE)
		self.center_win()

	def center_win(self):
		ws = self.winfo_screenwidth()
		hs = self.winfo_screenheight()
		x = int((ws/2) - (self.WIN_WIDTH/2))
		y = int((hs/2) - (self.WIN_HEIGHT/2))
		self.geometry('{win_dim}+{x0}+{y0}'.format(win_dim=self.WIN_SIZE,x0=x,y0=y))

	def init_ui(self):

		style_main_frame_bg = 'gray26'

		# Frame principale
		main_frame = Frame(self,bg=style_main_frame_bg)
		main_frame.pack(fill=BOTH,expand=True)


		# Frame Centrale
		center_frame = Frame(main_frame,bg="white")
		center_frame.pack(fill=BOTH,expand=1)

		kmap_style = {
			#'fg':'white',
			'bg':'white',
			#'height':300
		}

		t = Label(center_frame,kmap_style,text="Keymap",font=('Arial',33))

		#t.config(state='disabled')

		t.pack()


		# Frame de pieds
		style_footer_frame = {
			#'bg':"gray88",
			#'highlightbackground':"black",
			#'highlightthickness': 1,
			'height':80
		}
		footer_frame = Frame(main_frame,style_footer_frame)
		footer_frame.pack(fill=X,side=BOTTOM)


		# Frame du bouton de control du serveur
		control_server_frame = Frame(footer_frame,bg="gray88",height=80,padx=10,pady=10)
		control_server_frame.pack(side=LEFT)


		# Bouton de démarrage et d'arrêt du serveur
		btn_start_server = ttk.Button(control_server_frame,text="Démarrer", style="BW.TButton")
		btn_start_server.pack()



def main():
	app = Win()
	app.mainloop()

if __name__ == "__main__":
	main()