import random

mi_dic = {
    "lla1": random.randint(4, 98974),
    "ll2" : 3,
    "lla3" : 4,
    "lla4" : 5,
}

asd = [3,2,4,5,6,7,9,8,1,2,6,4]   


def main(x):
    if x < mi_dic["lla1"]:
        print(" el condigo se imprimira " + str(mi_dic["lla1"]) + " veces")
        
        print(list("Upper" * mi_dic["lla1"]))
    else:
        print("Else")



if __name__ == "__main__":
    main(4)







