class Item:
    id = None
    # Construtor:
    def __init__(self, nome, preco, tipo, disponivel):
        self.nome = nome
        self.preco = preco
        self.tipo = tipo
        self.disponivel = disponivel

    # Métodos:
    def exibir(self):
        return f"Nome: {self.nome}  |  Preço: {self.preco}  |  Tipo: {self.tipo}  |  Status: {"Disponível" if self.disponivel else "Esgotado"}"

    def converte_tupla(self):
        return (self.nome, self.preco, self.tipo, self.disponivel)

    @staticmethod
    def reverte_tupla(tupla):
        item = Item(tupla[1], tupla[2], tupla[3], tupla[4])
        item.id = tupla[1]
        return item