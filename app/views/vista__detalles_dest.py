# Vista detalles del destino, se vera el mapa y las ubicaciones seleccionadas o el destino seleccionado
import customtkinter
from tkintermapview import TkinterMapView

class VistaDetallesDestino(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master):