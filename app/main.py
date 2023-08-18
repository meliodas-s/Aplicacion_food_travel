import customtkinter

# Importando Vistas
from views.vista__inicio import VistaInicio
from views.vista__detalles_dest import VistaDetallesDestino
from views.vista__explorar import VistExplorar
from views.vista__planificar import VistaPlanificar
from views.vista__reviews import VistaReviews
from views.vista__inicio_sesion import VistaInicioSesion
from views.vista__registrarse import VistaRegistrarse

# Importando Controladores
from controller.controlador__detalles_dest import ControladorDetallesDest
from controller.controlador__inicio import ControladorInicio
from controller.controlador__inicio_sesion import ControladorInicioSesion
from controller.controlador__registrarse import ControladorRegistrarse


class Aplicacion(customtkinter.CTk):
    def __init__(self):
        self.c_naranja_quemado = '#FF5722'
        self.c_gris_azulado = '#607D8B'
        self.c_verde = '#4CAF50'
        self.c_gris_claro = '#EEEEEE'

        customtkinter.CTk.__init__(self)

        # Configuraciones basicas
        self.title("Food Tavel")
        self.geometry("500x500")
        self.config(bg=self.c_naranja_quemado)  # Color de background
        self.minsize(400, 500)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Llamar vista principal
        self.inicializar()
        self.cambiar_frame(self.vista_inicio_sesion)

    def inicializar(self):
        controlador_inicio_sesion = ControladorInicioSesion(self)
        controlador_inicio = ControladorInicio(self)
        controlador_detalles_dest = ControladorDetallesDest(self)
        controlador_registrarse = ControladorRegistrarse(self)
        controlador_explorar = None
        controlador_planificar = None
        controlador_reviews = None

        # (Inicio)
        self.vista_inicio = VistaInicio(self, controlador_inicio)
        self.vista_inicio.inicializar()
        # (Detalles destinos)
        self.vista_detalles_dest = VistaDetallesDestino(
            self, controlador_detalles_dest)
        # (Inicio sesion)
        self.vista_inicio_sesion = VistaInicioSesion(
            self, controlador_inicio_sesion)
        self.vista_inicio_sesion.inicializar()
        # (Registrare)
        self.vista_registrarse = VistaRegistrarse(
            self, controlador_registrarse)
        # self.vista_detalles_dest.inicializar()
        # self.vista_explorar = VistExplorar(self, controlador_explorar)
        # self.vista_planificar = VistaPlanificar(self, controlador_planificar)
        # self.vista_reviews = VistaReviews(self, controlador_reviews)

        self.ajustar_frame(self.vista_inicio)
        self.ajustar_frame(self.vista_detalles_dest)
        self.ajustar_frame(self.vista_inicio_sesion)
        self.ajustar_frame(self.vista_registrarse)
        # self.ajustar_frame(self.vista_explorar)
        # self.ajustar_frame(self.vista_planificar)
        # self.ajustar_frame(self.vista_reviews)

    def ajustar_frame(self, frame):
        frame.grid(row=0, column=0, sticky='nswe')

    def cambiar_frame(self, frame_destino):
        frame_destino.tkraise()


if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
