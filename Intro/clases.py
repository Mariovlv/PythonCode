class coches:
	marca = 'Bugatti'
	modelo = 'Chiron'
	numero_km = 1
	velocidad = 0
	arrancado = True

def arrancar(self):
	if not self.arrancado:
		print('Arrancando...')
		self.arrancado = True
	else:
		print('Ya está encendido')

def marca(self):
	print(self.marca)

def main(self):
	arrancar(coche)
	marca(coche)	


coche = coches()
main(coche)
