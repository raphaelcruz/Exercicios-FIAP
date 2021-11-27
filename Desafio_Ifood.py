#Ordenar os 6 restaurantes em ordem de Pontuação/Estrelas (1). Critério de desempate: distância (2)
#['nome do local', estrelas, distância]
#local de entrega: FIAP Paulista

a = []

a.append(['Padaria Real - Pinheiros', 4.8, 3.3])
a.append(['Purana - Priemiado Melhor Vegano', 4.7, 3.1])
a.append(['2 Marias Saudável Orgânico', 4.5, 1.2])
a.append(['Frevo - Augusta', 4.4, 1])
a.append(['Muy Comida Caseira - Dino', 4.4, 4])
a.append(['Greenjoy - Pinheiros', 4.8, 3.5])
a.append(['Estadão Grill', 4.5, 1.9])

import operator
a.sort(key=operator.itemgetter(1), reverse=True)

print(str(a).replace('[','').replace(']','\n').replace("'",'').replace(']','\n').replace(',',''))


#ou

a = [
[' Padaria Real - Pinheiros', 4.8, 3.3],
['Purana - Priemiado Melhor Vegano', 4.7, 3.1],
['2 Marias Saudável Orgânico', 4.5, 1.2],
['Frevo - Augusta', 4.4, 1],
['Muy Comida Caseira - Dino', 4.4, 4],
['Greenjoy - Pinheiros', 4.8, 3.5],
['Estadão Grill', 4.5, 1.9],
]

import operator
a.sort(key=operator.itemgetter(1), reverse=True)

print(str(a).replace('[','').replace(']','\n').replace("'",'').replace(']','\n').replace(',',''))