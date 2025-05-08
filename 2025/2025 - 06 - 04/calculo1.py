# delta = b² - 4ac#
from os import system

a = int(input("Digite a velocidade inicial (m/s): "))
if a <= 0:
  system.exit("informe uma velocidade positiva.")

b = int(input("Tempo em segundos: "))
if b <= 0:
  system.exit("informe um tempo positivo.")

c = int(input("Aceleração: "))
if c <= 0:
  system.exit("informe uma aceleração positiva.")

#delta =  b**2 - 4*a*c
deltaS =  a * b + (c * b**2)/2
print(f"Distancia percorrida:, {deltaS}, metros")
