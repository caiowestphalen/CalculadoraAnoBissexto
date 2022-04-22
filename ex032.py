# Programa que vai calcular se o ano é ou foi bissexto.

from time import sleep
from datetime import date
print('\033[0;0;36m-=\033[m'*20)
print('\033[0;0;32mCalculadora de ano bissexto.\n Digite 0 (zero) para utilizar o ano atual.\033[m')
print('\033[0;0;36m-=\033[m'*20)
ano = int(input('Digite um ano com os 4 digitos: '))
print('\033[0;0;34mCalculando...\033[m')
sleep(1)
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print('O ano \033[1;0;0m{}\033[m é \033[0;0;35mBISSEXTO\033[m!'.format(ano))
else:
    print('O ano \033[1;0;0m{}\033[m \033[0;0;33mNÃO É BISSEXTO\033[m!'.format(ano))

#

