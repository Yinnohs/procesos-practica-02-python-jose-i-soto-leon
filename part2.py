from subprocess import run as runProcess
from platform import system

if __name__ == "__main__":
    os = system()
    if  os == "Windows":
        process = runProcess(["ping www.google.com"],check=True,shell=True)
    else:
        process = runProcess(["ping www.google.com -c 4",],shell=True)
        
 
        