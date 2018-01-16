import os

class Config(object):
	
	SECRET_KEY = "my_secret_token"
	PAGE_ACCES_TOKEN = 'EAANiA1kIY1gBAGRCZBwbszxN4LPN9ZCUbovcLu0wdZBZCbTIowJEnWzYrr8iEYsZBlcWeVMuaXBkMNZCNzyR990KBKZCyWUtECzxw5le4O6WSNMVwW78ccjKlq6NTLnRtSTdvz9IZCWoJnqORj495osJXgihh2IEltv8uQ3k7YM0SAZDZD'


class DevelopmentConfig(Config):
	DEGUB = True