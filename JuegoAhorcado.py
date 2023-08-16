import random
import os






if __name__=='__main__':
    frutas=["banana","fresa","limon","melon"]
    palabra=random.choice(frutas)
    resp=["_"]*len(palabra)
    vidas=4

    while True:
        os.system("cls")
        print("Adivina la fruta, te quedan ",vidas+1," intentos\n")
        for char in resp:
            print(char,end=" ")
        print ("\n")
        letra=input("ingresa una letra ").lower
        
        acierto= False
        for i, char in enumerate(palabra):
            if char ==letra:
                resp[i]=letra
                acierto=True

        if not acierto:
            vidas-=1

        if "_" not in resp:
            os.system("cls")
            print("La Palabra es: ",resp)
            print("\n -----FELICITACIONES HAS GANADO---------")
            break
            input()
            

        if vidas==0:
            os.system("cls")
            print("\n -----Perdiste--------")
            break
            input
            