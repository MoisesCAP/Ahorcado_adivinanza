import os
import time
import random

def ahorcado():
    print('ADIVINA EL MES DEL AÑO (EN INGLES) QUE ESCOGIO LA PC...')
    meses = ['january','february','march','april','may','june','july',
    'august','september','october','november','december']

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
    print('''
    Piensa en un numero del 1 al 30 el cual la 
    computadora tiene que adivinar!

            REGLAS 
    -> Para indicar que el numero es mas BAJO, oprime "z"
    -> Para indicar que el numero es mas ALTO, oprime "m"
    -> Si la computadora adivino el numero, oprime "g"
    ''')
    print('...')
    time.sleep(7)

    bajo = 1
    alto = 30

    while True:

        numero_alea = random.randint(bajo,alto) # la pc escoge un numero
        print() 
        print(f'El numero que pensaste es: {numero_alea}?')

        print()
        usuario = input('z, m, g --> ').lower()

        print()

        if usuario == 'z':
            alto = numero_alea - 1 #Ej: la pc escogio 25, pero el numero a adivinar es mas bajo, 
            # se le resta -1, ahora la pc escogera del 24 para abajo, porque ya se sabe quue del 
            # 25 para arriba no esta el numero a adivinar 

        elif usuario == 'm':
            bajo = numero_alea + 1 # De estas dos formas se ira modificando el rango, + , - 

        elif usuario == 'g':
            print('Fin del juego!')
            break

        else:
            print('Esa operacion no se encuentra disponible')
            break
        

def datos(desicion):
    segundos = 3

    print(' ')
    nombre = input('Cual es tu nombre? -> ').upper()
    print(' ')

    print('Comenzamos en...')
    for i in range(0,segundos):
            print(' ')
            print(f'Segundos: {segundos}')
            time.sleep(1)
            os.system('cls')
            segundos -= 1

    if desicion == 'a':
        print(f'BIENVENIDO {nombre}')
        adivinanza()
    else:
        print(f'BIENVENIDO AL JUEGO DEL AHORCADO {nombre}')
        ahorcado()


def run():
    
    desicion = input('''
    Quieres jugar el ahorcado o gustas hacer una
    pequeña adivinanza de un numero?
    H para el ahorcado y A para el otro --> ''').lower()
    
    if desicion == 'h' or desicion == 'a':
        datos(desicion)
    else:
        print('Esa letra no esta disponible')

  
if __name__ == '__main__':
    print('BIENVENIDO!')
    run()


