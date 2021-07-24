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

numeros = [1, 2, 3] #exemplo de array
print(type(numeros))

numeros.append(3) #adicionando valores 
numeros.append(4)

print(len(numeros)) #exibindo tamanho do array

numeros[3] = 20 #atribuindo valor a uma posição específica
numeros.insert(0, -200) #inseri um registros na posição 0

print(numeros[-1]) #imprimi sempre o ultimo valor
