import pyrebase 
from flask import Flask 
#mport firebase_admin
#from firebase_admin import credentials
#from firebase_admin import db
#from firebase_admin import firestore

app = Flask(__name__)
firebase = firebase.post('https://pseudogram-3d35e.firebaseio.com/')
result = firebase.post('/Usuario', None)
print(result)

#ced = credentials.Certificate('')
#firebase_admin.initialize_app(cred)

#db = firestore.client()

#carpeta = db.collection(u'Usuarios')
#nombre1 = carpeta.get()

#for n in nombre1:
 #   print(u'{}:{}'.format(n.id,n.to_dict()))


@app.route('/')
def index():
	#return"<h1><center>SPACE APP</center></h2><h2>SUPERFICIE</h2>"
	return result

@app.route('/Articulo')
def Rl():
	return result



#config={
	#"apiKey": "AIzaSyBWg0bxZHvBgVAtE0tCxRFKhf7kl6TxF-I",
    #"authDomain": "pseudogram-3d35e.firebaseapp.com",
    #"databaseURL": "https://pseudogram-3d35e.firebaseio.com",
    #"projectId": "pseudogram-3d35e",
    #"storageBucket": "pseudogram-3d35e.appspot.com",
    #"messagingSenderId": "905498695592"
#}


#firebase = pyrebase.initialize_app(config)

#auth = firebase.auth()



if __name__ == '__main__':
	app.run('0.0.0.0', 5012, debug=True)






