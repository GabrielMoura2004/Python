tupla = (1, 7, 7, 19, 3, 2, 11, 15, 6, 1,5)
print(f"A tupla foi criada assim:{tupla}")


for numero, valor in enumerate(tupla):
    print(f"No índice {numero} temos:{valor}")

print(f"Quantidade:{len(tupla)}")


print(f"Máximo: {max(tupla)}")

print(f"Mínimo:{min(tupla)}")

print(f"Soma{sum(tupla)}")

lista=[True,False]
print(f"Lista:{lista}")
tupla2= tuple(lista)
print(f"Tupla:{tupla2}")

tupla3 = (1,0)

print(f"Testando a tupla2 com all:{all(tupla2)}")
print(f"Testando a tupla3 com all:{all(tupla3)}")

print(f"Testando a tupla2 com any:{any(tupla2)}")
print(f"Testando a tupla3 com any:{any(tupla3)}")
