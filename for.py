alunos = ( "João", "Maria", "Pedro", "Ana", "Lucas" , "Carla", "Rafael", "Fernanda", "Gustavo", "Juliana") # tupla é uma estrutura de dados imutável, ou seja, não pode ser alterada depois de criada. Ela é definida por parênteses e os elementos são separados por vírgulas. Nesse caso, a tupla alunos contém os nomes dos alunos.
for nome in (alunos): #  in serve para percorrer a lista ou tupla
    nota = float(input(f"Digite a nota de {nome}: "))

    if nota >= 7:
        print(f"Aluno : {nome}\nNota: {nota}\nAprovado ") #sempre quando for utilizar a funçâo for precisa de uma lista/tupla e ter uma variavel dentro do print para mostar o que for querido, nesse caso a variavel é nome, que é o nome de cada aluno da tupla alunos. O for vai percorrer cada elemento da tupla e imprimir o nome de cada aluno.
        print("-----------------\n")
    elif nota >=5 and nota <7 :
        print(f"Aluno : {nome}\nNota: {nota}\nRecuperação")
    if nota < 5 :
        print(f"Aluno : {nome}\nNota: {nota}\nReprovado ") #sempre quando for utilizar a funçâo for precisa de uma lista/tupla e ter uma variavel dentro do print para mostar o que for querido, nesse caso a variavel é nome, que é o nome de cada aluno da tupla alunos. O for vai percorrer cada elemento da tupla e imprimir o nome de cada aluno.
        print("-----------------\n")

#Como funciona:
#1 - O for pega o primeiro aluno da tupla → nome = João.

#2 - Pergunta a nota → usuário digita 8.

#3 - Verifica com if/else → imprime “Aprovado”.

#4 - Vai para o próximo aluno → nome = Maria.

#5 - Pergunta a nota → usuário digita 5.

#6 - 5;,w3
# 2Verifica com if/else → imprime “Reprovado”.

#7 - Continua até o último aluno (Juliana).



