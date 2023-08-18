# Importo la clase usuario para el registro
from models.modelo__usuario import Usuario

# custom tkinter para mensajes de exito o fallo
import customtkinter

# Codigo de la clase controlador
class ControladorRegistrarse:
    def __init__(self, app) -> None:
        # Defino los colores
        self.c_naranja_quemado = '#FF5722'
        self.c_gris_azulado = '#607D8B'
        self.c_verde = '#4CAF50'
        self.c_gris_claro = '#EEEEEE'
        self.c_rojo_error = '#f5291d'

        self.app = app
        self.mensaje_activo = False # P/saber si se mostro msj

    def volver_login(self):
        self.app.cambiar_frame(self.app.vista_inicio_sesion)

    def mensaje_aviso(self, mensaje:str, color:str):
        """
        Avisa si el registro fue existoso o fallido
        """
        mensaje = customtkinter.CTkLabel(
            self.app.vista_registrarse.frame_central, fg_color=color, text=mensaje, corner_radius= 10 , height=40)


        if not self.mensaje_activo:
            # Lo coloco en la ultima columna disponible
            mensaje.grid(column=0, row=self.app.vista_registrarse.cantidad_filas, pady = 10)

            # Aumento el contador de filas
            self.app.vista_registrarse.cantidad_filas += 1
            
            # Cambio el valor de self.mensaje_activo
            self.mensaje_activo = True
        else:
             # Como ya hay un mensaje, entonces lo tapo con este nuevo
            mensaje.grid(column=0, row=self.app.vista_registrarse.cantidad_filas - 1, pady = 10)

    def registrarse(self, entradas):
        """
        Recibe datos y lo almacena como un json del tipo usuario
        """
        nuevo_usuario = Usuario(
            entradas['usuario'], entradas['contrasenna'], entradas['nombre'], entradas['apellido'])
        
        ruta = "data/usuarios.json"
        usuarios = []
        usuarios = Usuario.cargar_de_json(ruta)
        usuarios.append(nuevo_usuario)
        Usuario.guardar_datos(ruta, usuarios)

        self.mensaje_aviso('Registro exitoso', self.c_verde)

    def registro_fallido(self):
        print('El registro fallo')
        self.mensaje_aviso('registro fallido', self.c_rojo_error)
