import sys


a1 = int(input('Digite um Ângulo inteiro positivo: '))
a2 = int(input('Digite um Ângulo inteiro positivo: '))
a3 = int(input('Digite um Ângulo inteiro positivo: '))
soma = a1 + a2 + a3 

if soma != 180 or a1 <= 0 or a2 <= 0 or a3 <=0:
    sys.exit('ERROR: os valores não formam um triangulo')
if soma == 180
else:
  if a1 == 90 or a2 == 90 or a3 == 90:
    print('TRIÂGULO RETÂNGULO')
  elif a1 > 90 or a2 > 90 or a3 > 90:
     print('TRIÂGULO OBTUSÂNGULO')
  else:
     print('TRIÂGULO ACUTÂNGULO')