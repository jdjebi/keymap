import requests
import os

# http://jetic2019.mi/

data = {
	"terminal":"SimpleDirectionalTerminal",
	"message":"yes it's me"
}

data = {
	"RIGHT":"1",
	"UP":"2"
}
host = "http://127.0.0.1:5000"

req = requests.Session()


for i in range(0, 2):
	r = req.get(host)

	print(r)
	print(r.content)
	print(r.headers);
	print(r.status_code);

	#with open("response.html","w") as response:
		#response.write(r.text)

#os.system("start response.html")