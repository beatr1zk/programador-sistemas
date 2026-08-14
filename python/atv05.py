nome="Beatriz Kava" 
prod1=61.2
prod2=70
prod3=5.60
prod4=9.39
prod5=215.3

resultado = prod1 + prod2 + prod3 + prod4 + prod5

#pode ser feito assim: como no PHP
print("\nA conta total de", nome, "é: R$", resultado, "\n")

#ou adicionando um f dentro dos parenteses e indicando a string com {}
print(f"\nA conta total de {nome} é: R$ {resultado}\n")
