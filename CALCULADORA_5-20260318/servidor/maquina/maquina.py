from servidor.operacoes.somar import Somar
from servidor.operacoes.dividir import Dividir
import cliente.interface
import servidor
import json
import socket
from servidor.processaCliente import ProcessaCliente


class Maquina:
	def __init__(self):
		self.sum = Somar()
		self.div = Dividir()
		self.s = socket.socket()
		self.s.bind(('', servidor.PORT))




	# def __init__(cliente.interface.Interface:object interface):
	# 	self.interface:object = interface
	# 	self.somar:object  = servidor.operacoes.somar.Somar()
	# 	self.dividir:object = servidor.operacoes.dividir.Dividir()
	# def exec():
	# 	res = self.interface.exec()
    # 		if res =="+":
    #     	s:object = somar.Somar(x,y)
    #     	res = s.executar(x,y)
    #     	interacao.resultado(res)
    #     print("O valor da operação somar é:", res)
    # elif res =="/":
    #     s:object = dividir.Dividir(x,y)
    #     res = s.executar()
    #     if type(res)==str:
    #         print (res)
    #     else:
    #         print("O valor da operação divisão é:",res)

	#def execute(self,command:str):
	def execute(self):
		self.s.listen(1)
		print("Waiting for clients on port " + str(servidor.PORT))
		while True:  # Loop infinito para múltiplos clients
			print("On accept...")
			connection, address = self.s.accept()
			print("Client", address, " connected")
			processa = ProcessaCliente(connection, address)
			processa.start()  # Arranca thread após ligação

#c = command.split()
		# Get the operator
	#	if c[0] =="+":
			#Call operator
	#		res = self.sum.execute(float(c[1]),float(c[2]))
	#	return res