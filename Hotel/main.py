from Hotel.hotel import Hotel


def main():
    hotel = Hotel()

    nome = input("Digite o nome do hóspede: ")
    cpf = input("Digite o CPF do hóspede: ")
    tipo_quarto = input("Digite o tipo de quarto (Casal/Solteiro): ")

    hospedagem = hotel.criar_hospedagem(nome, cpf, tipo_quarto)

    item = input("Digite o nome do item a ser consumido: ")
    hospedagem.consumir_item(item)

    opcao = input("Deseja consumir mais itens? (S/N): ")
    while opcao.upper() == "S":
        item = input("Digite o nome do item a ser consumido: ")
        hospedagem.consumir_item(item)
        opcao = input("Deseja consumir mais itens? (S/N): ")

    cpf_hospede = input("Digite o CPF do hóspede para finalizar a hospedagem: ")
    hotel.finalizar_hospedagem(cpf_hospede)


if __name__ == '__main__':
    main()
