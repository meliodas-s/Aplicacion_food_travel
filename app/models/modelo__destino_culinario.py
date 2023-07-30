import json
from models.modelo__objeto_id import ObjetoId
from customtkinter import CTkCheckBox

class DestinoCulinario(ObjetoId):
    """
    [Descripcion]:
        Esta clase hereda de la clase ObjetoId dos cosas:
            1. Mmetodo __intit__ que permite la autogeneracion de id.
            2. Metodo tipo property, permite llamar al atributo id.
    """
    def __init__(self,
                 nombre: str,
                 tipo_cocina: str,
                 ingredientes: list[str],
                 precio_minimo: float,
                 precio_maximo: float,
                 popularidad: float,
                 id_ubicacion: int,
                 imagen: str,
                 id=None,
                 ) -> None:
        super().__init__('data/destinos_culinarios.json', id)
        self.nombre = nombre
        self.tipo_cocina = tipo_cocina
        self.ingredientes = ingredientes
        self.precio_minimo = precio_minimo
        self.precio_maximo = precio_maximo
        self.popularidad = popularidad
        self.id_ubicacion = id_ubicacion
        self.imagen = imagen

    # Metodos de lectura
    @classmethod
    def cargar_de_json(cls, archivo):
        """
        [Descripcion]:
            Dada la ubicacion del archivo json, importa los datos
        y los devuelve en forma de clase todos dentro de una lista.

        [Nota]:
            Podria se poco eficiente, debido a que siempre se llama
        a todos los destinos juntos y no a uno especifico.

        [Args]:
            archivo (str): ruta del archivo .json

        [Returns]:
            lst: Lista con los destinos
        """
        with open(archivo, 'r') as f:
            data = json.load(f)
        return [cls(**destino) for destino in data]

    # Metodos de guardado
    def crear_json(self):
        return {
            'nombre': self.nombre,
            'tipo_cocina': self.tipo_cocina,
            'ingredientes': self.ingredientes,
            'precio_minimo': self.precio_minimo,
            'precio_maximo': self.precio_maximo,
            'popularidad': self.popularidad,
            'id_ubicacion': self.id_ubicacion,
            'imagen': self.imagen,
            'id': self.id
        }

    @staticmethod
    def guardar_datos(archivo: str, objetos: list):
        """
        [Descripcion]:
            Dada una lista de objetos (DestinoCulinario) los convierte
        en diccionarios y los transforma en json. Luego se guardan en
        la ubicacion correspondiente.
        """
        with open(archivo, 'w') as f:
            lista_dicts = [destino_dict.crear_json()
                           for destino_dict in objetos]
            json.dump(lista_dicts, f)
