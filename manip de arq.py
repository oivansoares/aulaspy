arq = open("bemvindo.txt", "r") #Abre o arquivo "bemvindo.txt" no modo de leitura ("r") e armazena a referência do arquivo na variável arq

msg = arq.read() #Lê o conteúdo do arquivo e armazena na variável msg
arq.close() #Fecha o arquivo para liberar recursos do sistema
print(msg) # Imprime a mensagem lida do arquivo

caminho = "C:\\Users\\Ivan Soares\\Desktop\\aulaspy\\bemvindo.txt" # Define o caminho do arquivo "bemvindo.txt" em uma variável chamada caminho. Certifique-se de usar a barra invertida (\\) ou a barra normal (/) para evitar erros de escape.
with open(caminho , "r") as arq: # Abre o arquivo usando a declaração with, que garante que o arquivo seja fechado automaticamente após o bloco de código ser executado. O arquivo é aberto no modo de leitura ("r") e a referência do arquivo é armazenada na variável arq.
    m = arq.read() # Lê o conteúdo do arquivo e armazena na variável m. O bloco with garante que o arquivo seja fechado corretamente, mesmo que ocorra um erro durante a leitura.
print(m) # Imprime a mensagem lida do arquivo, que é armazenada na variável m.

msg = "Bem-vindo ao curso de Python do Ivan Soares!" # Define a mensagem que será escrita no arquivo "bemvindo.txt" e armazena na variável msg
with open("bemvindo.txt" , "w") as arquivo: # Abre o arquivo "bemvindo.txt" no modo de escrita ("w") usando a declaração with, que garante que o arquivo seja fechado automaticamente após o bloco de código ser executado. A referência do arquivo é armazenada na variável arquivo.
    arquivo.write(msg) # Abre o arquivo "bemvindo.txt" no modo de escrita ("w") usando a declaração with, que garante que o arquivo seja fechado automaticamente após o bloco de código ser executado. O conteúdo da variável msg é escrito no arquivo usando o método write(). Se o arquivo já existir, ele será sobrescrito; caso contrário, um novo arquivo será criado.

with open(caminho) as arq:
    conteudo = arq.read()

conteudo = conteudo + "\nEspero que você aproveite o curso!" # Adiciona uma nova linha e uma mensagem adicional ao conteúdo lido do arquivo, armazenando o resultado na variável conteudo
with open(caminho, "w") as arq: # Abre o arquivo "bemvindo.txt" no modo de escrita ("w") usando a declaração with, que garante que o arquivo seja fechado automaticamente após o bloco de código ser executado. A referência do arquivo é armazenada na variável arq.
    arq.write(conteudo) # Escreve o conteúdo atualizado (que inclui a mensagem adicional) de volta no arquivo "bemvindo.txt" usando o método write(). Se o arquivo já existir, ele será sobrescrito; caso contrário, um novo arquivo será criado. 