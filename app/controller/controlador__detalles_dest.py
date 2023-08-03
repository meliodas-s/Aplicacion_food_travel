from models.modelo__destino_culinario import DestinoCulinario
from models.modelo__destino_culinario import ItemMenu
from models.modelo__ubicacion import Ubicacion
import customtkinter
from PIL import Image, ImageTk


class ControladorDetallesDest:
    def __init__(self, app) -> None:
        # Defino los colores
        self.c_naranja_quemado = '#FF5722'
        self.c_gris_azulado = '#607D8B'
        self.c_verde = '#4CAF50'
        self.c_gris_claro = '#EEEEEE'

        self.destinos = DestinoCulinario.cargar_de_json(
            'data/destinos_culinarios.json')  # -> list[DestinoCulinario]
        self.ubicaciones = Ubicacion.cargar_de_json(
            'data/ubicacion.json')  # -> list[Ubicacion]
        self.items_menu = []
        self.app = app
        self.ultimo_marcador_abierto = None

    def mostrar_ubicaciones(self, vista) -> None:
        """Carga los nombres de los locales en el menu de seleccion"""
        for i, destino in enumerate(self.destinos):
            checkbox = customtkinter.CTkCheckBox(
                vista, text=destino.nombre, hover_color=self.c_verde, fg_color=self.c_gris_azulado)
            checkbox.grid(row=i, column=0, pady=10, padx=10, sticky="w")
            item_menu = ItemMenu(destino, checkbox)

            # Se carga un item menu en el controlador
            self.items_menu.append(item_menu)

    def cargar_imagenes(self) -> None:
        """Carga las imagenes para crear los marcadores"""
        for item in self.items_menu:
            imagen = ImageTk.PhotoImage(
                Image.open(f'views/images/{item.destino.imagen}').resize((200, 200)))
            item.imagen = imagen

    def cargar_marcadores(self, vista, lista_marcadores: list) -> None:
        for item in self.items_menu:
            item.ubicacion = Ubicacion.busca_id(
                item.destino.id_ubicacion, self.ubicaciones)
            marcador = vista.agregar_marcador_mapa(
                latitud=item.ubicacion.coordenadas[0], longitud=item.ubicacion.coordenadas[1], texto=item.destino.nombre, imagen=item.imagen)
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
            if self.ultimo_marcador_abierto is None:
                pass
            else:
                # Escondo el ultimo marcador abierto
                self.ultimo_marcador_abierto.hide_image(True)

            marcador.hide_image(False)
            self.ultimo_marcador_abierto = marcador

        else:
            marcador.hide_image(True)
            self.ultimo_marcador_abierto = None
        print("Ubicación seleccionada: ", marcador.text)

    def get(self):
        """Metodo para el boton accion"""
        ids_destinos = []
        for item in self.items_menu:
            if item.check_box.get() == 1:
                ids_destinos.append(item.destino.id)

        if len(ids_destinos) != 1:
            # Si seleccion mas de un items o 0 items sale un mensaje de error
            self.app.vista_detalles_dest.cambiar_frame(
                self.app.vista_detalles_dest.frame_error)

    def regresar(self):
        """Metodo para regresar del menu de error"""
        self.app.vista_detalles_dest.cambiar_frame(
            self.app.vista_detalles_dest.frame_menu)
        
    def regresar_menu(self):
        '''Metodo para volver al menu principal'''
        self.app.cambiar_frame(self.app.vista_inicio)
