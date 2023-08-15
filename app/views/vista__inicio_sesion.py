# Vista inicio sesion
import customtkinter


class VistaInicioSesion(customtkinter.CTkFrame):
    def __init__(self, master=None, controlador=None,
                 values=['Usuario', 'Contraseña'],):
        """
        Crea la vista de inicio de sesion.
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
        self.acciones = values
        self.entradas = []
        self.numero_intentos = 0 # Contador para saber cuantas veces se equivoco

        # Frame_1: Botones, titulo, descripcion
        self.frame_central = customtkinter.CTkFrame(self)
        self.frame_central.grid(row=0, column=0)

        # Fuente grande y en negrita para el título
        titulo_font = customtkinter.CTkFont(size=24, weight="bold")
        self.titulo = customtkinter.CTkLabel(self.frame_central,
                                             text="Food Travel",
                                             font=titulo_font)
        self.titulo.grid(row=0, column=0, pady=10, padx=50)

        # Creando los entry
        for i, (value, accion) in enumerate(zip(self.values, self.acciones)):
            show = None
            if value == 'Contraseña':
                show = '*'
            entrada = customtkinter.CTkEntry(
                self.frame_central, show=show, placeholder_text=value, fg_color=self.c_gris_azulado, height=40)
            entrada.grid(row=i + 1, column=0, pady=10)
            self.entradas.append(entrada)

        # (Boton iniciar sesion)
        self.boton_inicio = customtkinter.CTkButton(
            self.frame_central, text='Iniciar Sesion', command=None, height=40, fg_color=self.c_gris_azulado, hover_color=self.c_verde)
        self.boton_inicio.grid(column=0, row=i + 2, pady = 10)

        # (Boton Registrarse)
        self.boton_registrarse = customtkinter.CTkButton(
            self.frame_central, text='Registrarse', command=None, height=40, fg_color=self.c_gris_azulado, hover_color=self.c_verde)
        self.boton_registrarse.grid(column=0, row=i + 3, pady= 10)

    # Para establecer la configuracion por que se resetea
    def inicializar(self):
        self.configure(bg_color=self.c_naranja_quemado,
                       fg_color=self.c_naranja_quemado)
        self.frame_central.configure(bg_color=self.c_naranja_quemado,
                                     fg_color=self.c_naranja_quemado)
