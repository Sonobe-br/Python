""" Faça um programa em Python que receba um valor referente a ano e emita uma mensagem se este ano é ou
não bissexto. 
Por exemplo: 800, 1004, 1852, 2020"""

print ('Insira o ano a ser analisado: \n')
a = int(input())
if (a % 400 ==0) or (a % 4 == 0 and a % 100 != 0):
    print ('O ano é bissexto!')
else:
    print ('O ano digitado não é bissexto')