#!python3

""" 
    Olá Jovem Padawan 💻

Estrutura de repetição FOR

    Segue alguns exemplos 🤓
"""

for i in range(10):  # Vai de 0 ao 9
    print(i)

for i in range(1, 11):  # Vai de 1 ao 10
    print(i)

for i in range(1, 100, 7):  # Vai de 1 ao 100 incrementando de 7 em 7
    print(i)

lista = [1, 4, 8, 16, 20]
for i in range(20, 0, -2):  # Vai de 20 ao 0 decrementando de 2 em 2
    print(i, end=' ')

for i in range(0, 10):
    pass  # comando permitir definir estrutura vazia

for i in range(0, 10):
    while i == 1:
        continue  # Interrompe o while mas continua o for

for i in range(0, 10):
    while i == 1:
        break  # Interrompe o while e o for
