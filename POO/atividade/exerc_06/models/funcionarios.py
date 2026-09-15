class Funcionario:
    funcionarios = []

    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self._salario = salario
        
        Funcionario.funcionarios.append(self)

    def __str__(self):
        return f"Nome: {self.nome} | Cargo: {self.cargo} | Salário: {self.salario}"

    @property
    def salario(self):
        return self._salario

    @classmethod
    def listar_funcionarios(cls):
        for funcionario in cls.funcionarios:
            print(f"\nNome: {funcionario.nome} \n| Cargo: {funcionario.cargo} \n| Salário: R$ {funcionario.salario} \n\n---------------------------------------------------")

    def aumentar_salario(self, percentual):
        aumento = self._salario * (percentual / 100)
        self._salario += aumento