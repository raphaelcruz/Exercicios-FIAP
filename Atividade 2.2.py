assinatura = input("Insira aqui o tipo da assinatura:  ")
faturamento_anual = float(input("informe o faturamento anual: R$ "))

if assinatura == "basic":
    bonus = faturamento_anual * 0.3
elif assinatura == "silver":
    bonus = faturamento_anual * 0.2
elif assinatura == "gold":
    bonus = faturamento_anual * 0.1
elif assinatura == "platinum":
    bonus = faturamento_anual * 0.05

print(("Seu bonus de programador será: R$"), bonus)