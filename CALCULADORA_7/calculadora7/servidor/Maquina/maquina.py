from servidor.Maquina.lista_clientes import ListaClientes
from servidor.operacoes.somar import Somar
from servidor.operacoes.dividir import Dividir
from  servidor.operacoes.subtrair import  Subtrair
import socket
import servidor
from servidor.Maquina.processaCliente import ProcessaCliente
from dados.dados import Dados
from servidor.Maquina.broadast_emissor  import ThreadBroadastEmissor




class Maquina:
	def __init__(self):
		self.broadcast = None
		self.s = socket.socket()
		self.dados = Dados()
		self.s.bind(('', servidor.PORT))
		self.clientes= ListaClientes()




	# def __init__(cliente.interface.Interface:object interface):
	# 	self.interface:object = interfac
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
		self.broadcast = ThreadBroadastEmissor(self.clientes, self.dados, intervalo=5)
		self.broadcast.start()
		while True:  # Loop infinito para múltiplos clients
			print("On accept...")
			connection, address = self.s.accept()
			self.clientes.connetar([connection,address])
			print("Client", address, " connected")
			processo_cliente = ProcessaCliente(connection, address, self.dados,self.clientes)
			processo_cliente.start()

			