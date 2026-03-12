nota = float(input("Digite a nota do aluno: ")) #o usuário irá digitar a nota do aluno, e essa nota será convertida para um número decimal (float) para permitir notas com casas decimais

 #toda vez que a nota for alterada, a nota será atribuiada a uma letra diferente, de acordo com a tabela de conversão de notas americana

if nota >= 8.5 and nota <=10:
    print("A+")
elif nota >= 7 and nota <8.5:
    print("B")
elif nota >6 and nota <7:
    print("C")
else:
    print("F")