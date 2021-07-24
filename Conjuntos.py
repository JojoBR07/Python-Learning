#!python3

""" 
    Olá Jovem Padawan 💻

Python e outras linguegens 
possuem CONJUNTOS (Sets), algo semelhante a listas
mas que não permite numeros duplucados
e outras peculiaridades

OBS: Conjuntos não possuem indexe, então não é possivel
fazer isso:
    print(nums[0])

    Segue alguns exemplos 🤓
"""

print({1, 2, 3})

nums = ({1, 2, 3, 4, 5})
print(type(nums))

nums.remove(2)  # Removendo um numero
print("Números: ", nums)

nums.discard(1)  # Removendo um numero com a função discard
print("Números: ", nums)
