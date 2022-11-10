from multiprocessing import Process
from time import sleep
import os

def processFunctionality():
    print('Empezando el Proceso (%s)...' % ( os.getpid()))
    sleep(5)
    print("Se acaba la ejecucion del proceso " + str(os.getpid()))
    os._exit(0)
    



if __name__ == "__main__":
    userInput =  int(input("Cuantos processos hijos debe de tener ? "))
    print('Proceso padre %s.' % os.getpid())
    for i in range (userInput):
        p = Process(target=processFunctionality, args=('test',))
        p.start()

