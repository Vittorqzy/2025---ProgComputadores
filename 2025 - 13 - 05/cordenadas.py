try:
    # Solicitar as coordenadas do ponto
    coordX = float(input('Digite a coordenada X: '))
    coordY = float(input('Digite a coordenada Y: '))

    # Verificar em qual quadrante o ponto está
    if coordX > 0 and coordY > 0:
        print('O ponto está no 1º quadrante.')
    elif coordX < 0 and coordY > 0:
        print('O ponto está no 2º quadrante.')
    elif coordX < 0 and coordY < 0:
        print('O ponto está no 3º quadrante.')
    elif coordX > 0 and coordY < 0:
        print('O ponto está no 4º quadrante.')
    else:
        print('O ponto está na origem ou nos eixos coordenados.')
except ValueError:
    print("Erro: Por favor, insira números válidos para as coordenadas.")