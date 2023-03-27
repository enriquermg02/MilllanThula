import json


def hash_function(name):
    suma = 0
    for character in name:
        suma += ord(character)
    return suma % 3


class juego():
    def __init__(self, modelo, titulo, precio, status="EN STOCK"):
        self.modelo = modelo
        self.titulo = titulo
        self.precio = precio
        self.status = "EN STOCK"

    def to_dict(self):
        return {
            "modelo": self.modelo,
            "titulo": self.titulo,
            "precio": self.precio,
            "status": self.status
        }

        pass


def insertar_overflow(overflow, juego):

    aux = 0
    for n in overflow:
        if len(n) != 3:
            overflow[aux].append(juego)
            break

        aux += 1

    return overflow

# [[{"course": "python", "fee": 4000}], [{"duration": "60days", "discount": 1200}]]


print(""" ---------------------- HOLA BIENVENIDO A LA TIENDA Rent - A - Game ----------------------------
INSETAR NUEVOS JUEGOS A LA TIENDA/ EN ESTE PROGRAMA PODRAS ALQUILAR JUEGOS/ DEVOLVER JUEGOS""")

lista = [[], [], []]
overflow = [[], [], [], [], [], []]

with open("storage.json", "r") as f:
    # if f.read(2) == null:
    #     f.seek(0)  # it may be redundant but it does not hurt
    data = json.load(f)

    dicc_juegos = data["lista"]
    dicc_overflow = data["overflow"]

    for k, v in dicc_juegos.items():
        numero = hash_function(k)
        juego_actual = juego(v["modelo"], v["titulo"],
                             v["precio"], v["status"])

        lista[numero].append(juego_actual)

    for k, v in dicc_overflow.items():
        juego_actual = juego(v["modelo"], v["titulo"],
                             v["precio"], v["status"])

        overflow.append(juego_actual)


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

        numero = hash_function(modelo)

        if len(lista[numero]) >= 3:
            overflow = insertar_overflow(overflow, game)

        else:
            lista[numero].append(game)

    elif int(opcion) == 2:
        print("ALQUILAR JUEGO")

        buscar = input(
            "Indique el modelo del juego que deasea Alquilar. Se le sera indiquaco si esta disponible o no.")

        numero = hash_function(buscar)
        # aqui lo que haces es buscar si el juego esta en la lista hash, si esta se alquila y se quita el juego, si no pasamos al else
        if len(lista[numero]) != 0:
            for n in lista[numero]:
                if n.modelo == buscar:
                    lista[numero].remove(n)
                    print("USTED HA ALQUILADO UN JUEGO\n")
                    break
        else:
            # aqui se supone que el overflow es el almacen, y se busca en el overflow, si no se encuentra decimos que no existe el juego

            print("No tenemos juegos en stock. Desea buscar en almacen ")
            opcion = input("(1)SI\n(2)NO")
            if opcion == "1":
                print("oks")

    elif int(opcion) == 3:
        print("opcion3")

    elif int(opcion) == 4:
        json_lista = {}
        json_overflow = {}

        for juegos in lista:
            for j in juegos:
                json_lista[j.modelo] = j.to_dict()

        for juegos in overflow:
            for j in juegos:
                json_overflow[j.modelo] = j.to_dict()

        print(json_lista)

        storage = {
            "lista": json_lista,
            "overflow": json_overflow
        }

        with open('storage.json', 'w') as fp:
            json.dump(storage, fp, indent=4)

        break
