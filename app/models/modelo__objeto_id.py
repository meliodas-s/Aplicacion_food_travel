import json


class ObjetoId:
    """Es un modelo que dado un archivo .json genera un id"""
    def __init__(self,
                 ubicacion,
                 id=None,
                 ) -> None:
        self.__id = id
        self.ubicacion = ubicacion

        # Asignando id al destino culinario

        def creacion_id():
            """
            Definimos el id del destino culinario
            al llamar el archivo donde se guardan los destinos, contar
            la cantidad de elementos y asignar ese numero mas uno
            como id del destino.
            """
            with open(self.ubicacion, 'r') as file:
                # Pasamos de Json a dict
                destinos = json.load(file)

                # Buscamos el ultimo id del objeto
                if len(destinos) == 0:
                    # Si no hay objetos el Id es 1
                    self.__id = 1
                else:
                    # Si hay objetos el Id no sera uno
                    ultimos_id = destinos[-1]['id']

                    # Asignamos este valor mas uno como id
                    self.__id = ultimos_id + 1

        # Si es un nuevo Objeto no tiene ID
        if self.__id is None:
            creacion_id()

    @property
    def id(self):
        return self.__id