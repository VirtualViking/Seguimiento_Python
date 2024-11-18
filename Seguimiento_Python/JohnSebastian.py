#Trabajo de Python
#John Sebastian Castañeda Hoyos
# 13/11/2024

# 1. Crear lista con nombres de 5 frutas colombianas y mostrar en pantalla

Frutas_colombianas = ["Chontaduro", "Granadilla", "Papaya", "Uvas pasas", "Guayaba agria"]
print(Frutas_colombianas)

# 2.Acceder al segundo y cuarto elemento de la lista anterior
print(f"segundo elemento de la lista: {Frutas_colombianas[1]}")
print(f"cuarto elemento de la lista: {Frutas_colombianas[3]}")

# 3. Crear una lista con los numeros del 1 al 10
numeros = [1,2,3,4,5,6,7,8,9,10]
print(len(numeros))

# 4. Concatenar las listas creadas en el punto 1 y 3
listas_concatenadas = Frutas_colombianas + numeros
print(listas_concatenadas)

# 5. Modificar el tercer elemento de la lista ejercicio 3 al valor de 100
numeros[2] = 100
print(numeros)

# 6. Eliminar el ultimo elemento de la lista ejercicio 3
numeros.pop()
print(numeros)

# 7. Crear una lista con 3 numeros enteros y multiplicar cada elemento por 5
numeros_enteros = [20,4,19]
multiplicacion = [numero * 5 for numero in numeros_enteros]
print(multiplicacion)

# 8. Crear dos listas con 5 numeros enteros y multiplicar ambas listas
num1 = [1,2,3,4,5]
num2 = [6,7,8,9,10]
resultado = [a*b for a,b in zip(num1, num2)]
print(resultado)

# 9. Crear una lista de listas anidadas y acceder al segundo elemento de la segunda lista
anidadas = [[3,4],[6,7]]
segundo_elemento = anidadas[1][1]
print(segundo_elemento)

# 11. Usar el metodo .append() para agregar un nuevo elemento al final de la lista ejercicio 1
Frutas_colombianas.append("Ciruelas")
print(Frutas_colombianas)

# 12. Usar el metodo .insert() para agregar un nuevo elementos en la posicion 2 ejercicio 3
numeros.insert(2,98)
print(numeros)

# 13. Use el metodo remove() para eliminar un elemento especifico de la lista del ejercicio 7
numeros_enteros.remove(4)
print(numeros_enteros)

# 14. Usar el metodo .reverse() para reinvertir el orden de la lista del ejercicio 3
numeros.reverse()
print(numeros)

# 15. Usar el metodo .sort() para ordenar de forma ascendente la lista del ejercicio 7
numeros_enteros.sort()
print(numeros_enteros)

# 16. Usar el método `.pop()` para eliminar y obtener el último elemento de la lista del ejercicio 3.

numeros.pop(9)
print(numeros)

# 17. Usar el metodo count() para contar cuantas veces aparece un elemento especifico en el ejercicio 7

numeros_enteros.count(1)
print(numeros_enteros)

# 18. Usar el metodo index() para obtener el indice de un elemento especifico de la lista del ejercicio 3

indice = numeros.index(5)
print(indice)

# 19. Usar el metodo clear() para eliminar todos los elementos de la lista del ejercicio 1

Frutas_colombianas.clear()
print(Frutas_colombianas)

# 20. Crear una lista vacia y utilizar un blucle for para agregar los numeros del 1 al 10

Lista1 = []
for i in range (1,11):
    Lista1.append(i)

print(Lista1)

# 21. Crear una lista con los nombres de 5 materias favoritas y ordenarlas alafabeticamente

Lista_Materias = ["Programacion" ,"Bases de datos","Ingenieria de software", "Logica programacion", "Fisica electricidad" ]
Lista_Materias.sort()
print(Lista_Materias)

# 22. Crear una lista con los numeros del 1 al 15 y mostrar los multiplos de 3

Lista_multiplos = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for i in Lista_multiplos:
    if i % 3 == 0:
        print(i)

# 27. Crear una lista con los meses del año y usar .index() para obtener el indice del mes de Junio

