from models.avaliacoes import Avaliacoes
from models.hotel import Hotel

hotel_1 = Hotel("Trivago")
hotel_2 = Hotel("Decolar")

Avaliacoes(hotel_1, "Bia", 4)
Avaliacoes(hotel_2, "João", 5)


def main():
    print(f"Média de avaliações do {hotel_1.nome_hotel}: {hotel_1.media_avaliacoes}")
    print(f"Média de avaliações do {hotel_2.nome_hotel}: {hotel_2.media_avaliacoes}")

if __name__ == '__main__':
    main()