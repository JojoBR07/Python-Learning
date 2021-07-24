#!python3

""" 
    Olá Jovem Padawan 💻

Python assim como qualquer
outra linguegem possui
listas/vetores/arrays.
Alem disso também existe algumas
funções bem uteis que podem auxiliar
no aprendizado.

    Segue alguns exemplos 🤓
"""

numeros = [1, 2, 3]  # exemplo de array
print(type(numeros))

numeros.append(3)  # adicionando valores
numeros.append(4)

print(len(numeros))  # exibindo tamanho do array

numeros[3] = 20  # atribuindo valor a uma posição específica
numeros.insert(0, -200)  # inseri um registros na posição 0

print(numeros[-1])  # imprimi sempre o ultimo valor


"""Segue alguns exemplos de Tuplas"""
nomes = ['Joilson', 'Nara', 'Vilson']

print('Joilson' in nomes)  # Imprime se o nome estiver na tupla

print(nomes[0])  # Imprime uma posição especifica

print(nomes[1:3])  # Imprime da posição 1 até a 2

print(nomes)  # Imprime tudo

print(nomes[2:-1])  # imprime tudo da posição dois até o fim do array
