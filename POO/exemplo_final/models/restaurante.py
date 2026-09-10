from models.avaliacoes import Avaliacoes

class Restaurante:
    restaurantes = []
    avaliacoes = []

    def __init__(self, nome_restaurante, localizacao, tipo_comida, qntd_funcionarios):
        self.nome_restaurante = nome_restaurante
        self.localizacao = localizacao
        self.tipo_comida = tipo_comida
        self.qntd_funcionarios = qntd_funcionarios
        self._status = False
        self._avaliacoes = []

        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"Nome: {self.nome_restaurante} \nRua: {self.localizacao} \nTipo de comida: {self.tipo_comida} \nQuantidade de funcionários: {self.qntd_funcionarios} \nStatus: {self.ativo}"

    @classmethod
    def listar_restaurantes(cls):
        for restaurante in cls.restaurantes:
            print(f"\nNome: {restaurante.nome_restaurante} \n| Rua: {restaurante.localizacao} \n| Tipo de Comida: {restaurante.tipo_comida} \n| Quantidade de Funcionários: {str(restaurante.qntd_funcionarios)} \n| Avaliações: {restaurante.media_avaliacoes} \n| Status: {restaurante.ativo} \n\n---------------------------------------------------")

    @property
    def ativo(self):
        return 'Ativo' if self._status else 'Inativo'

    @property
    def media_avaliacoes(self):
        if not self._avaliacoes:
            return 0
        notas_somadas = sum(avaliacao._nota for avaliacao in self._avaliacoes)
        quantidade_avaliacoes = len(self._avaliacoes)

    def alterar_status(self):
        self._status = not self._status

    def receber_avaliacoes(self, cliente, nota):
        avaliacao = Avaliacoes(cliente, nota)
        self._avaliacoes.append(avaliacao)
