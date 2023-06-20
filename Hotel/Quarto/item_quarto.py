class Item_Quarto:
    def __init__(self, nome,valor):
        self.nome = nome
        self.valor = valor
        self.disponivel = True

    def consumir(self):
        self.disponivel = False
