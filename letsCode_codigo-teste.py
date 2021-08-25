print("Digite o valor da 1ª compra:")
compra1 = int(input())
print("Digite o valor da 2ª compra:")
compra2 = int(input())
media = (compra1 + compra2) / 2

if media >= 5000:
    print('Compras aprovadas')
else: 
    print('Compras reprovadas')
