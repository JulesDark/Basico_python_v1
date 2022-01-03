import random

def run():
    x = int(input("Adivina un numero del 1 al 100 tienes 5 intentos : "))
    i = random.randint(1, 100)
    v = 5
    print(i)
    
    while(x != i and v > 0):
        if x < i:
            print("El numero es mayor escoje otro, tienes " + str(v)+ " vidas" )
            x = int(input(":"))
            v = v - 1
        elif x > i:
            print("El numero es menor escoje otro, tienes " + str(v)+ " vidas") 
            x = int(input(":"))
            v = v - 1
                
        
    if(x == i):
        print("Ganaste tu numero era " + str(i) + " Felicidades")
    if(v == 0 and x != i):
        print("Perdiste el numero era " + str(i))
    
    
if __name__== "__main__":
    run()