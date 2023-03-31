# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso.
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")

def add(x, y):
    return x + y
def substract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

print('''Selecione o número da operação desejada:
 1 - Soma
 2 - Subtração
 3 - Multiplicação
 4 - Divisão''')

escolha = input('Digite sua opção (1/2/3/4): ')
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

'''if escolha == '1':
    print(f'{num1} + {num2} = {num1 + num2}')
elif escolha == '2':
    print(f'{num1} + {num2} = {num1 - num2}')
elif escolha == '3':
    print(f'{num1} + {num2} = {num1 * num2}')
elif escolha == '4':
    print(f'{num1} + {num2} = {num1 / num2}')
else:
    print('Operação incorreta.')'''

if escolha == '1':
    print('\n')
    print(num1 , '+', num2, '=', add(num1, num2))
    print('\n')
elif escolha == '2':
    print('\n')
    print(num1, '-', num2, '=', substract(num1, num2))
    print('\n')
elif escolha == '3':
    print('\n')
    print(num1, '*', num2, '=', multiply(num1, num2))
    print('\n')
elif escolha == '4':
    print('\n')
    print(num1, '/', num2, '=', divide(num1, num2))
    print('\n')
else:
    print('\nOperação incorreta.')

# Fim da Calculadora  #