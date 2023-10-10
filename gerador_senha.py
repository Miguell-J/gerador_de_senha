import random as rd

char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%¨&*().,/;:[]`~+=-_?'

print('x----x----BEM VINDO AO GERADOR DE SENHAS----x----x')

tam_senha = int(input('COLOQUE O NÚMERO DE DIGITOS DA SUA SENHA: '))

print('x----x----AQUI ESTÁ A SUA SENHA GERADA----x----x \n')

senha = ''

for j in range(tam_senha):
    senha += rd.choice(char)
print(senha)