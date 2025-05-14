import sys

try:
  intDivsor =  int(input('Digite Divisor:'))
  intDividendo =  int(input('Digite Dividendo:'))
  intNum =  intDividendo / intDivsor
except ValueError:
  print(f'ERROR: Insira um valor que possa ser convertido para inteiro')
except ZeroDivisionError:
  print(f'ERROR: Divisão po ZERO')
except:
  print(f'ERROR : {sys.exc_info()}')
else:
  print(intNum)