from models.modelo__destino_culinario import DestinoCulinario
from models.modelo__ubicacion import Ubicacion
import customtkinter

class ControladorInicio:
    def __init__(self, app) -> None:
        self.app = app
    
    def ir_vista__detalles_dest(self):
        self.app.cambiar_frame(self.app.vista_detalles_dest)