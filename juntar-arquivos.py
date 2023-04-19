#!/usr/bin/env python3 

# abre os três arquivos de texto para leitura
arquivo1 = open('br-utf8.txt', 'r')
arquivo2 = open('palavras.txt', 'r')
arquivo3 = open('pt_BR.dic', 'r')



# cria um arquivo novo para escrever
arquivo_final = open('arquivo_final.txt', 'w')

# adiciona todas as palavras dos três arquivos em uma lista
palavras = []
for arquivo in [arquivo1, arquivo2, arquivo3]:
    for linha in arquivo:
        for palavra in linha.split():
            if palavra not in palavras:
                palavras.append(palavra)
                arquivo_final.write(palavra + ' ')

# fecha todos os arquivos
arquivo1.close()
arquivo2.close()
arquivo3.close()
arquivo_final.close()

