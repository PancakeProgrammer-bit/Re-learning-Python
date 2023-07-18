print('Hello world!')

# Aula 6 - Tipos primitivos e inserção de dados

# Int - Números inteiros, um dos tipos primitivos que não é float e considera apenas o número inteiro antes da vírgula
num1 = int(input('Insira 1 número: '))
num2 = int(input('Insira outro número: '))
soma = num1 + num2
print('A soma entre {} e {} é {}. '.format(num1, num2, soma))


# Mas quais são os típos primitivos?
# int = 7,-4,0,9875 - Qualquer número positivo, negativo ou nulo é inteiro
# float = 4.5,0.076,-15.223 - Números reais e negativos(ponto flutuante). O 7, assim como outros números, pode ser float também: 7.0
# bool = true or false
# str = 'Olá', 'Olá Mundo!', '7,5'

# Como saber o tipo primitivo de um valor
# Vai puxar apenas str, pois ele só se encontra dentro de uma string
n1 = input("Insira um valor: ")
print(type(n1))

# Se puxar como INC, ele ficará da seguinte forma:
n1 = int(input("Insira um número: "))
print(type(n1))  # Basicamente, como setamos o tipo como INC, ele vai localizar apenas valores INC, dando erro se não for dentro da base 10

# Somando dois valores
n1 = int(input("Insira um valor: "))
n2 = int(input('Insira outo valor: '))
print('A soma dos valores é: {}'.format((n1)+(n2)))  # Vai dar 8 se for 5+3

# E pra não somar, só juntar os valores?
n1 = (input("Insira um valor: "))
n2 = (input('Insira outo valor: '))
print('A soma dos valores é: {}'.format((n1)+(n2)))  # vai dar 53 se for 5+3
