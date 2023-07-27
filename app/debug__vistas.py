import customtkinter
from views.vista_inicio import VistaInicio

class Aplicacion(customtkinter.CTk):
    def __init__(self):
        customtkinter.CTk.__init__(self)
        self.title("Food Tavel")
        self.geometry("330x300")
        self.resizable(False, False)
        self.inicializar()
        self.cambiar_frame(self.vista_inicio)

    def inicializar(self):
        controlador_inicio = None

        self.vista_inicio = VistaInicio(self, controlador_inicio)


        self.ajustar_frame(self.vista_inicio)

    def ajustar_frame(self, frame):
        frame.grid(row=0, column=0, sticky="nsew")

    def cambiar_frame(self, frame_destino):
        frame_destino.tkraise()


if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
