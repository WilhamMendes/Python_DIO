# Interação com usuário
a = int(input("Digite o primeiro valor: "))
b = int(input('Digite o segundo valor: '))

# Valores estáticos
# a = 10
# b = 6

# Operações aritméticas
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

print(type(soma))
print('\nsoma = ' + str(soma))
print(type(subtracao))
print("Subtração = " + str(subtracao) +"\n")
print(multiplicacao)
print(type(divisao))
print('Divisão = ' + str(divisao))
print('Parte inteira da div. = ' + str(int(divisao)))
print("Resto da div. \/")
print(resto)

# Outras formas de imprimir
print("\nOutra forma de imprimir ;<)")
print('Soma = {}  \nSub. = {}  \t Multi. = {}\n\n' .format(soma, subtracao, divisao))

resultado = ("\nDiv. = {d} \nResto = {res} \n\n" .format(res=resto, d=divisao))
print(resultado)

x = '2'
print(type(x)) # Converção de string para inteiro
soma2 = int(x) + 4
print("Soma_2 = " + str(soma2))