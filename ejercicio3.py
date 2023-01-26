peso: float = float( input("Escriba su peso en kg "))
estatura: float= float( input("Escriba su estatura en metros")) 
imc = round(peso/estatura**2,2) 
print("Tu índice de masa corporal es " + str(imc))
