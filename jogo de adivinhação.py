numero_certo = 13
tentativas = 5

while tentativas > 0:
    chute = int(input(f"Digite um número (tentativas restantes: {tentativas}): "))

    if chute < numero_certo:
        print("Número baixo, tente novamente")
    elif chute > numero_certo:
        print("Número alto, tente novamente")
    else:
        print("Parabéns, você acertou o número!")
        break

    tentativas -= 1  # diminui uma tentativa

# se sair do loop sem acertar
if tentativas == 0:
    print("Você perdeu! 😢 O número era", numero_certo)