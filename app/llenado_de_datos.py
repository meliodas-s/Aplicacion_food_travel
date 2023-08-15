# Crear nuevo destino culinario
from models.modelo__ubicacion import Ubicacion
from models.modelo__actividad import Actividad
import json
from models.modelo__destino_culinario import DestinoCulinario

# Consola
print('Importar modulo de destino culinario: Ok')

# Creando destinos
lista_destinos_debug = [
    {
        "nombre": "El Buen Gusto",
        "imagen": "image_1.png",
        "id_ubicacion": 1
    },
    {
        "nombre": "La Monumental",
        "imagen": "image_2.png",
        "id_ubicacion": 2
    },
    {
        "nombre": "La 12",
        "imagen": "image_3.png",
        "id_ubicacion": 3
    },
    {
        "nombre": "Donatello",
        "imagen": "image_4.png",
        "id_ubicacion": 4
    },
    {
        "nombre": "Lo del Negro Copa",
        "imagen": "image_5.png",
        "id_ubicacion": 5
    },
    {
        "nombre": "Pizza Mara",
        "imagen": "image_6.png",
        "id_ubicacion": 6
    }
]

lista_destinos = []
for i,destino in enumerate(lista_destinos_debug):
    destino_culinario = DestinoCulinario(
        destino['nombre'], 'Tipo de cocina', ['sal', 'sal'], 10, 100, 5, destino['id_ubicacion'], destino['imagen'], i+1)
    lista_destinos.append(destino_culinario)

# Consola
print('Crear destino culinario: Ok')

# Verificamos el guardado de datos
archivo = 'data/destinos_culinarios.json'
DestinoCulinario.guardar_datos(archivo, lista_destinos)
print('Guardado de nuevo JSON: Ok')

#
print()

# Creando ubicaciones
lista_ubicaciones_debug = [
    {
        "id": 1,
        "latitud": -24.7761,
        "longitud": -65.4093,
        "direccion": "O'Higgins 575"
    },
    {
        "id": 2,
        "latitud": -24.7778,
        "longitud": -65.4114,
        "direccion": "Balcarce 999"
    },
    {
        "id": 3,
        "latitud": -24.7746,
        "longitud": -65.4117,
        "direccion": "12 de Octubre 756"
    },
    {
        "id": 4,
        "latitud": -24.7763,
        "longitud": -65.4096,
        "direccion": "Bartolomé Mitre 1086"
    },
    {
        "id": 5,
        "latitud": -24.7750,
        "longitud": -65.4092,
        "direccion": "12 de Octubre 581"
    },
    {
        "id": 6,
        "latitud": -24.7758,
        "longitud": -65.4138,
        "direccion": "O'Higgins 903"
    }
]
lista_ubicaciones = []
for i,ubicacion in enumerate(lista_ubicaciones_debug):
    ubicacion_debug = Ubicacion(ubicacion['direccion'], [
                                ubicacion['latitud'], ubicacion['longitud']],i+1)
    lista_ubicaciones.append(ubicacion_debug)

# Verificamos el guardado de datos
archivo = 'data/ubicacion.json'
Ubicacion.guardar_datos(archivo, lista_ubicaciones)
print('Guardado de nuevo JSON: Ok')

# Arregla problema del id, si creo una lista de objetosId y los guardo a todos
# juntos todos se guardan con el mismo id.
# Solucion 1: Cada vez que se cree un objetoId se debe guardar
# solucion 2: Si se gurda una lista con objetos debe ir creandose id por id
#     a medida que se vallan guardando los objetos. Pero siempre que se cree uno
#     se debera verificar cual es el ultimo id y ese la desventaja de esta solucion.
#       No debe haber problema por ahora, ya que el programa esta hecho para crear
#     los destinos de a uno y no introducir dos destinos a la ves