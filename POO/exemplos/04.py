class Restaurante:
    restaurantes = []

    def __init__(self, nome_restaurante, localizacao, tipo_comida, qntd_funcionarios):
        self.nome_restaurante = nome_restaurante
        self.localizacao = localizacao
        self.tipo_comida = tipo_comida
        self.qntd_funcionarios = qntd_funcionarios
        self.status = False

        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"Nome: {self.nome_restaurante} \nRua: {self.localizacao} \nTipo de comida: {self.tipo_comida} \nQuantidade de funcionários: {self.qntd_funcionarios} \nStatus: {self.status}"

    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f"\nNome: {restaurante.nome_restaurante} \n|Rua: {restaurante.localizacao} \n|Tipo de Comida: {restaurante.tipo_comida} \n|Quantidade de Funcionários: {str(restaurante.qntd_funcionarios)} \n|Status: {restaurante.status} \n\n---------------------------------------------------")
 

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

Restaurante.listar_restaurantes()

