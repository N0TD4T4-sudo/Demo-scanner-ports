import socket
import time
try:
    Ps = int(input("Puerto de inicio \n "))
    Pe = int(input("Puerto final \n"))
except ValueError:
    raise ValueError("Error eso no es un numero")
if Ps < 1 or Ps > Pe:
    raise ValueError ("El Valor de inicio no esta dentro de los limites")
elif Pe < Ps or Pe > 65535:
    raise ValueError ("El valor no se encuentra dentro de los limites")
A = time.time()
Encontro = False
for n in range(Ps,Pe+1):
    s = socket.socket()
    s.settimeout(0.5)
    Resultconex = s.connect_ex(("127.0.0.1", n))
    if Resultconex == 0:    
        print(f"El Puerto {n} esta abierto")
        Encontro = True
    s.close()
if not Encontro:
    print("no se encontro puerto")
B= time.time()
print(B-A, Encontro ,) 