
palabra = "El programa correra hasta que escriba (salir)"
print(palabra)

# aqui coloque palabra para que no mediera error el codigo la verdad no se porque me daba error el codigo jaskjs :v pero ya con esto como que ya conoce la 
## la variable palabra y ya no bota error ksajlsa 

x = 3

def run(palabra):
    while palabra != "salir":
        palabra = input("Escribe una palabra : ")
        palabra = palabra.replace(" ","").lower()
        palabra2 = palabra[::-1]
        if palabra == palabra2:
            print("Es palindromo")
        elif palabra == "salir":
            print("adios boludo <3".capitalize()) 
        else:
            print("No es palindromo")
         

if __name__ == '__main__':
    run(palabra)