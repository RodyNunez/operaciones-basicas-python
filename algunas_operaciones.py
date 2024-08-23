


nombre = str(input("Especifique el nombre de la persona: "))

apellido = str(input("Ahora ingresa el apellido: "))

valor_de_suma1 = int(input("Ingrese el primer digito: "))

valor_de_suma2 = int(input("Ingrese el segundo digito a sumar: "))

suma = valor_de_suma1+valor_de_suma2



print(f"{nombre} {apellido} tiene {suma} puntos por el momento")

pregunta_resta = int(input("Ingrese la cantidad a restar: "))

resultado_resta = suma - pregunta_resta

print(f"El resultado de la resta es de: {resultado_resta}")

division_pregunta = int(input("Por cuanto quieres dividir los puntos?: "))

divisor_resultado = suma/division_pregunta

print(f"La division se ha hecho con exito, ahora {nombre} {apellido} tiene {divisor_resultado}")





