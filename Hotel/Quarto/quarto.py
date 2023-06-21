from Hotel.Quarto.item_quarto import Item_Quarto


class Quarto:
    def __init__(self, num_quarto, tipo, diaria):
        self.itens_quarto = []
        self.num_quarto = num_quarto
        self.tipo = tipo
        self.diaria = diaria
        self.disponivel = True
        self.add_itens()

    def add_itens(self):
        self.itens_quarto = []
        self.itens_quarto.append(Item_Quarto("snack", 10.00))
        self.itens_quarto.append(Item_Quarto("bolacha", 5.00))
        self.itens_quarto.append(Item_Quarto("biscoito", 5.00))
        self.itens_quarto.append(Item_Quarto("Agua sem gás", 5.00))
        self.itens_quarto.append(Item_Quarto("Agua com gás", 5.00))
        self.itens_quarto.append(Item_Quarto("coca-cola", 8.00))

    def ocupar(self):
        self.disponivel = False

    def liberar(self):
        self.disponivel = True
        self.add_itens()

    def consumir_item_quarto(self, nome_item):
        achou = False
        for item in self.itens_quarto:
            if item.nome == nome_item:
                item.consumir()
                achou = True

        if not achou:
            print('Item não existe')