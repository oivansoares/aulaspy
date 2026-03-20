numero = int(input("Digite um número: "))

contador = 0  # Variável para contar os números pares

for i in range(1, numero + 1): # Percorre os números de 1 até o número digitado
    if i % 2 == 0: # Verifica se o número é par (resto da divisão por 2 é igual a 0)
        print(i) # Imprime o número par
        contador += 1 # Incrementa o contador de números pares

print(f"Total de números pares: {contador}") # Imprime o total de números pares encontrados
