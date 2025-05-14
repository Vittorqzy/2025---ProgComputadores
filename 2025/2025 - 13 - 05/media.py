try:

    etapa1 = int(input('Informe a nota da Etapa 1: '))
    if etapa1 < 0 or etapa1 > 100:
        raise ValueError('ERRO: Nota Etapa 1 Inválida. Informe nota entre 0 e 100.')

    etapa2 = int(input('Informe a nota da Etapa 2: '))
    if etapa2 < 0 or etapa2 > 100:
        raise ValueError('ERRO: Nota Etapa 2 Inválida. Informe nota entre 0 e 100.')

    media = int(round((etapa1 * 2 + etapa2 * 3) / 5, 0))
    print(f'Média do Aluno: {media}')

    if media >= 60:
        print('Aluno Aprovado.')
    elif media >= 20:
        print('Aluno em Prova Final.')
    else:
        print('Aluno Reprovado.')
except ValueError as e:
    print(e)
except Exception:
    print("ERRO: Ocorreu um erro inesperado. Tente novamente.")
