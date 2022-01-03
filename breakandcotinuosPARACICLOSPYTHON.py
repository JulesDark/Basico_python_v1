def run():
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)

    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break

    # texto = input("escribe un texto : ")
    # for letra in texto:
    #     if letra == "o":
    #         break
    #     print(letra)


    x = 1
    limite = int(input("Escribe un limite : "))
    while(x <= limite):
        print(x)
        x += 1
        if x == 1545:
            break
    


if __name__== "__main__":
    run()