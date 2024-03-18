# Creación de un programa básico de gestión de inventario.
# Desarrollar un programa en Python que permita gestionar un inventario simple de
# productos, incluyendo funciones básicas como agregar productos, eliminar productos y
# mostrar el inventario.
# El programa debe tener un menú interactivo que permita al usuario seleccionar las
# siguientes operaciones:
#     - Agregar un nuevo producto al inventario, solicitando al usuario el nombre y la cantidad
#       inicial del producto.
#     - Eliminar un producto existente del inventario, solicitando al usuario el nombre del
#       producto a eliminar.
#     - Mostrar el inventario actual, que incluya el nombre y la cantidad de cada producto.
#       Salir del programa.
# El inventario puede ser almacenado utilizando un diccionario simple, donde las claves sean
# los nombres de los productos y los valores sean las cantidades.
# Se deben manejar situaciones simples como la introducción de productos duplicados o la
# eliminación de productos inexistentes.
def MenuOpciones():
    print()
    print('------ Menu de Opciones ------')
    print('1- Agregar un producto') 
    print('2- Eliminar un producto')
    print('3- Imprimir Inventario')
    print('4- Salir')
    return int(input('Ingrese una opcion: '))

def AgregarProducto(productos):
    print()
    print('------ Se agregara un producto al inventario ------')
    nom = input('Ingrese el nombre del producto: ')
    if nom in productos:
        print('!!!!!!! El producto ya existe !!!!!!')
    else:
        cant = int(input('Ingrese la cantidad del producto: '))
        productos[nom] = cant
        print(f'------ Se agrego {nom} con exito ------')

def EliminarProducto(productos):
    print()
    print('------ Se eliminara un producto al inventario ------')
    nom = input('Ingrese el nombre del producto:')
    if nom in productos:
        del productos[nom] 
        print(f'------ Se elimino {nom} con exito ------')
    else:
        print('!!!!!!! El producto no existe !!!!!!')

def MostrarInventario(productos):
    print()
    print('------ Se mostrara el inventario ------')
    if (len(productos) != 0):
        for nom,cant in productos.items():
            print(f'- Producto : {nom} \n- Cantidad : {cant}')
    else:
        print('EL inventario no tiene productos.')


productos = {}
opcion = MenuOpciones()

while (opcion != 4):
    if (opcion == 1) : AgregarProducto(productos)
    elif (opcion == 2) : EliminarProducto(productos)
    elif (opcion == 3 ): MostrarInventario(productos)
    else : print('------ La opcion Ingresada no es valida ------')
    opcion = MenuOpciones()

