##ejercicio Alerta telemática

#Datos# 
velocidad = [25, 12, 19, 16, 11, 11, 24, 1,
 14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
 14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2,
 14, 23, 19, 23, 9, 18, 20, 22, 14, 1,
 10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5,
 11, 10, 18, 10, 14, 5, 23, 20, 23, 21]

promedio=sum(velocidad)/len(velocidad) ##me permite definir el promedio de los datos totales

print("El promedio de las velocidades es [m/s]:", promedio) ##permite imprimir dicho promedio obtenido

nueva_lista=[]

for correa, i in enumerate(velocidad):
    if i>promedio:
        nueva_lista.append(correa)

print("El listado de correas es:", nueva_lista) ## permite identificar la posición de las correas para las velocidades sobre el promedio

 
