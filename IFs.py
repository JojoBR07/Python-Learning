#!python3

""" 
    Olá Jovem Padawan 💻

Eis algumas estruturas de controle 
você se divertir. De uma olhada
em um conceito chamado tabela
verdade.

    Segue alguns exemplos 🤓
"""

nota = float(input('Informa sua nota: '))

if nota >= 9:
    print('Você passou, Parabens!')
elif nota >= 6:
    print('Você passou, Mas deve estudar mais!')
else:
    print('Você reprovou')


if nota:
    print('Existe')
else:
    print('Não existe ou é zero ou é vazio') 