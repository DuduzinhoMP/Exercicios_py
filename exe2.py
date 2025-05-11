# operadores de comparação
#
# OP --- significado ---- true
# > --- maior -----
# >= --- maior ou igual ---
# < --- menor --- 
# <= -- menor ou igual ---
# == --- igual --- 
# != --- diferente --- 

"""

maior = 2 > 1
maior_ou_igual = 2 >= 2
menor = 1 < 2
menor_ou_igual = 3 <= 3
igual = 'a' == 'a'
diferente = 'a' != 'b'

"""

########################################################

"""
primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('digite o segundo valor: ')

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor} é maior do que {segundo_valor}')
else:
    print(f'{segundo_valor} é maior do que {primeiro_valor}')
"""

#############################################################################

########## BRINCADEIRA

"""

idade = int(input('Digite a sua idade para entrar no sistema: '))

maior_idade = int(idade) > 18

if maior_idade > 18:
    print('Voce está autorizado')
else:
    print('Voce não está autorizado')

"""
# Pede a nota do aluno
nota = float(input("Digite a nota do aluno (0 a 10): "))

# Verifica a situação com if, elif e else
if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")


