##ejercicio: apoyo matemático##

##Factorial##

#fact_i=int(input("entregue el valor del factorial: ")) ## entrega el valor que será factorial

#def fact_1(fact_i): ## se define la función
#    r = 1 #para que no se invalide en 0
#    while fact_i > 1:
#        r = r*fact_i #acumula los resultados
#        fact_i = fact_i-1 #da condición n-1 
#    return r
#resultado = fact_1(fact_i) #se define la variable a imprimir
#print(f"El factorial de {fact_i} es {resultado}")

##productoria##

#def prod_1(lista): 
#    resp = 1
#    for valor in lista: 
#        resp *= valor 
#    return resp
#entrada = input("Ingresa los números de la lista separados por comas: ") ##ingresa los valores de la productoria
#lista = [int(x.strip()) for x in entrada.split(",")] ##entrega la lista con los datos eliminando espacios en blanco e identificando entre comas ","
#print(f"La productoria de {lista} es {prod_1(lista)}")


## código con todo unido

## Función factorial ##
def fact_1(fact_i):
    r = 1
    while fact_i > 1:
        r = r * fact_i
        fact_i = fact_i - 1
    return r

## Función productoria ##
def prod_1(lista): 
    resp = 1
    for valor in lista: 
        resp *= valor 
    return resp

## Función principal que coordina ##
def calcular():
    opcion = input("¿Qué deseas calcular? (escribe 'factorial', 'productoria' o 'ambos'): ").strip().lower()

    resultados = []  # con esta lista es posible acumular los resultados

    if opcion == "factorial" or opcion == "ambos": ##considerando ambas posibilidades
        fact_i = int(input("Ingresa el número para el factorial: "))
        resultado_fact = fact_1(fact_i)
        resultados.append(f"El factorial de {fact_i} es {resultado_fact}")

    if opcion == "productoria" or opcion == "ambos":  ##considerando ambas posibilidades
        entrada = input("Ingresa los números de la lista separados por comas: ")
        lista = [int(x.strip()) for x in entrada.split(",")] ##entrega la lista con los datos eliminando espacios en blanco e identificando entre comas ","
        resultado_prod = prod_1(lista)
        resultados.append(f"La productoria de {lista} es {resultado_prod}")

    print("\nRESULTADOS:")
    for res in resultados:
        print(res)

## para ejecutar el controlador ##
calcular()
