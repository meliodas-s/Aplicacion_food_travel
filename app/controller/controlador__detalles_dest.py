from models.modelo__destino_culinario import DestinoCulinario
from models.modelo__ubicacion import Ubicacion
import customtkinter
from PIL import Image, ImageTk


class ControladorDetallesDest:
    def __init__(self) -> None:
        # Defino los colores
        self.c_naranja_quemado = '#FF5722'
        self.c_gris_azulado = '#607D8B'
        self.c_verde = '#4CAF50'
        self.c_gris_claro = '#EEEEEE'

        self.destinos = DestinoCulinario.cargar_de_json(
            'data/destinos_culinarios.json')  # -> list[DestinoCulinario]
        self.ubicaciones = Ubicacion.cargar_de_json(
            'data/ubicacion.json')  # -> list[Ubicacion]
        self.ultimo_marcador_abierto = None

    def mostrar_ubicaciones(self, vista, lista_destinos: list) -> None:
        for i, destino in enumerate(self.destinos):
            destino = customtkinter.CTkCheckBox(
                vista, text=destino.nombre, hover_color= self.c_verde, fg_color= self.c_gris_azulado)
            destino.grid(row=i, column=0, pady=10, padx=10, sticky="w")
            lista_destinos.append(destino)

    def cargar_imagenes(self, lista_images: list) -> None:
        for local in self.destinos:
            imagen = ImageTk.PhotoImage(
                Image.open(f'views/images/{local.imagen}').resize((200, 200)))
            lista_images.append(imagen)

    def cargar_marcadores(self, vista, lista_marcadores: list) -> None:
        for local in self.destinos:
            imagen = ImageTk.PhotoImage(
                Image.open(f'views/images/{local.imagen}').resize((200, 200)))
            # Por ahora el id de la ubicacion corresponde al
            # numero de item de la lista ubicaciones
            ubicacion = self.ubicaciones[local.id_ubicacion - 1]
            marcador = vista.agregar_marcador_mapa(
                latitud=ubicacion.coordenadas[0], longitud=ubicacion.coordenadas[1], texto=local.nombre, imagen=imagen)
            marcador.hide_image(True)
            lista_marcadores.append(marcador)

# def seleccionar_local(self, event):
#         # Obtiene el índice del elemento seleccionado
#         indice_seleccionado = self.lista_locales.curselection()
#         # Obtiene el local seleccionado
#         local_seleccionado = self.locales[indice_seleccionado[0]]
        
#         ubicacion_seleccionada = Ubicacion(0, 0, 0, "")
        
#         # Busca la ubicación correspondiente al local seleccionado
#         for ubicacion in self.ubicaciones:
#             if ubicacion.id == local_seleccionado.id_ubicacion:
#                 ubicacion_seleccionada = ubicacion
#                 break
    def seleccionar_ubicacion(self, marcador):
        if marcador.image_hidden is True:
            # Escondo el ultimo marcador abierto
            if self.ultimo_marcador_abierto is None:
                pass
            else:
                self.ultimo_marcador_abierto.hide_image(True)

            marcador.hide_image(False)
            self.ultimo_marcador_abierto = marcador
            
        else:
            marcador.hide_image(True)
            self.ultimo_marcador_abierto = None
        print("Ubicación seleccionada: ", marcador.text)
    
    def get(self, lista_destinos):
        checked_checkboxes = []
        for checkbox in lista_destinos:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.get('text'))
        return checked_checkboxes