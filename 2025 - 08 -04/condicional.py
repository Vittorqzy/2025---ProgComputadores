
import sys

etapa1 = int(input('informe a nota da etapa 1 (0-100): '))
if etapa1 < 0 or etapa1 > 100:
  sys.exit('ERROR: NOTA ETAPA 1 INVALIDA')


etapa2 = int(input('informe a nota da etapa 2 (0-100): '))
if etapa2 < 0 or etapa1 > 100:
  sys.exit('ERROR: NOTA ETAPA 1 INVALIDA')

media = int(round( (etapa1 * 2 + etapa2 *3) / 5, 0))
print(f'Media do aluno: {media}')
#print(f'Media do aluno(arredondada): {media:.0f}')

if media >= 60:
  print('Aprovado')
elif media <= 20:
  print('Prova final')
else:
  print('Reprovado')