Meses_año = ["Enero","Febrero,","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
indice_MesAño = Meses_año.index("Junio")
print(f"El indice de Junio es: {indice_MesAño}")

# 28. Crear una lista con el nombre de 6 mascotas y usar .remove() para eliminar una mascota

mascotas = ["Luna", "Max","Bella","Charlie","Lucy","Rocky"]
mascotas.remove("Charlie")
print(mascotas)

# 29. Crear una lista con los numeros del 1 al 20 y usar el metodo .sort(reverse=true) de forma descendente

Numeros1 = list(range(1,21))
Numeros1.sort(reverse=True)
print(Numeros1)

# 30. Crear una lista de 4 libros y utilizar el metodo .append() para agregar un libro al final de la lista

libros = ["1984", "Harry potter", "Hacer amigos", "Mr.Robot"]
libros.append("Juego de tronos")
print(libros)

# 31. Crear una lista con los numeros del 1 al 15 y crear una lista con numeros impares

numeros2 = list(range(1, 16))
numeros_impares = [numero for numero in numeros2 if numero % 2 != 0]
print(numeros_impares)

# 32. Crear una lista con 7 comidas favoritas y usar el metodo .insert() para agregar una comida en la posicion 3

comidas_favoritas = ["Pizza", "Sushi", "Tacos", "Hamburguesa", "Pasta", "Ensalada", "Helado"]
comidas_favoritas.insert(2, "Empanadas")
print(comidas_favoritas)

# 33. Crear una lista con los numeros del 1 al 10 y utilizar el metodo .extend() para agregar una segunda lista con
# los numeros del 11 al 15

numeros_1_10 = list(range(1, 11))
numeros_11_15 = list(range(11, 16))
numeros_1_10.extend(numeros_11_15)
print(numeros_1_10)

# 34. Crear una lista con el nombre de 6 compañeros y usar el metodo .count() para ver cuantas veces se repite el nombre

companeros = ["Ana", "Carlos", "Ana", "Luis", "Maria", "Carlos","Ana"]
repeticiones_ana = companeros.count("Ana")
print(f"El nombre 'Ana' se repite {repeticiones_ana} veces en la lista.")

# 35. Crear una lista con los numeros del 1 al 12 y hacer una lista de los numeros divisibles por 3

numeros = list(range(1, 13))
numeros_divisibles_por_3 = [numero for numero in numeros if numero % 3 == 0]
print(numeros_divisibles_por_3)

# 36. Crear una lista con los numeros del 1 al 20 y utilizar una funcion lambda y el metodo .sort() para ordenar
#la lista de forma descendente

numeros = list(range(1, 21))
numeros.sort(key=lambda x: x, reverse=True)
print(numeros)

# 37. Crear una lista con materias de la universidad y usar el metodo .pop() para eliminar y obtener el ultimo elemento de lista

materias = ["Matemáticas", "Física", "Química", "Historia", "Literatura", "Biología"]
ultima_materia = materias.pop()
print("Lista actualizada:", materias)
print("Última materia eliminada:", ultima_materia)

# 38. Crear una lista con los numeros del 1 al 25 y hacer una lista con los multiplos de 5

Lista_multiplos5 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
for i in Lista_multiplos5:
    if i % 5 == 0:
        print(i)

# 39. Crear una lista con 8 deportes y usar una funcion anonima y el metodo .sort() para ordenar la lista

deportes = ["Fútbol", "Baloncesto", "Tenis", "Natación", "Ciclismo", "Voleibol", "Atletismo", "Golf"]
deportes.sort(key=lambda x: x)
print(deportes)

# 40. Crear una lista con los numeros del 1 al 15y utilizar el metodo .clear() para elimianr todos los elements de la lista

Lista2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
Lista2.clear()
print(Lista2)

# 41. Crear una lista cos lo nombres de 6 paises y usar un bucle for para imprimir cada elemento en minuscula

paises = ["COLOMBIA", "REINO UNIDO", "CANADA", "CHINA", "AUSTRALIA", "ESPAÑA"]
for pais in paises:
    print(pais.lower())

# 42. Crear una lista con 8 videojuegos y utilizar el metodo index() para tener el indice de uno juego especifico

VideoJuegos = ["State of decay 3","Assasin creed","Borderlands","Madden25","Hitman","Lego","Harry Potter","GTA"]
indice_videoJuego = VideoJuegos.index("Harry Potter")
print(f"El indice del video juego Harry potter es: {indice_videoJuego}")

# 43. Crear una lista con los numeros del 1 al 12 y utilizar el metodo .remove() para eliminar un numero especifico

Lista3 = [1,2,3,4,5,6,7,8,9,10,11,12]
Lista3.remove(7)
print(Lista3)












