import customtkinter
from views.vista__inicio import VistaInicio


class Aplicacion(customtkinter.CTk):
    def __init__(self):
        self.c_naranja_quemado = '#FF5722'
        self.c_gris_azulado = '#607D8B'
        self.c_verde = '#4CAF50'
        self.c_gris_claro = '#EEEEEE'

        customtkinter.CTk.__init__(self)

        # Configuraciones basicas
        self.title("Food Tavel")
        self.geometry("330x500")
        self.config(bg=self.c_naranja_quemado)  # Color de background
        self.minsize(400, 500)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Llamar vista principal
        self.inicializar()
        self.cambiar_frame(self.vista_inicio)

    def inicializar(self):
        controlador_inicio = None

        self.vista_inicio = VistaInicio(self, controlador_inicio)
        self.vista_inicio.inicializar()
        self.ajustar_frame(self.vista_inicio)

    def ajustar_frame(self, frame, stick = 'nswe'):
        frame.grid(row = 0, column = 0, sticky = stick)

    def cambiar_frame(self, frame_destino):
        frame_destino.tkraise()


if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
