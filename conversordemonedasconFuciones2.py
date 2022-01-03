menu = """
Bienvenido al conversor de monedas de python by jules
1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos 
Elige una opcion :
"""
op = int(input(menu))

def conversor(x):
    pesos = input("cuantos pesos colombianos tenes : ")
    pesos = float(pesos) #convierte los pesos a numero
    valor_dolar = (x)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2) #Le deja solo dos numeros decimales al nuestro resultado
    dolares = str (dolares)
    print("tienes $"+ dolares + " dolares" )

if op == 1:
    conversor(3800)
elif op == 2:
    conversor(70)
elif op == 3:
   conversor(24)
else:
    print("ingresa una opcion correcta porfavor")