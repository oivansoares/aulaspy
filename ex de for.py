notas = [ 9.1 , 9.5 , 6.7 , 10.0]
disciplinas = ( "Propotipagem" , "Interface" , "Prompts" , "Programação")

for i in range(len(notas)):
    print(f"A disciplina {disciplinas[i]} teve a nota : {notas[i]}") #A função len() retorna o número de elementos em uma lista ou tupla, e o range() gera uma sequência de números de 0 até o número fornecido (neste caso, o comprimento da lista de notas). Assim, o loop percorre cada índice da lista de notas e imprime a disciplina correspondente e a nota associada.