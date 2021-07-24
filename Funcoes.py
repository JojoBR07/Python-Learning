#!python3

""" 
    Olá Jovem Padawan 💻

Neste módulo existem alguns 
exemplo da utilização de
Funções, aproveite pois funções 
são muito uteis.

    Segue alguns exemplos 🤓
"""

def ola_mundo():
    print('Hellow World')

def vazio():
    pass

def saudacao(nome, dia = 20):
    print(f'Bom Dia {nome} \n Hoje é dia {dia}')

if __name__ == '__main__': #O arquivo só é main quando é executado como principal
    saudacao('Joilson')

def soma(a, b):
    return a + b