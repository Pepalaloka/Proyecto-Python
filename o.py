print("hola soy lalo")

lista = [15, "nombre", 3.1415, True]

print(lista[0])

usuario = ["usernametest1","pass123","coreo@correo.cl","17"]

numeros = [10,50,100,255,500]
#append = agrega valors a la ultima posicion de la lista
numeros.append(1000)
print (numeros)

#exends = agrega un arreglo al final de nuestra list
extra =[75,350,999]
numeros.extend(extra)
print(numeros)

#nsert = agregar valor en posicion espeifica
numeros.insert(6,5000)
print (f"{numeros}\n")
#remove = elimina el valor elegido de la lista
numeros.remove(50)
print(numeros)
#pop = elimina el ultimo registro
#pop(i) = elimina la posicion del numero
numeros.pop()
print(numeros)
numeros.pop(3)
print (f"{numeros}\n")
#reserve = invierte el orden de la lista
numeros.reverse()
print(numeros)

#sort = ordena los valors de menor a mayor
numeros.sort()
print(numeros)
#sort(reverse=true) = ordena los valores de mayor a menor
numeros.sort(reverse=True)
print (f"{numeros}\n")
