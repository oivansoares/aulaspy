nota = 5
media = 6
nota_recuperacao = 2
nota_final = 10

if nota >= media:
    print("Aprovado😁👍")
elif nota < media: # aluno na recuperação
    print("Recuperação😕")
    if nota_recuperacao >= media:
        print("Aprovado na recuperação😁👍")
    if nota_recuperacao < media:
        print("Voce vai para prova final")
    if nota_final >= media:
        print("Aprovado na prova final😁👍")
    else:
        print("Reprovado na prova final😞👎 ")





