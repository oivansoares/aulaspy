candidatos = ["bolsonaro", "lula", "ciro"] #lista de candidatos válidos
votos = [] #lista para armazenar os votos dos eleitores

# votação (3 pessoas votando)
for i in range(3):
    voto = input("Digite o nome do candidato: ").lower() #armazena o voto do eleitor e converte para minúsculo
    
    if voto in candidatos: #verifica se o voto é válido (se o candidato existe na lista de candidatos)
        votos.append(voto) #adiciona o voto à lista de votos
    else:
        print("Candidato inválido")

# contagem de votos
resultado = {} #dicionário para armazenar o resultado da contagem de votos

for candidato in candidatos: #percorre a lista de candidatos para contar os votos de cada um
    contador = 0 #variável para contar os votos do candidato atual
    
    for voto in votos: #percorre a lista de votos para contar quantos votos o candidato atual recebeu
        if voto == candidato: #se o voto for igual ao candidato atual, incrementa o contador
            contador += 1 #incrementa o contador de votos do candidato atual
    
    resultado[candidato] = contador #armazena o resultado da contagem de votos do candidato atual no dicionário de resultados
    print(f"{candidato} recebeu {contador} votos")

# descobrir vencedor
maior = 0 #variável para armazenar o maior número de votos recebido por um candidato, inicialmente definida como 0
vencedor = "" #variável para armazenar o nome do candidato vencedor, inicialmente definida como uma string vazia

for candidato in resultado: #percorre o dicionário de resultados para encontrar o candidato com o maior número de votos
    if resultado[candidato] > maior: #se o número de votos do candidato atual for maior do que o maior número de votos registrado até agora, atualiza o valor de maior e o nome do vencedor
        maior = resultado[candidato] #atualiza o maior número de votos registrado
        vencedor = candidato #atualiza o nome do candidato vencedor

print(f"\n🏆 {vencedor} venceu com {maior} votos!")