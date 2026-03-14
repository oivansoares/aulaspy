print(f"Escolha uma disciplina\n1- Fisica\n2- Matematica\n3- Portugues\n4- Quimica")
disciplinas = [ "fisica" , "matematica" , "portugues" , "quimica"]
escolha = int(input("Digite o numero de disciplinas: "))

if escolha == 1:
    print(f"Voce escolheu a disciplina {disciplinas[0]}")
elif escolha == 2:
    print(f"Voce escolheu a disciplina {disciplinas[1]}")   
elif escolha == 3:
    print(f"Voce escolheu a disciplina {disciplinas[2]}")
elif escolha == 4:
    print(f"Voce escolheu a disciplina {disciplinas[3]}")
else:
    print("Opcao invalida")
