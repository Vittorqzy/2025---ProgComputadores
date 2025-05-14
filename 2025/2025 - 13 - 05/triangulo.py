import sys

try:
    # Solicitar os ângulos do triângulo
    a1 = int(input('Digite um Ângulo inteiro positivo: '))
    a2 = int(input('Digite um Ângulo inteiro positivo: '))
    a3 = int(input('Digite um Ângulo inteiro positivo: '))
    soma = a1 + a2 + a3 

    # Verificar se os ângulos são positivos
    if (a1 <= 0) or (a2 <= 0) or (a3 <= 0):
        sys.exit('ERROR: os valores não são positivos')

    # Verificar se a soma dos ângulos é igual a 180
    if soma != 180:
        sys.exit('ERROR: os valores não formam um triângulo')
    else:
        # Identificar o tipo de triângulo
        if a1 == 90 or a2 == 90 or a3 == 90:
            print('TRIÂNGULO RETÂNGULO')
        elif a1 > 90 or a2 > 90 or a3 > 90:
            print('TRIÂNGULO OBTUSÂNGULO')
        else:
            print('TRIÂNGULO ACUTÂNGULO')
except ValueError:
    print("Erro: Por favor, insira apenas valores inteiros positivos.")