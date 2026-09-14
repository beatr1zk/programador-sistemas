from models.restaurante import Restaurante
from models.cardapio.bebida import Bebida
from models.cardapio.prato import Prato
from models.cardapio.sobremesa import Sobremesa

la_mafia = Restaurante( "La Mafia", "Rua Desembargador Motta, Nº 2601", "Italiana", 7)
coco_bambu = Restaurante("Coco Bambu", "Rua Comendador Araújo, Nº 731", "Frutos do mar", 170)
nomu = Restaurante( "Nômade", "Rua Paulo Gorski, 1095", "Contemporânea", 15)
barolo = Restaurante( "Barolo", "Alameda Dom Pedro II, 144", "Italiana", 25)


prato_1 = Prato( "Conchiglia com recheio de camarão", 129.80, "Conchiglia recheada com camarão e molho San Marino, preparado com mix de queijos e camarão.")
prato_2 = Prato( "Filetto al Pepe Verde", 95.00, "Mignon ao molho cremoso de pimenta verde, acompanhado de tagliatelle de abóbora ou risoto.")
prato_3 = Prato( "Ossobuco", 89.00, "Ossobuco acompanhado de risoto milanês com açafrão ou ravióli de abóbora com sálvia.")

sobremesa_1 = Sobremesa( "Petit Gâteau", 32.00, "Petit gâteau recheado com chocolate ou doce de leite.")

bebida_1 = Bebida( "Coca-Cola", 6.90, "350 ml")

  
coco_bambu.adicionar_cardapio(prato_1)

la_mafia.adicionar_cardapio(prato_2)
la_mafia.adicionar_cardapio(prato_3)
la_mafia.adicionar_cardapio(sobremesa_1)
la_mafia.adicionar_cardapio(bebida_1)


la_mafia.receber_avaliacoes("Bia", 4)


barolo.alterar_status()


def main():
    # Restaurante.listar_restaurantes()
    la_mafia.exibir_cardapio

if __name__ == '__main__':
    main()