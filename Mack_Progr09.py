'''Lista de Exercícios Estrutura Sequencial. 

Resolva os exercícios em Python -

EXERCÍCIO 1 – Escreva um programa em Python que permita ao usuário
digitar dois números inteiros e exibir o resultado para cada uma das
seguintes operações: soma, subtração, multiplicação, divisão, divisão
truncada, resto e exponenciação. '''

print('Digite um número:')
user1 = int(input())
print('Digite outro número:')
user2 = int(input())
soma = (user1+user2)/5
print(f'A divisão com base na soma das variáveis é {soma}', 'e a multiplicação do resultado da variável soma menos o valor de 5 é igual a', soma *3-5)
'''>>> No console do Shell: A divisão com base na soma das variáveis é 20.0 e a multiplicação do resultado da variável soma menos o valor de 5 é igual a 55.0'''


'''EXERCÍCIO 2 – Faça um programa em Python que leia dois números inteiros e exiba o quadrado da diferença do primeiro valor pelo segundo.''' 
print('Digite o primeiro número:')
numero1 = int(input())
print('Digite o segundo número:')
numero2 = int(input())
resultado = (numero1*numero2)/2
print('O quadrado da diferença do primeiro valor pelo segundo é', resultado)


'''EXERCÍCIO 3 – Faça um programa em Python que resolva o seguinte problema: 
Um concurso possui um prêmio no montante de R$ 780.000,00 para dividir entre três ganhadores da seguinte forma: 
- o primeiro ganhador receberá 46% do prêmio; 
- o segundo ganhador receberá 32% do prêmio; 
- o terceiro ganhador receberá o restante do prêmio.'''

premioMontante = 780.000
jogador1 = 46
jogador2 = 32
jogador3 = 22
ganhador1 = (jogador1)*(premioMontante)/100 
print('O primeiro ganhador levou', ganhador1)
ganhador2 = (jogador2)*(premioMontante)/100
print('O segundo ganhador ficou com', ganhador2)
ganhador3 = (jogador3)*(premioMontante)/100
print('e o terceiro ganhador levou apenas', ganhador3)
'''>>>O primeiro ganhador levou 358.8
O segundo ganhador ficou com 249.6
e o terceiro ganhador ficou apenas com 171.6'''


