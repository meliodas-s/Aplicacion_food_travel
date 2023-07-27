"""Esta vista contiene el menu principal. Permite dirigirnos hacia:
    - Explorar destinos Culinarios.
    - Busqueda y Filstro.
    - Planificar vistas.
    - Review y Calificaciones."""

import customtkinter


class VistaInicio(customtkinter.CTkFrame):
    def __init__(self, master=None, controlador=None,
                 values=['Destinos culinarios', 'Busqueda', 'Planificar', 'Reviews'],):
        """
        Crea la vista de inicio.
        """

        # Defino los colores
        self.c_naranja_quemado = '#FF5722'
        self.c_gris_azulado = '#607D8B'
        self.c_verde = '#4CAF50'
        self.c_gris_claro = '#EEEEEE'

        super().__init__(master)
        self.master = master
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.controlador = controlador
        self.values = values
        self.botones = []

        # Frame_1: Botones, titulo, descripcion
        self.frame_inicio = customtkinter.CTkFrame(self)
        self.frame_inicio.grid(row=0, column=0)

        # Fuente grande y en negrita para el título
        titulo_font = customtkinter.CTkFont(size=24, weight="bold")
        self.titulo = customtkinter.CTkLabel(self.frame_inicio,
                                             text="Food Travel",
                                             font=titulo_font)
        self.titulo.grid(row=0, column=0, pady=10, padx=50)

        # Descripcion y nombre de usuario
        descripcion_font = customtkinter.CTkFont(size=12)
        user_name = 'Usuario'
        self.descripcion = customtkinter.CTkLabel(
            self.frame_inicio,
            text=f"Bienvenido {user_name}",
            font=descripcion_font,
            wraplength=300,
            height=40)
        self.descripcion.grid(row=1, column=0, pady=10)

        # Creando los botones
        for i, value in enumerate(self.values):
            boton = customtkinter.CTkButton(
                self.frame_inicio, text=value, command=self.controlador,
                fg_color=self.c_gris_azulado, hover_color=self.c_verde,height=40)
            boton.grid(row=i + 2, column=0, pady=10)
            self.botones.append(boton)

    # Para establecer la configuracion por que se resetea
    def inicializar(self):
        self.configure(bg_color=self.c_naranja_quemado,
                       fg_color=self.c_naranja_quemado)
        self.frame_inicio.configure(bg_color=self.c_naranja_quemado,
                          fg_color=self.c_naranja_quemado)
