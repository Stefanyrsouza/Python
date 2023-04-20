# > LAÇOS DE REPETIÇÃO = FOR

"""for variavel in range(5):
    print(variavel)

for variavel in range(1, 10):
    print(variavel)

for variavel in range(1, 12, 3):
    print(variavel)"""

# Exemplo1: receber 3 notas e realizar a média.

"""nota1 = float(input('Infome sua nota 1:'))
nota2 = float(input('Infome sua nota 2:'))
nota3 = float(input('Infome sua nota 3:'))"""

soma = 0

for i in range(1, 4):
    nota = float(input('Infome sua nota {i}:'))

    soma = soma + nota

print(soma / 3)
