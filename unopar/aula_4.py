# Primeiros passos em Python:
print('Olá mundo!')

# Estrutura condicional simples:
nome = 'Rayan'
sobrenome = ' '
lista = []

if nome:
    # Isso só será executado se a condição imposta for verdadeira
    print("A variável nome não é vazia")


# Estrutura composta

valor1 = int(input('Insira um valor: '))
valor2 = int(input('Insira outro valor: '))
if valor1 > valor2:
    print("O primeiro valor é maior que o segundo.")
else:
    print('O segundo valor é maior que o primeiro.')

# Estrutura encadeada
color = str(input('Escolha uma das cores do semáforo: '))
if color == 'Verde':
    print('Acelere')
elif color == 'Amarelo':
    print('Desacelere um pouco')
elif color == 'Vermelho':
    print('Pare! Uepaaa, XIIIII RAPAAAAAZ ele gooooosta')
else:
    print('Essa cor nem existe no semáforo mano wtf tá doido é')

# Estrutura condicional:
qtde_faltas = int(input('Digite a quantidade de faltas: '))
soma_notas = float(input('Digite a soma das suas notas: '))
media_final = soma_notas/4
if qtde_faltas <= 5 and media_final >= 7:
    print('Sua nota final foi {}. Aluno aprovado!'.format(media_final))
else:
    print('Sua nota final foi {}. Aluno reprovado!'.format(media_final))

# Utilizando for e enumerate() para retornar a posição de cada item dentro de uma sequência.
nome = 'Guido'
for i, c in enumerate(nome):
    print(f'Posição = {i}, valor = {c}')

# Utilizando range:
for x in range(5):
    # Ele irá executar uma sequência de 5 (indo de 0 a 4) até chegar na 5° casa. FUNCIONA
    print(x)
