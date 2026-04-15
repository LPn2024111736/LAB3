import threading
from servidor.operacoes import somar, subtrair, dividir
import servidor
import json
class ProcessaCliente(threading.Thread):
    def __init__(self, connection, address,dados,clientes):
        super().__init__()
        self.connection = connection
        self.address = address
        self.sum = somar.Somar()
        self.sub = subtrair.Subtrair()
        self.div = dividir.Dividir()
        self.dados=dados
        self.clientes = clientes


        # ---------------------- interaction with sockets ------------------------------
    def receive_int(self, connection, n_bytes: int) -> int:
        """
        :param n_bytes: The number of bytes to read from the current connection
        :return: The next integer read from the current connection
        """
        data = connection.recv(n_bytes)
        return int.from_bytes(data, byteorder='big', signed=True)

    def send_int(self, connection, value: int, n_bytes: int) -> None:
        """
        :param value: The integer value to be sent to the current connection
        :param n_bytes: The number of bytes to send
        """
        connection.send(value.to_bytes(n_bytes, byteorder="big", signed=True))

    def receive_str(self, connection, n_bytes: int) -> str:
        """
        :param n_bytes: The number of bytes to read from the current connection
        :return: The next string read from the current connection
        """
        data = connection.recv(n_bytes)
        return data.decode()

    def send_str(self, connection, value: str) -> None:
        """
        :param value: The string value to send to the current connection
        """
        connection.connection.send(value.encode())

    # TODO
    # Implement a method that sends and object and returns an object.
    # ...
    def send_object(self, connection, obj):
        """1º: envia tamanho, 2º: envia dados."""
        data = json.dumps(obj).encode('utf-8')
        size = len(data)
        self.send_int(connection, size, servidor.INT_SIZE)  # Envio do tamanho
        connection.send(data)  # Envio do objeto

    def receive_object(self, connection):
        """1º: lê tamanho, 2º: lê dados."""
        size = self.receive_int(connection, servidor.INT_SIZE)  # Recebe o tamanho
        data = connection.recv(size)  # Recebe o objeto
        return json.loads(data.decode('utf-8'))
    def run(self):
        print(self.clientes.listar())
        print(self.address,"Thread iniciada")
        last_request = False
        while not last_request:
            request_type = self.receive_str(self.connection,servidor.COMMAND_SIZE)
            if request_type == servidor.ADD_OP:
                x = self.receive_int(self.connection,servidor.INT_SIZE)
                y = self.receive_int(self.connection,servidor.INT_SIZE)
                print(self.address, ":somar ", x, " + ", y)
                result = self.sum.execute(x, y)
                self.send_int(self.connection,result, servidor.INT_SIZE)
                # Regista soma
                self.dados.registar_oper('soma', x, y, result, self.address)
                print(self.address, ": registada uma soma")
                print(self.dados.get_operacoes())
            elif request_type == servidor.SUB_OP:
                x = self.receive_int(self.connection,servidor.INT_SIZE)
                y = self.receive_int(self.connection,servidor.INT_SIZE)
                print(self.address, ":somar ", x, " - ", y)
                result = self.sub.execute(x, y)
                self.send_int(self.connection,result, servidor.INT_SIZE)
                # Regista soma
                self.dados.registar_oper('subtracao', x, y, result, self.address)
                print(self.address, ": registada uma subtração")
                print(self.dados.get_operacoes())

            elif request_type == servidor.END_OP:
                last_request =True
                self.clientes.disconectar([self.connection,self.address])
                print(self.address,"Thread terminada")
                self.connection.close()
