'''
   Os primeiros dois números consecutivos que podem ser decompostos 
   como apenas dois fatores primos são 14 = (2 * 7) e 15 = (3 * 5).

   Faça um programa que recebe a quantidade n de fatores primos que 
   um número pode ter. 
   
   O programa deve listar os primeiros n números consecutivos que 
   atendem ao critério.
'''
import sys, math, time

try:
    intQtFatores = int(input('Digite a quantidade de fatores primos que um número pode ter: '))
except ValueError:
    sys.exit('ERRO: Informe um inteiro válido...')
except Exception as e:
    sys.exit(f'ERRO: {e}')
else:
    iniciot = time.time()
    n = 2
    while True:
        found = True
        for i in range(n, n + intQtFatores):
            contador = 0
            nAtual = i
            cFat = 2
            while cFat <= math.isqrt(nAtual):
                while nAtual % cFat == 0:
                    contador += 1
                    nAtual //= cFat
                cFat += 1
            # Se sobrou um fator primo maior que a raiz
            if nAtual > 1:
                contador += 1
            if contador != intQtFatores:
                found = False
                break
        if found:
            print(f'Os primeiros {intQtFatores} números consecutivos com {intQtFatores} fatores primos são: {list(range(n, n + intQtFatores))}')
            break
        n += 1
    fimt = time.time()
    print(f"Tempo decorrido: {fimt - iniciot:.2f} segundos")
