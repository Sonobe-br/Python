'''Código para resolver formas de pagamento Python'''

preco = float(input('Preço normal da etiqueta:'))
cod = int(input('Códigos de (1 a 4):'))

if cod == 1:
    valor = preco * .90
    print('À vista em dinheiro ou débito você recebe 10%% de desconto: R$ %.2f' %valor)
elif cod == 2:
    valor = preco * .95
    print('À vista no cartão de crédito você recebe 5%% de desconto: R$ %.2f' %valor)
elif cod == 3:
    valor = preco/2
    print('Pagamento em 2 vezes, preço normal de etiqueta sem jutos. \nValor da parcela: R$ %.2f' %valor)
else:
    print('Código invalido')
