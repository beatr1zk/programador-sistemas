class Veiculo:
    veiculos = []

    def __init__(self, modelo, marca, ano):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self._vendido = False

        Veiculo.veiculos.append(self)

    def __str__(self):
        return f"Modelo: {self.modelo} Marca: {self.marca} Ano: {self.ano} Status: {self.vender}"

    @classmethod
    def listar_veiculos(cls):
        for veiculo in cls.veiculos:
            print (f"\nModelo: {veiculo.modelo} \n| Marca: {veiculo.marca} \n| Ano: {veiculo.ano} \n| Status: {veiculo.vender}\n\n---------------------------------------------------" )

    @property
    def vender(self):
        return "Vendido" if self._vendido else "Disponível"

    def alterar_status(self):
        self._vendido = not self._vendido

