from multiprocessing import Process
from time import sleep
import os

if __name__ == "__main__":
    userInput =  int(input("Cuantos processos hijos debe de tener ? "))
    print('Proceso padre %s.' % os.getpid())
    for i in range (userInput):
        p = Process(target="some function", args=('test',))
        p.start()

