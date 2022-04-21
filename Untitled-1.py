import os
import time

segundos = 10

print('BIENVENIDO')
for i in range(0,segundos):
        print(' ')
        print(f'Segundos: {segundos}')
        time.sleep(1)
        os.system('cls')
        segundos -= 1
print('olo')

os.system('notepad.exe')

