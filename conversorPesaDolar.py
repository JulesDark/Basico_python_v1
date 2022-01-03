dolares = input("Cuantos dolares tenes: ")
dolares = float(dolares) #convierte los pesos a numero
valor_dolar = 3875
pesos = dolares * valor_dolar
pesos = round(pesos, 2) #Le deja solo dos numeros decimales al nuestro resultado
pesos = str (pesos)
print("tienes $"+ pesos + " pesos Colombianos" )