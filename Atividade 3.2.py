soma = 0
trasacoes = int(input("Quantas transações você fez hoje? "))
for valor in range(0, trasacoes):
    valor = float(input("Informe o valor gasto: "))
    soma = soma + valor
    media = soma / trasacoes

print("Você gastou um total de R${:.2f} e a média de gastos por transações foi de {:.2f}".format(soma, media))