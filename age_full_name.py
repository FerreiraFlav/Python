#.\venv\scripts\active
# ("""  """) <- entre parenteses é chamado de Docstring não é um comentario mas pode ser utilizado como
#(#) <- isso é a forma de comentar em python, com DocString você consegue pegar mais de uma linha
#print(121,12, sep="*")
#print(123,122,sep="---")
#print(123,213)
#print(1.1+1+2)
#print(type ((1.1)))

nome = input ('Digite seu prmimero nome: ')
sobrenome = input ('Digite seu sobrenome: ')
idade = input ('Digite sua idade: ')
idade = int(idade)
ano_nascimento = 2023 - idade
maior_de_idade = idade >=18
altura_metros = 1.75

fullname = f'{nome }  {sobrenome}'
idade_e_nascimento_altura = f'Tem {idade} e nasceu em {ano_nascimento} e sua altura e {altura_metros}'
print(fullname)
print(idade_e_nascimento_altura)
print('É maior de idade? ', maior_de_idade)





