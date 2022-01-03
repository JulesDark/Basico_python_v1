z = input("Introduce el texto a convertir : ")


s = int(input("""A que formato deseas convertirlo
1 - Mayus
2 - Minusculas
3 - Capitalizado
4 - Al reves
5 - salir
: """))

if  s == 1:
    print(z.upper())        
elif s == 2:
    print(str(z.lower()))
elif s == 3:
    print(str(z.capitalize()))
elif s == 4:
    print(z[::-1])
else:
    print("no has introducido una opcion correcta")



        