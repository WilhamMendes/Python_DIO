
# # OPERADORES CONDICIONAIS

# a = int(input('\nDigite o primeiro valor: '))
# b = int(input('Digite o segundo valor: '))
# c = int(input('Digite o terceiro valor: '))
#
# if a > b and a > c:
#     print('\nO maior valor digitado é o primeiro valor, que é o número: {}' .format(a))
# elif b > a and b > c:
#     print('\nO maior valor digitado é o segundo valor, que é o número: {}' .format(b))
# else:
#     print('\nO maior valor digitado é o terceiro valor, que é número: {}' .format(c))
#
# print('\nPrograma concluido com sucesso!')

##########################################################################################



# # Operadores lógicos
# d = int(input('\nEntre com o primeiro valor: '))
# e = int(input('Entre com o segundo valor: '))
#
# resto_d = d % 2
# resto_e = e % 2
#
# #if resto_d == 0 or resto_e == 0:
# if resto_d == 0 or not resto_e > 0:
#     print('\nVocê digitou um número par!')
#     if resto_d == 0:
#         print('Nesse caso, o primeiro valor é o número par!')
#     elif resto_e == 0:
#         print('Nesse caso, o segundo valor é o número par!')
# else:
#     print('\nNenhum número par foi digitado!')



####################################################################################


# Calculadora da média de um aluno
a = int(input("\nInforme a nota do 1º Bimestre: "))
if a > 10:
    a = int(input('Você digitou nota errada! Digite novamente a nota do 1º Bimestre: '))

b = int(input('informe a nota do 2º Bimestre: '))
if b > 10:
    b = int(input('Você digitou nota errada! Digite novamente a nota do 2º Bimestre: '))

c = int(input('informe a nota do 3º Bimestre: '))
if c > 10:
    c = int(input('Você digitou nota errada! Digite novamente a nota do 3º Bimestre: '))

d = int(input('informe a nota do 4º Bimestre: '))
if d > 10:
    d = int(input('Você digitou nota errada! Digite novamente a nota do 4º Bimestre: '))

media = (a + b + c + d) / 4
print('\nA Média desse aluno é = {}' .format(media))
if media >= 7:
    print("Parabéns, você aprovou. Boas férias ;<)")
else:
    print("Reprovado, boa sorte no prossimo ano :<|)")


# # Outra forma de verificar se a nota digitada está correta
"""
if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    print('\nA Média desse aluno é = {}' .format(media))
else:
    print('\nVocê digitou alguma nota errada!')
"""

