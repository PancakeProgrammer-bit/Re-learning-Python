# Estrutura de dados em Python 
# Objetos do tipo sequência 
# Como aprendido antes, se digitarmos Curso, ele contará 5 letras mas diminuirá 1, pois a contagem de caractéres
# começa de 0 e vai até 4
# Logo, a lógica por trás dessa relação é que será feita uma análise de sequências onde n-1

frase = 'Curso e vídeo Python'
print(len(frase)) # Calcula o tamanho da frase

frase = 'Curso e vídeo Python'
print("Água" in frase) # Localiza se tem os caractéres na sequência. Se sim, retorna true, se não, retorna false

print(frase.count('o')) # Conta quantos caractéres tem em uma frase.

# Fatiamento
print(frase[0:5]) # LIteralmente fatia a frase 

print(frase.split( ))#Aqui, ele vai separar cada palavra da frase e vai transformar em lista. Se for definido um parâmetro, ele vai cortar apenas o parâmetro e vai separar as palavras em lista.


