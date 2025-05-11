'''
Solicita as informações para o usuarios 

Varifica se ele é maior de idade ou não

'''

nome = input('Digite o seu nome: ')
sobrenome = input('Digite o seu sobrenome: ')
idade = int(input('digite a sua idade: '))
altura_metros = float(input('Digite a sua altura: '))


print('Nome:', nome)
print('Nome:', sobrenome)
print(f'Você tem {idade} anos')
if idade >= 18:
    print('Voce é maior de idade')
else:
    print('Voce não é maior de idade')
print('Altura em metros', altura_metros)