nomes = ("João" , "Maria" , "Pedro") #usasse os parenteses para criar uma tupla, e os elementos da tupla são separados por virgula
notas = [7.2 , 8.5 , 10.0 ] #usasse o colchetes para criar uma lista, e os elementos da lista são separados por virgula
disciplina = ["fisica" , "matematica" , "portugues"] #tambem podemos criar uma lista de strings, ou seja, uma lista de palavras
notas.append(9) #para adicionar um elemento no final da lista, usamos o metodo append. O metodo append recebe como parametro o elemento que queremos adicionar na lista. No exemplo acima, estamos adicionando a disciplina quimica no final da lista disciplina.
notas[3] = notas[2] 
# nota de fisica = 7.2
# nota de matematica = 8.5
# nota de portugues = 10.0

print(f"A nota da disciplina {disciplina[-3]} é {notas[3]} do aluno {nomes[0]}") #para acessar um elemento da lista, usamos o nome da lista seguido do indice do elemento entre colchetes. O indice começa em 0, ou seja, o primeiro elemento da lista tem indice 0, o segundo elemento tem indice 1, e assim por diante. No exemplo acima, estamos acessando o segundo elemento da lista disciplina (matematica) e o segundo elemento da lista notas (8.5) para imprimir a nota da disciplina matematica.