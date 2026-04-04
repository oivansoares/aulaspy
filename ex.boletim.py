disciplinas = [ "Matematica", "Portugues", "Ingles", "Historia", "Geografia" , "Fisica", "Quimica", "Biologia", "Educaçao Fisica", "Artes" 
]


notas = [ 8.5, 9.0, 7.5, 6.0, 8.0, 9.5, 7.0, 8.5, 9.0, 7.5
]


lista = []

for i in range(3):
    texto = input("Digite algo: ")
    lista.append(texto + "\n")

with open("arquivo.txt", "w") as arquivo:
    arquivo.writelines(lista)

# O código acima solicita ao usuário que digite algo três vezes, armazenando cada entrada em uma lista chamada lista. Em seguida, o conteúdo da lista é escrito em um arquivo chamado "arquivo.txt" usando o método writelines(), que escreve cada elemento da lista como uma linha separada no arquivo. O arquivo é aberto no modo de escrita ("w"), o que significa que se o arquivo já existir, ele será sobrescrito; caso contrário, um novo arquivo será criado.