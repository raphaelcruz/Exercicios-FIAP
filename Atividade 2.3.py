segunda = int(input("Quantidade de votos na segunda feira: "))
terca = int(input("Quantidade de votos na terça feira: "))
quarta = int(input("Quantidade de votos na quarta feira: "))
quinta = int(input("Quantidade de votos na quinta feira: "))
sexta = int(input("Quantidade de votos na sexta feira: "))

if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    print ("Segunda-feira obteve mais votos")
elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
    print ("Terça-feira obteve mais votos")
elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta:
    print ("Quarta-feira obteve mais votos")
elif quinta > segunda and quinta > terca and quinta > quarta and quinta > sexta:
    print ("Quinta-feira obteve mais votos")
elif sexta > segunda and sexta > terca and sexta > quarta and sexta > quinta:
    print ("Sexta-feira obteve mais votos")