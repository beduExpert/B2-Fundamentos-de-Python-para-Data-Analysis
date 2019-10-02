listaNombres = ['Ana', 'Rocío', 'Luis', 'Jose Antonio']
listaApellidosPat = ['Vasquez', 'Cuevas', 'Hernández', 'Ramírez']
listaApellidosMat = ['Ortega', 'Florencia', 'López', 'Bastián']

listaNombresCompletos = []

for contador in range(0,len(listaNombres)):
    listaNombresCompletos.append(listaNombres[contador]+" "+listaApellidosPat[contador]+" "+listaApellidosMat[contador])

print(listaNombresCompletos)
