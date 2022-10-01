
language = "Python"


#Adding the language variable into a string
print ( "TERRA MÉDIA ICM CALCULATOR"  )   

distancia = int(input("Escreva a distância entre as esferas Palantír: "))
diametro1 = int(input("Escreva diametro do Palantír de Sauron: "))
diametro2 = int(input("Escreva diametro da Palantir de Saruman: "))

icm = distancia/(diametro1+diametro2)


print(f"distancia entre torres: {distancia} .")
print(f"diametro Sauron: {diametro1} .")
print(f"diametro Saruman: {diametro2} .")
print('Interferência de Comunicação Mágica (ICM) : %.2f' % (icm) )
