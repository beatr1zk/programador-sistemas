from models.avaliacoes import Avaliacoes

class Hotel:
    hoteis = []

    def __init__(self, nome_hotel, cidade):
        self.nome_hotel = nome_hotel
        self.cidade = cidade
        self._avaliacoes = []
        
        Hotel.Hoteis.append(self)

    def receber_avaliacoes(self, cliente, nota):
        avaliacao = Avaliacoes(cliente, nota)
        self._avaliacoes.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacoes:
            return 0
        else:
            total_avaliacoes = sum(avaliacao._nota for avaliacao in self._avaliacoes)
            quantidade_avaliacoes = len(self._avaliacoes)
            media = round(total_avaliacoes/quantidade_avaliacoes, 1)
            return media

