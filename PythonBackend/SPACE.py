from flask import Flask 

app = Flask(__name__)
def hello():
	return "lr"

if __name__ == "__main__":
	app.run()
