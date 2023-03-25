def hash_function(name):
    suma = 0
    for character in name:
        suma += ord(character)
    return suma % 3


print(hash_function("hola"))
