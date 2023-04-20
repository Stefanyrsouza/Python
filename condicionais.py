# > ESTRUTURAS CONDICIONAIS

""" Imagine que você queira imprimir "Aprovada(o)", caso
    o estudante tenha uma média superior ou igual a 7, e "Reprovado",
    caso a média seja inferior a 7."""


media = float(input('Informe a média do estudante:'))

if media >= 7:
    print('Você foi Aprovada(o)!')

elif media >= 5:
    print('Você está em recuperação!')

else:
    print('Você foi reprovada(o)!')
