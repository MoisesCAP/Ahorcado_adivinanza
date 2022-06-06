import os
import time
import random

def ahorcado():

    meses = ['enero','febrero','marzo','abril','mayo','junio','julio',
    'agosto','septiembre','octubre','noviembre','diciembre']

    palabra_aleatoria = random.choice(meses)
    
    espacios = ['_'] * len(palabra_aleatoria)
    lista_letras = ''

    vidas = 5 
    print(f'Tienes {vidas} vidas en total')

    while True:

        for i in espacios:
            print(i,end=' ')

        print(' ')
        print(' ')

        letra_usuario = input('Ingresa una letra: ')
        
        for numero, valor in enumerate(palabra_aleatoria):
            if valor == letra_usuario:
                espacios[numero] = letra_usuario

        if letra_usuario not in palabra_aleatoria:
            if vidas == 1:
                print('Vidas = 0, Suerte para la proxima!')
                break
            else:
                print(' ')
                print('---> No se encuentra <---')
                vidas -= 1
                print(f'Te quedan {vidas} vidas')
                print(' ')
        
        if '_' not in espacios:
            print('GANASTE!')
            break


def adivinanza():
        
    vidas = 7

    print('Adivina el numero que escogio la computadora...')
    print(f'Tienes {vidas} vidas')
    print(' ')
    numero_escogido = int(input('Ingresa un numero del 1 al 50: '))
    numero_aleatorio = random.randint(1, 50)
    print(' ')
  
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
        

def datos():
    segundos = 5

    print(' ')
    nombre = input('Cual es tu nombre? -> ')
    edad = int(input(f'Que edad tienes {nombre}? -> '))
    nombre = nombre.upper()
    print(' ')

    print('Comenzamos en...')
    for i in range(0,segundos):
            print(' ')
            print(f'Segundos: {segundos}')
            time.sleep(1)
            os.system('cls')
            segundos -= 1

    if edad <= 12:
        print(f'BIENVENIDO {nombre}')
        adivinanza()
    else:
        print(f'BIENVENIDO AL JUEGO DEL AHORCADO {nombre}')
        ahorcado()


def run():
    
    desicion = input('''
    Quieres jugar un juego?
    S para si y N para no --> ''').lower()
    
    if desicion == 's':
        datos()
    else:
        print('Aburrid@ :(')

  
if __name__ == '__main__':
    print('BIENVENIDO!')
    run()


