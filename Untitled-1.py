import os
import time
import random

def adivinanza():
        
    vidas = 6
    print(f'Tienes {vidas} vidas')
    print(' ')
    print('Tienes que adivinar el numero que escogio la computadora')
    numero_escogido = int(input('Ingresa un numero del 1 al 50: '))
    numero_aleatorio = random.randint(1, 50)
  
    while numero_escogido != numero_aleatorio and vidas >= 2:

        if numero_escogido < numero_aleatorio:
            print('Escoge un numero mas grande')
            print('---------------------------------')
            
        else:
            print('Escoge un numero mas pequeño')
            print('---------------------------------')
        vidas -= 1
        print(f'VIDAS = {vidas}')
            
        numero_escogido = int(input('Escoge otro numero: '))
        print(' ')
        
    if numero_escogido == numero_aleatorio:
        print('¡Ganaste!')
    else:
        print('Te quedaste sin vidas :(')
        print('Suerte para la proxima')
        print(' ')
        
        
def run():
    segundos = 5

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
        adivinanza()
    else:
        print('Aburrid@ :(')
    

if __name__ == '__main__':
    run()


    
