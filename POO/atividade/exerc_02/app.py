from models.veiculos import Veiculo

veiculo_1 = Veiculo("Twingo", "Renault", 1998)
veiculo_2 = Veiculo("Beetle", "Volkswagen", 2011)
veiculo_3 = Veiculo("MX-5 Miata", "Mazda", 2005)
veiculo_4 = Veiculo("C3 Pluriel", "Citroën", 2004)
veiculo_5 = Veiculo("C4 Vectra GL do et", "Overclock", 2001)

Veiculo.alterar_status(veiculo_5)

def main():
    Veiculo.listar_veiculos()

if __name__ == '__main__':
    main()