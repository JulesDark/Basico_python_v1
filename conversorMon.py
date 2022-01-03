menu = """
Bienvenido al conversor de monedas de python by jules
1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos 
Elige una opcion :
"""
op = int(input(menu))

if op == 1:
    pesos = input("cuantos pesos colombianos tenes : ")
    pesos = float(pesos) #convierte los pesos a numero
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2) #Le deja solo dos numeros decimales al nuestro resultado
    dolares = str (dolares)
    print("tienes $"+ dolares + " dolares" )

elif op == 2:
    pesos = input("cuantos pesos Argentinos tenes : ")
    pesos = float(pesos) #convierte los pesos a numero
    valor_dolar = 65
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2) 
    dolares = str (dolares)
    print("tienes $"+ dolares + " dolares" )
elif op == 3:
    pesos = input("cuantos pesos Mexicanos tenes : ")
    pesos = float(pesos) #convierte los pesos a numero
    valor_dolar = 24
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2) 
    dolares = str (dolares)
    print("tienes $"+ dolares + " dolares" )
else:
    print("ingresa una opcion correcta porfavor")

