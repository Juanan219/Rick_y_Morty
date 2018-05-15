from flask import Flask, render_template, url_for
import requests
app = Flask(__name__)

@app.route('/')
def enlaces():
	return render_template("enlaces.html")
@app.route('/personajes')
def personajes():
	r=requests.get('https://rickandmortyapi.com/api/character')
	if r.status_code == 200:
		doc = r.json()
		lista = []
		lista.append(doc["results"][0]["name"])
		for pag in range(2,int(doc["info"]["pages"])):
			payload = "page=%s" %(pag)
			re=requests.get('https://rickandmortyapi.com/api/character/?%s' %(payload))
			doc = re.json()
			lista.append(doc["results"][0]["name"])
	return render_template("personajes.html",lista1=lista)
if __name__ == '__main__':
	app.run(debug=True)