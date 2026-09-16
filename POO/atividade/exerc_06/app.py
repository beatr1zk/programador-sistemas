from models.funcionarios import Funcionario

funcionario_1 = Funcionario("Ana", "Designer", 2500)
funcionario_2 = Funcionario("Carlos", "Desenvolvedor", 3500)
funcionario_3 = Funcionario("Beatriz", "Gerente", 4200)
funcionario_4 = Funcionario("João", "Analista", 2250)
funcionario_5 = Funcionario("Mariana", "Administradora", 3100)

funcionario_1.aumentar_salario(10)
funcionario_2.aumentar_salario(15)
funcionario_3.aumentar_salario(5)

def main():
    Funcionario.listar_funcionarios()

if __name__ == '__main__':
    main() 