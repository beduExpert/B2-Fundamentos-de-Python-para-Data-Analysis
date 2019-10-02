listaCantidades = [3,2,4,1]
listaCosas = ['manzanas', 'peras', 'cajas de cereal', 'paquetes de arroz']

listaSuper = []
for contador in range(0, len(listaCosas)):
    listaSuper.append(str(listaCantidades[contador]) + " " +listaCosas[contador])
    print(listaSuper[contador])

