from Hotel.Quarto.quarto import Quarto


class Quarto_Duplo(Quarto):
    def __init__(self, num_quarto):
        tipo = "Casal"
        diaria = 210.00
        super().__init__(num_quarto, tipo, diaria)
