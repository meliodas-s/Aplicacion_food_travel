import json
from models.modelo__objeto_id import ObjetoId


class Review(ObjetoId):
    def __init__(self,
                 id_destino:int,
                 id_usuario:int,
                 calificacion:int,
                 comentario:str,
                 animo:str,
                 id=None) -> None:
        super().__init__('data/actividades.json', id)
        self.id_destino = id_destino
        self.id_usuario = id_usuario
        self.calificacion = calificacion
        self.comentario = comentario
        self.animo = animo

    # Metodos de lectura
    @classmethod
    def cargar_de_json(cls, archivo):
        """
        [Descripcion]:
            Dada la ubicacion del archivo json, importa los datos
        y los devuelve en forma de clase todos dentro de una lista.

        [Nota]:
            Podria ser poco eficiente, debido a que siempre se llama
        a todos los destinos juntos y no a uno especifico.

        [Args]:
            archivo (str): ruta del archivo .json

        [Returns]:
            lst: Lista con los Objetos
        """
        with open(archivo, 'r') as f:
            data = json.load(f)
        return [cls(**objeto) for objeto in data]

    # Metodos de guardado
    def crear_json(self):
        return {
            'id_destino': self.id_destino,
            'id_usuario': self.id_usuario,
            'calificacion': self.calificacion,
            'comentario': self.comentario,
            'animo': self.animo,
            'id': self.id
        }

    @staticmethod
    def guardar_datos(archivo: str, objetos: list):
        """
        [Descripcion]:
            Dada una lista de objetos (Objeto) los convierte
        en diccionarios y los transforma en json. Luego se guardan en
        la ubicacion correspondiente.
        """
        with open(archivo, 'w') as f:
            lista_dicts = [objeto_dict.crear_json()
                           for objeto_dict in objetos]
            json.dump(lista_dicts, f)
