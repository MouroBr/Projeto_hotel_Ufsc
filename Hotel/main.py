from Hotel import hotel
from Hotel.hotel import Hotel


def main():
    hotel = Hotel()

    tipo_quarto = input("Digite o tipo de quarto (Casal/Solteiro): ")
    nome = input("Digite o nome do hóspede: ")
    cpf = input("Digite o CPF do hóspede: ")
    qtde_dias = int(input("Digite a quantidade de dias da hospedagem: "))

    hospedagem = hotel.criar_hospedagem(nome, cpf, tipo_quarto, qtde_dias)

    item = input("Digite o nome do item a ser consumido: ")
    hospedagem.consumir_item(item)

    opcao = input("Deseja consumir mais itens? (S/N): ")
    while opcao.upper() == "S":
        item = input("Digite o nome do item a ser consumido: ")
        hospedagem.consumir_item(item)
        opcao = input("Deseja consumir mais itens? (S/N): ")

    cpf_hospede = input("Digite o CPF do hóspede para finalizar a hospedagem: ")

    hotel.finalizar_hospedagem(cpf_hospede)

    hospedagem = hotel.criar_hospedagem("Bruno", 456789, "Casal", 2)
    hotel.finalizar_hospedagem(456789)


if __name__ == '__main__':
    main()
