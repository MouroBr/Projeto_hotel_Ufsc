from Hotel.hospedagem import Hospedagem
from Hotel.hospede import Hospede
from Quarto.Tipos_Quarto.quarto_duplo import Quarto_Duplo
from Quarto.Tipos_Quarto.quarto_simples import Quarto_Simples


class Hotel:
    def __init__(self):
        self.nome = "Hotel Topzera do Bruno"
        self.quartos = []
        self.hospedes = []
        self.hospedagens = []
        self.valor_caixa = 0

        self.quartos.append(Quarto_Duplo("1"))
        self.quartos.append(Quarto_Duplo("2"))
        self.quartos.append(Quarto_Duplo("3"))
        self.quartos.append(Quarto_Duplo("4"))
        self.quartos.append(Quarto_Simples("5"))
        self.quartos.append(Quarto_Simples("6"))
        self.quartos.append(Quarto_Simples("7"))
        self.quartos.append(Quarto_Simples("8"))

    def buscar_quarto_disponivel(self, tipo_quarto):
        for quarto in self.quartos:
            if quarto.tipo == tipo_quarto and quarto.disponivel:
                return quarto

        return 'Quarto indisponivel'

    def buscar_hospede(self, nome_hospede, cpf_hospede):
        for hospede in self.hospedes:
            if hospede.cpf == cpf_hospede:
                print('Olá ' + hospede.nome + ', bem vindo novamente.')
                return hospede

        print('Olá ' + nome_hospede + ', bem vindo.')
        novo_hospede = Hospede(nome_hospede, cpf_hospede)
        self.hospedes.append(novo_hospede)
        return novo_hospede

    def buscar_hospedagem(self, cpf_hospede):
        for hospedagem in self.hospedagens:
            if hospedagem.hospede.cpf == cpf_hospede and not hospedagem.pagamento_realizado:
                return hospedagem

        return 'Hospede não hospedado.'

    def criar_hospedagem(self, nome_hospede, cpf_hospede, tipo_quarto):
        quarto = self.buscar_quarto_disponivel(tipo_quarto)

        if quarto == 'quarto indisponivel':
            return 'Quarto indisponivel'

        hospede = self.buscar_hospede(nome_hospede, cpf_hospede)

        qtde_dias = 0
        hospedagem = Hospedagem(quarto, hospede, qtde_dias)
        self.hospedagens.append(hospedagem)
        return hospedagem

    def finalizar_hospedagem(self, cpf_hospede):
        hospedagem = self.buscar_hospedagem(cpf_hospede)

        if hospedagem == 'hospede não hospedado.':
            return 'Hospede não hospedado.'

        print('Cobrando hospedagem')
        valor_diaria = hospedagem.valor_total_diarias()
        itens_consumidos = hospedagem.valor_total_itens_consumidos()

        total_pagar = valor_diaria + itens_consumidos

        print(hospedagem.hospede.nome + ' verificando quanto vc deve pagar.')
        print(f'total:{total_pagar}')

        self.valor_caixa = self.valor_caixa + total_pagar

        hospedagem.finalizar()

        print('Hospedagem paga')
        print(f'Hotel tem em caixa :{self.valor_caixa}')
