# Crear nuevo destino culinario
from models.modelo__destino_culinario import DestinoCulinario

# Consola
print('Importar modulo de destino culinario: Ok')

# Creando destino y controlando id
destino_culinario_debug_1 = DestinoCulinario('Hola','Hola',['Hola','Hola'],21.2,21.2,21.2,21,'Hola')
print('Id del nuevo destino culinario:',destino_culinario_debug_1.id)

# Consola
print('Crear destino culinario: Ok')

# Verificamos el id del destino
import json
archivo = 'data/destinos_culinarios.json'
with open(archivo,'r') as file:
    destinos = json.load(file)
    if len(destinos) == 0:
        ultimo_id_en_archivo = 0
    else:
        ultimo_id_en_archivo = destinos[-1]['id']
    id_nuevo_destino = destino_culinario_debug_1.id
    if ultimo_id_en_archivo  == id_nuevo_destino - 1:
        print('Verificar ID del destino culinario: Ok')
        print(f'  Ultimo Id en data: {ultimo_id_en_archivo}')
        print(f'  ID del nuevo destino: {id_nuevo_destino}')

# Verificamos el cargado de archivos
lista_destinos_debug = DestinoCulinario.cargar_de_json(archivo)
print('Carga de JSON: Ok')

# Verificamos el guardado de datos
lista_destinos_debug.append(destino_culinario_debug_1)
DestinoCulinario.guardar_datos(archivo,lista_destinos_debug)
print('Guardado de nuevo JSON: Ok')