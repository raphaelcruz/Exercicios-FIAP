n = int(input("Digite um número inteiro: "))
a = 0
b = 1
c = 0

while c <= n:
    c = a + b
    a = b
    b = c
if n == a or n == b or n == c:
   print(f"Você digitou {n}. Ação bem sucedida")
else:
    print(f"Você digitou {n}. A ação falhou")


#PODERIA SER FEITO ASSIM??
#num = int(input("Digite um número: "))
#anterior = 0
#proximo = 1
#soma = 0
#resultado = 0
#print(soma)
#while proximo < num:
#    print(proximo)
#    soma = proximo + anterior
#    anterior = proximo
#    proximo = soma
#if num == proximo:
#    print(soma)
#    print(f"Você digitou {num}. Ação bem sucedida")
#else:
#    print(f"Você digitou {num}. A ação falhou")