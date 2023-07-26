import json


class Usuario:
    def __init__(self,
                 nombre: str,
                 apellido: str,
                 historial_rutas: list[int],
                 id=None) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.historial_rutas = historial_rutas
        self.__id = id

        # Asignando id al destino culinario

        def creacion_id():
            """Definimos el id del destino culinario
            al llamar el archivo donde se guardan los destinos, contar
            la cantidad de elementos y asignar ese numero mas uno
            como id del destino.
            """
            with open('data/usuarios.json', 'r') as file:
                # Pasamo de Json a dict
                destinos = json.load(file)

                # Contamos la cantidad de destinos
                cantidad_de_destinos = len(destinos)

                # Asignamos este valor mas uno como id
                self.__id = cantidad_de_destinos + 1

        # Si es un nuevo destino no tiene ID
        if self.__id == None:
            creacion_id()
