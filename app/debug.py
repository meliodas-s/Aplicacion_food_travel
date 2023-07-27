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

print()
################################################

# Crear nueva Actividad
from models.modelo__actividad import Actividad

# Consola
print('Importar modulo de Actividad: Ok')

# Creando destino y controlando id
actividad_debug_1 = Actividad('Hola',12,'hola')
print('Id de la nueva Actividad:',actividad_debug_1.id)

# Consola
print('Crear actividad: Ok')

# Verificamos el id de la actividad
import json
archivo = actividad_debug_1.ubicacion
with open(archivo,'r') as file:
    destinos = json.load(file)
    if len(destinos) == 0:
        ultimo_id_en_archivo = 0
    else:
        ultimo_id_en_archivo = destinos[-1]['id']
    id_nueva_actividad = actividad_debug_1.id
    if ultimo_id_en_archivo  == id_nueva_actividad - 1:
        print('Verificar ID de la actividad: Ok')
        print(f'  Ultimo Id en data: {ultimo_id_en_archivo}')
        print(f'  ID de nueva actividad: {id_nueva_actividad}')

# Verificamos el cargado de archivos
lista_actividades_debug = Actividad.cargar_de_json(archivo)
print('Carga de JSON: Ok')

# Verificamos el guardado de datos
lista_actividades_debug.append(actividad_debug_1)
Actividad.guardar_datos(archivo,lista_actividades_debug)
print('Guardado de nuevo JSON: Ok')