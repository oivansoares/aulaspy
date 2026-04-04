with open("frases.txt", "a") as arq:
    for i in range(5):
        frase = input("Digite uma frase: ")
        arq.write(frase + "\n")

contador = 0

with open("frases.txt", "r") as arq:
    for linha in arq:
        contador += 1

print(f"O arquivo possui {contador} linhas.")

# O código acima abre o arquivo "frases.txt" no modo de escrita ("a") usando a declaração with, que garante que o arquivo seja fechado automaticamente após o bloco de código ser executado. Em seguida, um loop é executado cinco vezes, solicitando ao usuário que digite uma frase. Cada frase digitada é escrita no arquivo, seguida por uma nova linha ("\n"). Depois disso, o código conta o número de linhas no arquivo "frases.txt" abrindo-o no modo de leitura ("r") e iterando sobre cada linha para incrementar um contador. Por fim, o número total de linhas é impresso na tela.