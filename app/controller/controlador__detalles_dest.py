from models.modelo__destino_culinario import DestinoCulinario
from models.modelo__destino_culinario import ItemMenu
from models.modelo__ubicacion import Ubicacion
import customtkinter
import tkinter
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

    def seleccionar_local(self):
        """
        Recorremos todos los item menu y vemos cual tiene el status de
        'normal' que es el estado cuando esta seleccionado.
        """
        ubicacion_seleccionada = Ubicacion('', 0, 0)
        self.mapa = self.app.vista_detalles_dest.mapa

        # Busca la ubicación correspondiente al local seleccionado
        id_selec = self.radiobutton_variable.get()
        for item in self.items_menu:
            if item.destino.id == id_selec:
                ubicacion_seleccionada = item.ubicacion
                break
        self.mapa.set_position(
            ubicacion_seleccionada.coordenadas[0], ubicacion_seleccionada.coordenadas[1])

        print(
            f'Latidu: {ubicacion_seleccionada.coordenadas[0]}, Longitud: {ubicacion_seleccionada.coordenadas[1]}')

    def mostrar_ubicaciones(self, vista) -> None:
        """Carga los nombres de los locales en el menu de seleccion"""
        self.radiobutton_variable = tkinter.IntVar(value=0)
        for i, destino in enumerate(self.destinos):
            radiobutton = customtkinter.CTkRadioButton(
                vista, command=self.seleccionar_local, text=destino.nombre, hover_color=self.c_verde, fg_color=self.c_gris_azulado, variable=self.radiobutton_variable, value=destino.id)
            radiobutton.grid(row=i, column=0, pady=10, padx=10, sticky="w")
            item_menu = ItemMenu(destino, radiobutton)

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
        """
        Metodo para el boton accion, para mostrar informacion en Gui
        """
        # Busca la info correspondiente al local seleccionado
        id_selec = self.radiobutton_variable.get()
        for item in self.items_menu:
            if item.destino.id == id_selec:
                lugar = item.destino
                break

        # Lleno el label con la informacion encontrada
        self.app.vista_detalles_dest.mostrar_info_lugar(lugar)

        # Cambio al frame con informacion que contiene le label
        self.app.vista_detalles_dest.cambiar_frame(
            self.app.vista_detalles_dest.frame_lugar)

        # Advierto que ahora estoy pocisionado en info lugar
        self.app.vista_detalles_dest.pestaña_abierta = 'info lugar'

        # Muestro informacion por consola
        print('Id Ubicacion seleccionado: ', self.radiobutton_variable.get())

    def regresar(self):
        """Metodo para regresar del menu de error"""
        self.app.vista_detalles_dest.cambiar_frame(
            self.app.vista_detalles_dest.frame_menu)

    def regresar_menu(self):
        """
        Metodo para:
            1. volver al "menu principa" si esta en la "lista"
            2. Volver a la "lista" si esta en "informacion del lugar"
        """
        if self.app.vista_detalles_dest.pestaña_abierta == 'lista lugares':
            # Estoy en la vista de listas entonces vuelve al menu principal
            self.app.cambiar_frame(self.app.vista_inicio)

        elif self.app.vista_detalles_dest.pestaña_abierta == 'info lugar':
            # Estoy en la vista de informacion entonces vuelve a la vista de lista
            self.app.vista_detalles_dest.cambiar_frame(
                self.app.vista_detalles_dest.frame_menu)

            # Restablesco la configuracion
            self.app.vista_detalles_dest.pestaña_abierta = 'lista lugares'
            
