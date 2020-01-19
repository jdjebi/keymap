from flask import Flask, request, make_response, abort, redirect
#from StringIO import StringIO
from PIL import Image

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello():
	return """
		Methode: {}<br>
		Page de résumé du serveur: {}
	""".format(request.method,request.path)


@app.route('/404')
def response_():
	response = make_response("Yo erreur 404 !",404)
	return response


@app.errorhandler(404)
def page(error):
	return "Yosh encore un 404", 404

@app.route('/profil')
def profil():
	return redirect(url_for('hello'))


"""
@app.route('/image')
def gen_image():
	img = StringIO()

	Image.new("RGB",(300,300),"#92C41D").save(file,'BMP')

	return img.getvalue()
"""


if __name__ == '__main__':
	app.run(debug=True)