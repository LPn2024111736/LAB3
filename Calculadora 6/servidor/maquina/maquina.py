import servidor
import socket
from servidor.processaCliente import ProcessaCliente
from dados.dados import Dados

class Maquina:
	def __init__(self):
		self.s = socket.socket()
		self.dados = Dados()
		self.s.bind(('', servidor.PORT))

	def execute(self):
		self.s.listen(1)
		print("Waiting for clients on port " + str(servidor.PORT))
		while True:  # Loop infinito para múltiplos clients
			print("On accept...")
			connection, address = self.s.accept()
			print("Client", address, " connected")
			processo_cliente = ProcessaCliente(connection, address, self.dados)
			processo_cliente.start()
