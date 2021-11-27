altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em Kg: "))
 
imc = peso / altura**2
 
 
if imc < 16:
	print("Baixo peso Grau III")
elif imc < 17:
	print("Baixo peso Grau II")
elif imc < 18.5:
	print("Baixo peso Grau I")
elif imc < 25:
	print("Peso Ideal")
elif imc < 30:
	print("Sobrepeso")
elif imc < 35:
	print("Obesidade Grau I")
elif imc < 40:
	print("Obesidade Grau II")
else:
	print("Obesidade Grau III")

print("Seu IMC é:", imc)