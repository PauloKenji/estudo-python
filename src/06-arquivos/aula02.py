""" Aula 02 - Arquivos """

arq = open("06-arquivos/test2.txt","w") 

x = ['Caio\n','João\n','Maria\n']

arq.writelines(x) #substitui

arq.close()

with open('06-arquivos/test2.txt','w') as arq:
    arq.write('hello\n')

print('fim write')

with open('06-arquivos/test2.txt','a') as arq:
    arq.write('world')

print('fim append')

with open('06-arquivos/test2.txt','r') as arq:
    # x = arq.read()
    # print(x)
    x = arq.readlines()
    print(x)

print('fim read')

with open('06-arquivos/test2.txt','rb') as arq:
    x = arq.read()
    print(type(x))
    print(type(x.decode('utf-8')))

print('fim read bytes')

with open('06-arquivos/test2.txt','r') as arq:
    for i in arq:
        print(i,end=' ')

print('\n////\n')

with open('06-arquivos/test2.txt','r') as arq:
    print(next(arq))