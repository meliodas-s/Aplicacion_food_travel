# Vista de registrar
import customtkinter


class VistaRegistrarse(customtkinter.CTkFrame):
    def __init__(self, master, controlador):

        # Defino los colores
        self.c_naranja_quemado = '#FF5722'
        self.c_gris_azulado = '#607D8B'
        self.c_verde = '#4CAF50'
        self.c_gris_claro = '#EEEEEE'

        super().__init__(master)
        self.master = master
        self.controlador = controlador
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.cantidad_filas = 0
        self.entradas = {}
        self.botones = {}

        # Frame_1: Botones, titulo, descripcion
        self.frame_central = customtkinter.CTkFrame(self)
        self.frame_central.grid(row=0, column=0)

        # Fuente grande y en negrita para el título
        titulo_font = customtkinter.CTkFont(size=24, weight="bold")
        self.titulo = customtkinter.CTkLabel(self.frame_central,
                                             text="Food Travel",
                                             font=titulo_font)
        self.titulo.grid(row=0, column=0, pady=10, padx=50)

        # Entradas
        self.entradas['nombre'] = customtkinter.CTkEntry(self.frame_central)
        self.entradas['apellido'] = customtkinter.CTkEntry(self.frame_central)
        self.entradas['usuario'] = customtkinter.CTkEntry(self.frame_central)
        self.entradas['contrasenna'] = customtkinter.CTkEntry(self.frame_central)

        # Entradas: Se acomodan
        for (i, entrada), key in zip(enumerate(self.entradas.values()), self.entradas.keys()):
            show = None
            if key == 'contrasenna':
                show = '*'
            entrada.configure(show= show, placeholder_text=key, height=40)
            entrada.grid(column=0, row=i, pady=10)
        self.cantidad_filas += (i + 1)

        # Botones: [Boton, accion]
        self.botones['registrarse'] = [customtkinter.CTkButton(self.frame_central), self.registrarse]
        self.botones['volver'] = [customtkinter.CTkButton(self.frame_central), self.controlador.volver_login]

        # Botones: se acomodan
        for (i, boton), key in zip(enumerate(self.botones.values()), self.botones.keys()):
            boton[0].grid(column=0, row=self.cantidad_filas + i, pady=10)
            boton[0].configure(text = key, command = boton[1], height=40)

        self.cantidad_filas += (i + 1)

    def obtener_entradas(self):
        entradas = {}
        for clave,entrada in zip(self.entradas.keys(),self.entradas.values()):
            entradas[f'{clave}'] = entrada.get()
        print(entradas)
        return entradas
    
    def validar_datos(self,valores):
        for clave,valor in zip(valores.keys(),valores.values()):
            if len(valor) < 8:
                print(f'{clave} tiene menos de 8 digitos')
                return False
        return True

    def registrarse(self):
        entradas = self.obtener_entradas()
        if self.validar_datos(entradas):
            self.controlador.registrarse(entradas)
        else:
            self.controlador.registro_fallido()