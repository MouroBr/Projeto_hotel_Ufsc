class Hospedagem:
    def __init__(self, quarto, hospede, qtde_dias):
        self.quarto = quarto
        self.hospede = hospede
        self.qtde_dias = qtde_dias
        self.pagamento_realizado = False
        quarto.ocupar()

    def consumir_item(self, nome_item):
        self.quarto.consumir_item_quarto(nome_item)

    def valor_total_diarias(self):
        return self.quarto.diaria * self.qtde_dias

    def valor_total_itens_consumidos(self):
        valor = 0

        for item in self.quarto.itens_quarto:
            if not item.disponivel:
                valor = valor + item.valor

        return valor

    def finalizar(self):
        self.pagamento_realizado = True
        self.quarto.liberar()
