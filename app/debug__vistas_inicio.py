import customtkinter

# Importando Vistas
from views.vista__inicio import VistaInicio
from views.vista__detalles_dest import VistaDetallesDestino
from views.vista__explorar import VistExplorar
from views.vista__planificar import VistaPlanificar
from views.vista__reviews import VistaReviews
from views.vista__inicio_sesion import VistaInicioSesion

# Importando Controladores
from controller.controlador__detalles_dest import ControladorDetallesDest
from controller.controlador__inicio_sesion import ControladorInicioSesion


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
        controlador_inicio_sesion = ControladorInicioSesion()

        self.vista_inicio_sesion = VistaInicioSesion(self, controlador_inicio_sesion)
        self.vista_inicio_sesion.inicializar()

        self.ajustar_frame(self.vista_inicio_sesion)

    def ajustar_frame(self, frame):
        frame.grid(row=0, column=0, sticky='nswe')

    def cambiar_frame(self, frame_destino):
        frame_destino.tkraise()


if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
