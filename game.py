class juego():
    def init(self, nombre,precio) :

        self.nombre=nombre
        self.precio=precio
        self.status="EN STOCK"



        pass


print(""" ---------------------- HOLA BIENVIDO A LA TIENDA Rent - A - Game ----------------------------

INSETAR NUEVOS JUEGOS A LA TIENDA/ EN ESTE PROGRAMA PODRAS ALQUILAR JUEGOS/ DEVOLVER JUEGOS""")
victoria=[]


while (True):
    print("Ingrese la opcion que desea realizar")


    hola=input("""    
    (1)INSERTAR JUEGO
    (2)ALQUILAR JUEGO
    (3)DEVOLVER JUEGO
    (4)SALIR
    ====>""")
    while hola!="1" and hola!="2" and hola!="3" and hola!="4":
        hola=input("""    
                (1)INSERTAR JUEGO
                (2)ALQUILAR JUEGO
                (3)DEVOLVER JUEGO
                (4)SALIR
                ====>""")

    if int(hola) == 1:

        print("INSERCION DE JUEGOS")

        nombre=input("Di el nombre del juego, debe de tener 6 letras y 2 digitos (EJEMPLO: SPACEI23):  " )

        while   nombre[5].isnumeric()==False and nombre[6].isnumeric()==False :
                nombre=input("""Di el nombre del juego, debe de tener 6 letras y 2 digitos (EJEMPLO: SPACEI23)
            ====>""")


        precio=input("Di el precio del juego: ")

        while precio.isnumeric()==False:
            precio=input("Di el precio del juego: ")


        game= juego(nombre,precio)

        victoria.append(game)

    elif int(hola) == 2:
        print("hola2")

    elif int(hola)==3:
        print ("hola3")
    elif int(hola) == 4:
        print(len(victoria))
        break