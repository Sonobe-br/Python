leituraAgua = int(input('O seu consumo de água em metros cúbicos:'))
if leituraAgua <= 10:
    pagaConta = 7 
elif leituraAgua >= 11 and leituraAgua <= 30:
    pagaConta = (leituraAgua - 10) * 1 + 7
elif leituraAgua >= 31 and leituraAgua <= 100:
    pagaConta = (leituraAgua - 30) * 2 + 27
else:
    pagaConta = (leituraAgua - 100) * 5 + 167 

print (f'Valor da sua conta será de R$ = {pagaConta}') 

 










""" Um empresa local de abastecimento de água, a Saneamento Básico da Cidade (SBC), está promovendo uma 
campanha de conservação de água, distribuindo cartilhas e promovendo ações demosntrando a importância da
água para a vida e para o meio ambiente.

Para icentivar ainda mais a economia de água, a SBC alterou os preços de seu fornecimento de forma que,
proporcionalente, aqueles clientes que consumirem menos água paguem menos pelo metro cúbico.

Todo cliente paga mensalmente uma assinatura de R$7 que inclui uma franquia de 10m³ de água. isto é, para 
que qualquer consumo entre 0 e 10m³, o consumidor para a mesma quantia de R$7 reia (notamos que o valor da 
assinatura deve ser pago mesmo que o consumidor não tenha consumido água).
Se o valor foi de 120m³, o valor foi de:
- 7 reias da assinatura básica;
- 20 reais pelo consumo no intervalo de 11 - 30m³; 
- 140 reais pelo consumo no intervalo de 31 - 100m³; 
- 100 reais pelo consumo no intervalo de 101 - 120m³;

Logo o total da conta foi de R$ 267 reais"""
