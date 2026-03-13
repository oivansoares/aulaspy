#boletim escolar
print("Boletim Escolar")

print("-----------------------------------------------------")



notas = [
    
    [7.2 , 8.5 , 10.0 , 7.5], #notas do aluno Ivan
    [10.0 , 9.5 , 8.0 , 9.0], #notas do aluno Gabriel
    [8.0 , 7.0 , 9.0 , 8.5], #notas do aluno Manu
    [9.0 , 8.5 , 7.5 , 8.0] #notas do aluno Ayla
] #para fazer uma lista de listas, basta colocar uma lista dentro de outra lista. No exemplo acima, temos uma lista de notas, onde cada elemento da lista é uma lista de notas de um aluno. A primeira lista de notas é a lista de notas do aluno Ivan, a segunda lista de notas é a lista de notas do aluno Gabriel, a terceira lista de notas é a lista de notas do aluno Manu, e a quarta lista de notas é a lista de notas do aluno Ayla.
disciplina = ["fisica" , "matematica" , "portugues" , "quimica"]
nomes = ('Ivan' , 'Gabriel' , 'Manu' , 'Ayla')
bimestre = [1 , 2 , 3 , 4]

print(f"Aluno: {nomes[0]}")
print("-----------------------------------------------------")
print('Disciplina       Notas')
print("-----------------------------------------------------")
print(f'{disciplina[0]}            {notas[0][0]}')
print(f'{disciplina[1]}        {notas[0][1]}')
print(f'{disciplina[2]}         {notas[0][2]}')
print(f'{disciplina[3]}           {notas[0][3]}')

print("-----------------------------------------------------")


