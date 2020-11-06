def lectura():
	fichero = open('pass.txt', 'r') # read
	fichero = fichero.read()
	print(fichero)

def escritura():
	fichero = open('pass.txt', 'w') # escritura
	fichero.write('esta es la contraseña')
	fichero.close
def main():
	lectura()
	escritura()

main()