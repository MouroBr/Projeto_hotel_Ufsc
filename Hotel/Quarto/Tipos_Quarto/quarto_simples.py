from Hotel.Quarto.quarto import Quarto


class Quarto_Simples(Quarto):
    def __init__(self, num_quarto):
        tipo = "Solteiro"
        diaria = 110.00
        super().__init__(num_quarto, tipo, diaria)
