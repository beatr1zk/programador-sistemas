from models.restaurante import Restaurante

la_mafia = Restaurante(
    "La Mafia",
    "Rua Desembargador Motta, Nº 2601",
    "Italiana",
    7
)

coco_bambu = Restaurante(
    "Coco Bambu",
    "Rua Comendador Araújo, Nº 731",
    "Frutos do mar",
    170
)

nomu = Restaurante(
    "Nômade",
    "Rua Paulo Gorski, 1095",
    "Contemporânea",
    15
)

barolo = Restaurante(
    "Barolo",
    "Alameda Dom Pedro II, 144",
    "Italiana",
    25
)

Restaurante.alterar_status(barolo)

la_mafia.receber_avaliacoes("Bia", 4)

def main():
    Restaurante.listar_restaurantes

if __name__ == '__main__':
    main()