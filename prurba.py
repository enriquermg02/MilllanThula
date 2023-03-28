
lista=[1,2,0,0]

def comprobarcero(lista,game,numero):

    if 0 in lista[numero]:
            numerovacio=lista[numero].index(0)
            
            lista[numero][numerovacio]=game



numero=1
game=2

hola=[[],[1,0,3]]

comprobarcero(hola,game,numero)


print(hola)
    


