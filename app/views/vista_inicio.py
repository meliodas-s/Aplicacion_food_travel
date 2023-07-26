"""Esta vista contiene el menu principal. Permite dirigirnos hacia:
    - Explorar destinos Culinarios.
    - Busqueda y Filstro.
    - Planificar vistas.
    - Review y Calificaciones."""

import tkinter as tk
from tkinter.font import Font


class VistaInicio(tk.Frame):
    def __init__(self, master=None, controlador=None):
        """
        Crea la vista de inicio.
        """
        super().__init__(master)
        self.master = master
        self.controlador = controlador

        # Define una fuente grande y en negrita para el título
        titulo_font = Font(size=24, weight="bold")

        # Crea una etiqueta para el título y la agrega a la vista
        self.titulo = tk.Label(self, text="Food Travel", font=titulo_font)
        self.titulo.grid(row=0, column=0, pady=5)

        # Define una fuente más pequeña para la descripción de la funcionalidad
        descripcion_font = Font(size=12)

        # Se guarda el nombre de usuario para mostrarlo en la descripcion
        user_name = 'Usuario'

        # Crea una etiqueta para la descripción de la funcionalidad y la agrega a la vista
        self.descripcion = tk.Label(
            self,
            text=f"Bienvenido {user_name}",
            font=descripcion_font,
            wraplength=300,
        )
        self.descripcion.grid(row=1, column=0, pady=50)

        # Botones

        # Explorar Destinos Culinarios
        # Crea el botón para ir a ... y lo agrega a la vista
        self.boton_juegos = tk.Button(
            self, text="Destinos Culinarios", command=self.controlador
        )
        self.boton_juegos.grid(row=2, column=0, pady=10)

        # Busqueda y Filtro
        # Crea el botón para ir a ... y lo agrega a la vista
        self.boton_juegos = tk.Button(
            self, text="Busqueda", command=self.controlador
        )
        self.boton_juegos.grid(row=2, column=0, pady=10)

        # Planificar Visitas
        # Crea el botón para ir a ... y lo agrega a la vista
        self.boton_juegos = tk.Button(
            self, text="Planificar Visitas", command=self.controlador
        )
        self.boton_juegos.grid(row=2, column=0, pady=10)

        # Reviews y calificaciones
        # Crea el botón para ir a ... y lo agrega a la vista
        self.boton_juegos = tk.Button(
            self, text="Reviews", command=self.controlador
        )
        self.boton_juegos.grid(row=2, column=0, pady=10)
