### Problema de clases: Simulación de biblioteca ###

class Libro:

    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.disponible = True

    def disponibilidad(self):
        return self.disponible
    
    def titulo_libro(self):
        return self.titulo

    def prestar(self):
        if self.disponible == False:
            return f"El libro {self.titulo} no está disponible para préstamo"
        else:
            self.disponible = False
            return f"Ha tomado prestado el libro: {self.titulo}" 

    def devolver(self):
        if self.disponible == False:
            self.disponible = True
            return f"Ha devuelto el libro: {self.titulo}"
        else:
            return f"El libro {self.titulo} ya estaba disponible"
        
    def informacion(self):
        if self.disponible:
            disponible = "Disponible"
        else:
            disponible = "No disponible"  
        return f"Título: {self.titulo}, Autor: {self.autor}, Año: {self.año}, Disponinilidad: {disponible}"
    
biblioteca = []

libro1 = Libro("La perla", "John Steinbeck", 1937)
libro2 = Libro("La muerte en Venecia", "Thomas Mann", 1912)
libro3 = Libro("El gran Gatsby", "Francis Scott", 1925)
libro4 = Libro("El Discurso del método", "René Descartes", 1637)

biblioteca.append(libro1)
biblioteca.append(libro2)
biblioteca.append(libro3)
biblioteca.append(libro4)

### Ver todos los libros de la biblioteca
print("El catálogo de libros de la biblioteca es el siguiente:")
for libro in biblioteca:
    print(f"- {libro.titulo_libro()}")


# Opcion 1 (infinitos intentos de introducir nombre del libro en caso de error):

while True:
    titulo = input("Introduzca título del libro: ")
    encontrado = False

    for libro in biblioteca:
        if libro.titulo_libro() == titulo:
            encontrado = True
            print("Seleccione una opción 1, 2 o 3: ")
            print("1. Llevarse un libro")
            print("2. Devolver un libro")
            print("3. Consultar información de un libro")

            opcion = int(input())

            if opcion == 1:
                    print(libro.prestar())

            elif opcion == 2:
                    print(libro.devolver())

            elif opcion == 3:
                print(libro.informacion())
        
            else:
                print("Opcion no válida. Intente nuevamente.")

    if encontrado == False:
        print(f"El libro con título '{titulo}' no se encuentra en la biblioteca")

    continuar = input("¿Desea realizar otra operación? (si/no)")
    if continuar.lower() != "si":
        print("Gracias por usar esta biblioteca, ¡vuelva pronto!")
        break

# Opción 2 (un intento de introducir el titulo del libro en caso de error):
"""
titulo = input("Introduzca título del libro: ")
libro_encontrado = None # None es para dejar la variable creada sin valor

for libro in biblioteca:
        if libro.titulo_libro() == titulo:
            libro_encontrado = libro
            break

if libro_encontrado is not None:
    print("Seleccione una opción 1, 2 o 3: ")
    print("1. Llevarse un libro")
    print("2. Devolver un libro")
    print("3. Consultar información de un libro")

    opcion = int(input())

    if opcion == 1:
            print(libro_encontrado.prestar())

    elif opcion == 2:
            print(libro_encontrado.devolver())

    elif opcion == 3:
            print(libro_encontrado.informacion())   
    else:
        print("Opcion no válida.")

if libro_encontrado is None:
    print(f"El libro con título '{titulo}' no se encuentra en la biblioteca")
"""
# Opción 3 (con excepciones):
"""
titulo = input("Introduzca título del libro: ")
try: 
    for libro in biblioteca:
        if libro.titulo_libro() == titulo:
            libro_encontrado = libro
            break
    libro_encontrado == titulo
except:
    print(f"El libro con título '{titulo}' no se encuentra en la biblioteca")
else:
    print("Seleccione una opción 1, 2 o 3: ")
    print("1. Llevarse un libro")
    print("2. Devolver un libro")
    print("3. Consultar información de un libro") 

    opcion = int(input())

    if opcion == 1:
            print(libro_encontrado.prestar())

    elif opcion == 2:
            print(libro_encontrado.devolver())

    elif opcion == 3:
            print(libro_encontrado.informacion())
   
    else:
        print("Opcion no válida.")
finally:
    print("Gracias por usar esta biblioteca, ¡vuelva pronto!")
"""