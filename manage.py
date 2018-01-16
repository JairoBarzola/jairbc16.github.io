from flask import Flask
from config import DevelopmentConfig
from flask import request

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)


@app.route('/webhook', methods = ['GET'])
def webhook():
	verify_token= request.args.get('hub.verify_token','')
	if verify_token == app.config['SECRET_KEY']:
		return request.args.get('hub.challenge')
	return 'Error al validar el secret token'

@app.route('/', methods = ['GET'])
def index():
	return 'Bienvenido al curso de creacion de un Bot!'
 
if __name__ == '__main__':
	app.run( debug= True, port = 8000)