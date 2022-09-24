import os
import random
os.system("cls")

def run():
        with open("C://Users/a842665/Platzi/python_intermedio/data.txt","r", encoding="utf-8")as f:
            data=[]
            for i in f:
                data.append(str(i))
        data1=[list(enumerate(data,start=1))]
        print(data1)

    # a=1
    # b=10
    # rndm=int(random.uniform(1,10))
    # x=list.get(rndm)
   

if __name__=="__main__":
    print("Welcome to the HANGMAN game")
    run()


