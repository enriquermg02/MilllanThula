def hash_function(name):
    suma = 0
    for character in name:
        suma += ord(character)
    return suma % 3


class juego():
    def init(self, modelo, titulo, precio):

        self.modelo = modelo
        self.titulo = titulo
        self.precio = precio
        self.status = "EN STOCK"

        pass


print(""" ---------------------- HOLA BIENVENIDO A LA TIENDA Rent - A - Game ----------------------------

INSETAR NUEVOS JUEGOS A LA TIENDA/ EN ESTE PROGRAMA PODRAS ALQUILAR JUEGOS/ DEVOLVER JUEGOS""")
victoria = []

while (True):
    print("Ingrese la opcion que desea realizar")

    opcion = input("""    
    (1)INSERTAR JUEGO
    (2)ALQUILAR JUEGO
    (3)DEVOLVER JUEGO
    (4)SALIR
    ====>""")
    while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4":
        opcion = input("""    
                (1)INSERTAR JUEGO
                (2)ALQUILAR JUEGO
                (3)DEVOLVER JUEGO
                (4)SALIR
                ====>""")

    if int(opcion) == 1:

        print("INSERCION DE JUEGOS")

        modelo = input(
            "Di el modelo del juego, debe de tener 6 letras y 2 digitos (EJEMPLO: SPACEI23):  ")

        while modelo[-1].isnumeric() == False and modelo[-2].isnumeric() == False:
            modelo = input("""Di el modelo del juego, debe de tener 6 letras y 2 digitos (EJEMPLO: SPACEI23)
            ====>""")

        titulo = input(
            "Di el titulo del juego, debe tener maximo 10 caracteres: ")
        while len(titulo) > 10:
            input("Di el titulo del juego: ")

        precio = input("Di el precio del juego: ")

        while precio.isnumeric() == False or (int(precio) > 999):
            precio = input("Di el precio del juego: ")

        game = juego(modelo, titulo, precio)

        victoria.append(game)

    elif int(opcion) == 2:
        print("opcion2")

    elif int(opcion) == 3:
        print("opcion3")
    elif int(opcion) == 4:
        print(len(victoria))
        break
