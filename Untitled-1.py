import os
import time

segundos = 10

print('BIENVENIDO')

desicion = input('''
Quieres jugar un juego?
S para si y N para no --> ''').lower()

if desicion == 's':
        print('Comenzamos en...')
        for i in range(0,segundos):
                print(' ')
                print(f'Segundos: {segundos}')
                time.sleep(1)
                os.system('cls')
                segundos -= 1
else:
        print('Aburrid@ :(')


