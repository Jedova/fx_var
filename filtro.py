#ejercicio etapa 1

#precios = {'Notebook': 700000,
# 'Teclado': 25000,
# 'Mouse': 12000,
# 'Monitor': 250000,
# 'Escritorio': 135000,
# 'Tarjeta de Video': 1500000}

#import sys

#valor=int(sys.argv[1]) ## me entrega el valor que debo utilizar para la comparación

#nueva_lista=[]

#for x, i in precios.items():  #me busca los items, en pares (x,i), dentro del diccionario
#    if i > valor: # se fija un umbral y se compara con el valor i ya identificado
#        nueva_lista.append(x) #agrega el valor identificado

#print(", ".join(nueva_lista))


#ejercicio etapa 2

precios = {'Notebook': 700000,
 'Teclado': 25000,
 'Mouse': 12000,
 'Monitor': 250000,
 'Escritorio': 135000,
 'Tarjeta de Video': 1500000}

import sys

valor=int(sys.argv[1]) ## me entrega el valor que debo utilizar para la comparación
criterio=(sys.argv[2]) ##definirá si es mayor o menor el umbral

nueva_lista=[]

if criterio=="mayor": # se fija una dirección sobre un umbral a definir en i
    for x, i in precios.items():  #me busca los items, en pares (x,i), dentro del diccionario
        if i>valor:
            nueva_lista.append(x) #agrega el valor identificado bajo la condición mayor que

elif criterio=="menor":
    for x, i in precios.items():  #me busca los items, en pares (x,i), dentro del diccionario
        if i<valor:
            nueva_lista.append(x) #agrega el valor identificado bajo la condición menor que

else:
    print("Lo sentimos, no es una operación válida")
    sys.exit() #utilizado para detener el ciclo si arroja error
    
print(", ".join(nueva_lista))
