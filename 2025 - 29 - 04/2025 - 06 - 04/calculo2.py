from os import system

a = int(input("Digite a distancia (K): "))
if a <= 0:
  system.exit("informe uma distancia positiva.")

b = int(input("velocidade inicial: "))
if b <= 0:
  system.exit("informe uma velocidade positiva.")

c = int(input("Aceleração: "))
if c <= 0:
  system.exit("informe uma aceleração positiva.")

d =  a * b + (c * b**2)/2