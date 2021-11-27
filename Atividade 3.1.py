alimento = str(input)
caloria_total = 0

while alimento!=("0"):
    print("Digite o alimento ingerido. Digite '0' para finalizar")
    alimento = (input("Alimento: "))
    print("Digite a quantidade de calorias. Digite '0' para finalizar")
    calorias = int(input("Calorias: "))
  
    caloria_total = caloria_total + calorias
    
print("Total de calorias ingeridas: {}".format(caloria_total))