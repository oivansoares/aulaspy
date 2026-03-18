palavra_proibida = ("feio" , "gay", "burro" , "preto" , "viado" , "ridiculo" , "horrivel" , "doido")

comentario = input("Faça um comentário na foto de Ivan : ").lower()

for palavra in palavra_proibida:
    if palavra in comentario:
        print("comentario bloqueado por conter a palavra :" , palavra)
        break
else :
    print(comentario)
