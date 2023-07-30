# Vista detalles del destino, se vera el mapa y las ubicaciones seleccionadas o el destino seleccionado
import customtkinter
import tkinter
from tkintermapview import TkinterMapView
from models.modelo__ubicacion import Ubicacion
from models.modelo__destino_culinario import DestinoCulinario


class VistaDetallesDestino(customtkinter.CTkFrame):
    def __init__(self, master, controlador, seleccionar_local_callback=None):
        self.c_naranja_quemado = '#FF5722'
        self.c_gris_azulado = '#607D8B'
        self.c_verde = '#4CAF50'
        self.c_gris_claro = '#EEEEEE'

        super().__init__(master)
        # Configuracion basica
        self.columnconfigure(0, weight=50)
        self.columnconfigure(1, weight=100)
        self.rowconfigure(0, weight=1)
        self.master = master
        self.controlador = controlador

        # Placeholder para el menu izquierdo
        self.frame_menu = customtkinter.CTkFrame(
            self, fg_color=self.c_naranja_quemado)
        self.frame_menu.grid(column=0, row=0, sticky='nswe')
        self.frame_menu.columnconfigure(0, weight=1)
        self.frame_menu.rowconfigure(0, weight=75)  # Menu locales
        self.frame_menu.rowconfigure(1, weight=25)  # Boto accion

        # Frame para el mapa
        self.frame_mapa = customtkinter.CTkFrame(self, fg_color=self.c_verde)
        self.frame_mapa.grid(column=1, row=0, sticky='nswe')
        self.frame_mapa.columnconfigure(0, weight=0)

        # Placeholder para el mapa
        self.mapa = TkinterMapView(self.frame_mapa)
        self.mapa.pack(fill='both', expand=True)
        self.mapa.set_position(-24.77616437851034, -65.41079411004006)
        self.mapa.set_zoom(16)

        # Frame para menu con locales (menu locales)
        self.frame_menu_sccroll = customtkinter.CTkScrollableFrame(
            master=self.frame_menu, label_text='Actividades', corner_radius=None, bg_color=self.c_naranja_quemado, fg_color='transparent', label_fg_color=self.c_gris_azulado, scrollbar_button_color=self.c_gris_azulado, scrollbar_button_hover_color=self.c_verde)
        self.frame_menu_sccroll.grid(column=0, row=0, sticky='nswe')
        self.frame_menu_sccroll.columnconfigure(0, weight=1)

        # Frame para boton accion segun local seleccionado (boton accion)
        self. boton_accion = customtkinter.CTkButton(
            self.frame_menu, text='Detalles', command=None, height=40, fg_color=self.c_gris_azulado, hover_color=self.c_verde)
        self.boton_accion.grid(column = 0, row = 1)

        # Cargando nombre de locales
        self.labels_locales = []
        self.controlador.mostrar_ubicaciones(
            self.frame_menu_sccroll, self.labels_locales)

        # Cargar imagenes
        self.imagenes = []
        self.controlador.cargar_imagenes(self.imagenes)

        # Cargar marcadores
        self.marcadores = []
        self.controlador.cargar_marcadores(
            lista_marcadores=self.marcadores, vista=self)

    def agregar_local(self, local):
        nombre = local.nombre
        self.labels_locales.append(local)

    def agregar_marcador_mapa(self, latitud, longitud, texto, imagen=None):
        return self.mapa.set_marker(latitud, longitud, text=texto, image=imagen, command=self.controlador.seleccionar_ubicacion)
