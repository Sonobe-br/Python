print('Digite quatro números:')
d1 = int(input())
d2 = int(input())
d3 = int(input())
d4 = int(input())
soma = (d1+d2+d3+d4)/4
print('A média da soma dos quatros números é {}'.format(soma))

print('Digite as três notas:')
nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
mediaNotas = (nota1+nota2+nota3)/3
print (f'A média das notas é {mediaNotas}')

print('Digite o peso de cada nota:')
peso1 = int(input())
peso2 = int(input())
peso3 = int(input())
media = (nota1*peso1+nota2*peso2+nota3*peso3)/(peso1+peso2+peso3)
print('Média ponderada = ', media)

salario = float(input('Salário:'))
novoSalario = salario *1.25 '''Guardei o valor na variável'''
print('Novo salário = ',novoSalario)
