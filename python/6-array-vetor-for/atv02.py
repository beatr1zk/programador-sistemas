# Crie um vetor contendo cinco nomes

# Mostre o primeiro aluno
# Mostre o último aluno
# Altere o nome armazenado no índice 2
# Adicione outro aluno no final
# Exiba o vetor atualizado
# Mostre a quantidade de personagens

personagens = ["Trystan Maverine", "Evie Sage", "Reinaldo", "Blade Gushiken", "Rebecka Erring"]

print(personagens[1])

print(personagens[len(personagens)-1])

personagens[2] = "Alexander William Kingsley"

personagens.append("Edwin")

print(personagens)  

print(len(personagens))

print(f"Total de alunox: {len(personagens)}")