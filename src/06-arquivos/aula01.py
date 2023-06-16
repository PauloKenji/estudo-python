""" Aula 06 - Arquivos """

# open("caminho","r")

# mode
# r - read
# a - append
# w - write
# x - create
# r+ - read and write

arquivo = open("06-arquivos/test2.txt","x")

# print(arquivo.readable())
# print(arquivo.writable())
# print(arquivo.read())
# print(arquivo.readline())
# print(arquivo.readlines())

# lista = arquivo.readlines()
# print(lista[0])

arquivo.write("Python\n")
arquivo.write("C++\n")
arquivo.write("Java\n")

arquivo.close()

import os

if os.path.exists("06-arquivos/test.txt"):
    os.remove("06-arquivos/test.txt")
else:
    print("O arquivo não existe")

os.rmdir("06-arquivos/pasta")