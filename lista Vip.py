frase = input("Digite uma frase: ") 
with open("frases.txt" , "a") as arq:
    arq.write(frase + "\n")
with open("frases.txt", "r") as arq:
    for linha in arq:
        if len(linha.strip()) > 10:
            print(linha.strip())

        

