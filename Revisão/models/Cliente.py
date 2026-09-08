class Cliente:
    id = None
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def exibir(self):
        return (f"Nome: {self.nome}  |  Email: {self.email}  |  Telefone: {self.telefone}")

    def converter_tupla(self):
        return (self.nome, self.email, self.email)

    @staticmethod
    def reverter_tupla(tupla):
        cliente = Cliente(tupla[1], tupla[2], tupla[3])
        cliente.id = tupla[0]
        return cliente