nota = float(input("Digite a nota do aluno: ")) #o usuário irá digitar a nota do aluno, e essa nota será convertida para um número decimal (float) para permitir notas com casas decimais
media = 7.0 # a média para aprovação é 7.0, ou seja, o aluno precisa ter uma nota igual ou superior a 7.0 para ser aprovado diretamente, caso contrário, ele terá que passar por um processo de recuperação ou prova final para tentar alcançar a média necessária para aprovação.
if nota >= media:
    print("Aprovado😁👍")
elif nota < media: # aluno na recuperação
    print(f"Você está na recuperação pois sua nota foi abaixo da média {media}😕")
    nota_recuperacao = float(input("Digite a nota da recuperação: "))
    if nota_recuperacao >= media:
        print(f"Aprovado na recuperação com nota {nota_recuperacao} 😁👍")
    else:   
        print("Voce vai para prova final pois a média é ", media , "e sua nota de recuperação é ", nota_recuperacao , " 😞👎") 
        nota_final = float(input("Digite a nota da prova final: "))
        if nota_final >= media:
            print("Aprovado na prova final com nota ", nota_final, "😁👍")

        else:
            print(f"Reprovado na prova final, pois sua deveria ser maior ou igual a {media} 😞👎 ")

