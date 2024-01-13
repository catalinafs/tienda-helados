Menu = '''
Elige la opcion que deseas realizar:

 1- Agregar al carrito
 2- Ver el carrito
 3- Salir

'''

sabores = ['Fresa', 'Chocolate', 'Vainilla', 'Mango', 'Maracuya']

def menu_sabores():
    for sabor in sabores:
        print(f'{sabor}')

def imprimir_carrito(helados):
    for helado in helados:
        print(f'Helado de {helado}')

carrito = []

while True:
    opcion = int(input(Menu))
    
    match opcion:
        case 1:
            print('Elige el producto que deseas agregar al carrito:\n')
            menu_sabores()
            helado = str(input(''))

            carrito.append(helado)
        case 2:
            print("--------------------------------------------------")
            imprimir_carrito(carrito)
            print('')
        case 3:
            print("Hasta la proxima")
            break
        case _:
            print("Mala respuesta")
            break