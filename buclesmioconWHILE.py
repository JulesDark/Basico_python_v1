x =  int(input("introduce un numero : "))

def run():
    contador = 1 
    while(contador <= x):
        print("2 elevado a " + str(contador) + " es igual a : " + str(2**contador)) 
        contador = contador + 1

if __name__ == "__main__":
    run()