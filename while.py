nota = float(input("Digite a nota da disciplina artes de ivan: "))

while nota < 0 or nota > 10: # Verifica se a
    nota = float(input("Nota inválida. Digite novamente: "))    
print(nota)