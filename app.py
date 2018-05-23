import os
from flask import Flask, render_template, url_for
import requests
from random import randint

app = Flask(__name__)
@app.route('/')
def enlaces():
	aleatorio = []
	url = []
	personaje = []
	nombreid = []
	nombre_id = []
	frases = ["Lamento decirlo, pero lo que la gente llama 'amor' es sólo una reacción química que motiva a los animales a aparearse. Es un golpe duro, y lentamente se desvanece dejándote varado en un matrimonio fallido. Yo lo hice. Tus padres lo harán. Rompe el ciclo. Álzate por encima. Enfócate en la ciencia.	-Rick Sanchez-", "A veces la ciencia es más arte que ciencia. Mucha gente no lo entiende. -Rick Sanchez-", "Científicamente hablando, las tradiciones son estúpidas", "Las bodas son básicamente funerales con pastel. Si quisiera ver a alguien desperdiciar su vida, me pasaría todo el día con Jerry. -Rick Sanchez-", "No existe Dios, Summer. Tuve que arrancar esa tirita ahora. Me lo agradecerás después. -Rick Sanchez-", "¡Wubba lubba dub dub! (Estoy sufriendo, por favor ayúdenme) -Rick Sanchez-"]
	aleatorio2 = str(randint(0,len(frases)-1))
	
	for a in range(1,4):
		aleatorio.append(randint(1,461))
	for b in aleatorio:
		r = requests.get("https://rickandmortyapi.com/api/character/%s"%(b))
		if r.status_code == 200:
			doc = r.json()
			personaje.append(doc)
	return render_template("enlaces.html",doc=personaje,frase=frases,aleatorio=aleatorio2)

@app.route('/personajes')
def personajes():
	nombreid = []
	nombre_id = []

	r=requests.get('https://rickandmortyapi.com/api/character')
	if r.status_code == 200:
		doc = r.json()
		for pag in range(1,doc["info"]["pages"]+1):
			payload = "?page=%s" %(pag)
			r=requests.get('https://rickandmortyapi.com/api/character/%s'%(payload))
			if r.status_code == 200:
				doc = r.json()
				for pers in doc["results"]:
					nombreid.append(pers["name"])
					nombreid.append(pers["id"])
					nombre_id.append(nombreid)
					nombreid = []
	return render_template("personajes.html",nombre_id_2=nombre_id)

@app.route('/personajes/<id>')
def personaje_individual(id):
	episodios = []
	epi_id = []
	nomid = []
	nom_id = []
	r = requests.get('https://rickandmortyapi.com/api/character/%s'%(id))
	if r.status_code == 200:
		doc = r.json()
		for ep in doc["episode"]:
			epi = requests.get(ep)
			epidoc = epi.json()
			episodios.append(epidoc["name"])
			episodios.append(epidoc["id"])
			epi_id.append(episodios)
			episodios = []
		for lug in doc["location"]:
			r = requests.get(doc["location"]["url"])
			doc2 = r.json()
			if doc2["name"] not in nomid:
				nomid.append(doc2["name"])
			if doc2["id"] not in nomid:
				nomid.append(doc2["id"])
			if nomid not in nom_id:
				nom_id.append(nomid)
				nomid = []
				

	return render_template("personaje_individual.html",datos=doc,nomepi=epi_id,lugid=nom_id)

@app.route('/lugares')
def lugares():
	nombre_id = []
	nombreid = []
	
	r = requests.get('https://rickandmortyapi.com/api/location')
	if r.status_code == 200:
		doc = r.json()
		for pag in range(1,doc["info"]["pages"]+1):
			payload = "?page=%s"%(pag)
			r = requests.get('https://rickandmortyapi.com/api/location%s'%(payload))
			if r.status_code == 200:
				doc = r.json()
				for nomid in doc["results"]:
					if nomid["name"] not in nombreid:
						nombreid.append(nomid["name"])
						nombreid.append(nomid["id"])
						nombre_id.append(nombreid)
						nombreid = []

	return render_template("lugares.html",nomid=nombre_id)

@app.route('/lugares/<id>')
def lugar_individual(id):
	personajeurl = []
	personaje_url = []
	r = requests.get('https://rickandmortyapi.com/api/location/%s'%(id))
	if r.status_code == 200:
		doc = r.json()
		for per in doc["residents"]:
			req = requests.get(per)
			perid = req.json()
			personajeurl.append(perid["name"])
			personajeurl.append(perid["id"])
			personaje_url.append(personajeurl)
			personajeurl = []
	return render_template("lugar_individual.html",datos=doc,perid=personaje_url)

@app.route('/episodios')
def episodios():
	nombreid = []
	nombre_id = []
	
	r = requests.get('https://rickandmortyapi.com/api/episode/')
	if r.status_code == 200:
		doc = r.json()
		for pag in range(1,doc["info"]["pages"]+1):
			payload = "?page=%s"%(pag)
			r = requests.get('https://rickandmortyapi.com/api/episode%s'%(payload))
			if r.status_code == 200:
				doc = r.json()
				for cap in doc["results"]:
					nombreid.append(cap["name"])
					nombreid.append(cap["id"])
					nombre_id.append(nombreid)
					nombreid = []
	return render_template("episodios.html",nombre_id=nombre_id)

@app.route('/episodios/<id>')
def episodio_individual(id):
	episodiourl = []
	episodio_url = []
	r = requests.get('https://rickandmortyapi.com/api/episode/%s'%(id))
	if r.status_code == 200:
		doc = r.json()
		for epi in doc["characters"]:
			req = requests.get(epi)
			epid = req.json()
			episodiourl.append(epid["name"])
			episodiourl.append(epid["id"])
			episodio_url.append(episodiourl)
			episodiourl = []
	return render_template("episodio_individual.html",datos=doc,epiurl=episodio_url)

if __name__ == '__main__':
	port=os.environ["PORT"]
	app.run('0.0.0.0',int(port), debug=True)