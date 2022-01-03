def run():
    mi_diccionario = {
        "llave1" : 1,
        "llave2" : 2,
        "llave3" : 3,

    }
    print("Keys de el primer diciionario")
    print(mi_diccionario["llave1"]) # imprime el valor de la llave 1
    print(mi_diccionario["llave2"]) #imprime el valor de la llave 2

    poblacion_paises =  {
        "Argentina" : 45655465,
        "Mexico"    : 454654,
        "Colombia"  : 587987,
    }
    print("keys de el dicionario de paises")
    for pais in poblacion_paises.keys():
        print(pais)
    #imprime la key y la trata como si fuera la variable pais


    print("valores de las keys del diccionario 2 de el dicionario de paises")
    for pais1 in poblacion_paises.values():
        print(pais1)
    #creo otra varaible y sera el valor de cada una de las keys




    print("los dos items del diccionario 2")
    for pais3, poblacion in poblacion_paises.items():
        print(pais3 + " tiene " + str(poblacion) )
    #imprime los dos items con el metodo items uno se llama pais y el otr
    #llama poblacion sera como cuando defino parametros en una funcion.

if __name__ == "__main__":
    run()
