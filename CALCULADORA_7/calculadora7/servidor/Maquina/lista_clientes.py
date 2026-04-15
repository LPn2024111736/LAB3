class ListaClientes:
    def __init__(self):
        self.clientes={"clientes":[],"clientes-Ativos":[]}

    def connetar(self,cliente:list):
        if cliente not in self.clientes["clientes"]:
            self.clientes["clientes-Ativos"].append(cliente)
            self.clientes["clientes"].append(cliente)

    def disconectar(self,cliente:list):
        if cliente in self.clientes["clientes"]:
            self.clientes["clientes-Ativos"].remove(cliente)

    def listar(self):
        return self.clientes
