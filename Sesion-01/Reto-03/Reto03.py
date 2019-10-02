def calcularIMC(peso, estatura):
    IMC = peso / (estatura**2)
    return IMC

def revisarEstadoDeSalud(peso, estatura):
    IMC = calcularIMC(peso,estatura)
    if(IMC < 18.5):
        print("te encuentras en peso bajo")
    elif(IMC >= 18.5 and IMC < 24.9):
        print("te encuentras en tu peso normal")
    elif(IMC >= 25.0 and IMC < 29.9):
         print("Te encuentras en sobrepeso")
    elif(IMC >= 30.0 and IMC < 34.9):
         print("Te encuentras en obesidad grado I")
    elif(IMC >= 35.0 and IMC < 39.9):
         print("Te encuentras en obesidad grado II")
    else:
        print("Te encuentras en obesidad grado III")
        
        
revisarEstadoDeSalud(85,1.85)

