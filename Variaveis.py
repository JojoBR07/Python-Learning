#!python3

""" 
    Olá Jovem Padawan 💻

Python não possui palavras 
reservadas como int, float, string...
Neste caso, quando a variavel recebe 
seu primeiro valor, automaticamente 
ela assume um tipo correspondente
e não altera até o final da execução

    Segue alguns exemplos 🤓
"""

#Atribuição de Int e Float
A = 3 
B = 4.4 

#Atribuição de String
idade = 'Minha idade é '

#Imprimindo Variaveis
print(A)

#Imprimindo e concatenando variavis
print(f'{idade} {A}')

#Usuário informando valores
PI = 3.14
raio = float(input('Informe o valor do Raio:'))
area = PI * pow(raio, 2) #Função utilizada para potencia
print(area)