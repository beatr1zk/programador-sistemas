print("\nInsira as informações para calcular o seu salário final\n")

nome_fun = input("Digite o seu nome: ")
salario = float(input("Valor total do seu salário: "))
hora_extra = float(input("Horas extras trabalhadas: "))
valor_hora = float(input("Qual o valor da sua hora: "))
desconto = float(input("Valor total dos seus descontos: "))


hora_extra_total = hora_extra * valor_hora
valor_total = hora_extra_total + salario - desconto

print(f"O valor da sua hora extra esse mês foi de: R${hora_extra_total}")
print(f"O valor total do seu salário, já somado as horas extras este mes é de: R${valor_total}")




