from Hotel.hotel import Hotel


def main():
    hotel = Hotel()
    hospedagem = hotel.criar_hospedagem("Bruno", "123456", "Casal")
    hospedagem.consumir_item("coca-cola")
    hospedagem.consumir_item("biscoito")
    hotel.finalizar_hospedagem("123456")
    hospedagem = hotel.criar_hospedagem("Bruno", "123456", "Solteiro")
    hospedagem.consumir_item("coca-cola")
    hospedagem.consumir_item("biscoito")
    hospedagem.consumir_item("snack")
    hotel.finalizar_hospedagem("123456")


if __name__ == '__main__':
    main()