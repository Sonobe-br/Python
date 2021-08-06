print('Digite 2 números: ')
a = int(input())
b = int(input())
media = (a+b)/2
print('Média = ', media)

'''Testes de Prints'''
a = 1
b = 2
#exemplo nº1
print('O número que está em a é %d e em b é %d' %(a,b))
#exemplo nº2
print('O número que está em a é 2%.f e em b é 2%.f' %(a,b))
#exemplo nº3
print('O número que está em a é', a,'e em b é', b)
#exemplo nº4
print('O número que está em a é {} e em b é {}'.format(a,b))
#exemplo nº5
print(f'O número que está em a é {a} e em b é {b}')

a = 1.0
b = 2.0
#exemplo nº6
print(f'O número que está em a é {a} e em b é {b}')
