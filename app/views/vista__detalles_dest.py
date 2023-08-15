# Vista detalles del destino, se vera el mapa y las ubicaciones seleccionadas o el destino seleccionado
import customtkinter
import tkinter
from tkintermapview import TkinterMapView
from models.modelo__ubicacion import Ubicacion
from models.modelo__destino_culinario import ItemMenu
from models.modelo__destino_culinario import DestinoCulinario


class VistaDetallesDestino(customtkinter.CTkFrame):
    def __init__(self, master, controlador):
        self.c_naranja_quemado = '#FF5722'
        self.c_gris_azulado = '#607D8B'
        self.c_verde = '#4CAF50'
        self.c_gris_claro = '#EEEEEE'

        super().__init__(master)
        # Configuracion basica
        self.columnconfigure(0, weight=5)
        self.columnconfigure(1, weight=20)
        self.columnconfigure(2, weight=100)
        self.rowconfigure(0, weight=1)
        self.master = master
        self.controlador = controlador
        # Para saber a que bentana nos lleva el boto de retroseso
        self.pestaña_abierta = 'lista lugares'

        # Placeholder para el menu izquierdo
        self.frame_menu = customtkinter.CTkFrame(
            self, fg_color=self.c_naranja_quemado)
        self.frame_menu.grid(column=1, row=0, sticky='nswe')
        self.frame_menu.columnconfigure(0, weight=1)
        self.frame_menu.rowconfigure(0, weight=75)  # Menu locales
        self.frame_menu.rowconfigure(1, weight=25)  # Boton accion

        # Frame para el mapa
        self.frame_mapa = customtkinter.CTkFrame(self, fg_color=self.c_verde)
        self.frame_mapa.grid(column=2, row=0, sticky='nswe')
        self.frame_mapa.columnconfigure(0, weight=0)

        # Placeholder para el mapa: se usa pack para lograr fullscreen
        self.mapa = TkinterMapView(self.frame_mapa)
        self.mapa.pack(fill='both', expand=True)
        self.mapa.set_position(-24.77616437851034, -65.41079411004006)
        self.mapa.set_zoom(16)

        # (menu locales): Frame para menu con locales
        self.frame_menu_sccroll = customtkinter.CTkScrollableFrame(
            master=self.frame_menu, label_text='Actividades', corner_radius=None, bg_color=self.c_naranja_quemado, fg_color='transparent', label_fg_color=self.c_gris_azulado, scrollbar_button_color=self.c_gris_azulado, scrollbar_button_hover_color=self.c_verde)
        self.frame_menu_sccroll.grid(column=0, row=0, sticky='nswe')
        self.frame_menu_sccroll.columnconfigure(0, weight=1)

        # (boton accion): Boton accion segun local seleccionado
        self. boton_accion = customtkinter.CTkButton(
            self.frame_menu, text='Detalles', command=controlador.get, height=40, fg_color=self.c_gris_azulado, hover_color=self.c_verde)
        self.boton_accion.grid(column=0, row=1)

        self.controlador.mostrar_ubicaciones(
            self.frame_menu_sccroll)  # Cargar locales
        self.controlador.cargar_imagenes()  # Cargar imagenes

        # Cargar marcadores
        self.marcadores = []
        self.controlador.cargar_marcadores(
            lista_marcadores=self.marcadores, vista=self)

        # (boton regresar) Frame: Regresa al menu inicio
        self.grid_return = customtkinter.CTkFrame(self)
        self.grid_return.grid(column=0, row=0, sticky='nswe')
        self.grid_return.columnconfigure(0, weight=1)
        self.grid_return.rowconfigure(0, weight=1)

        # (Boton regresar)
        self.boton_return = customtkinter.CTkButton(self.grid_return, command=controlador.regresar_menu,
                                                    height=40, width=10, fg_color=self.c_gris_azulado, hover_color=self.c_verde, text='<')
        self.boton_return.grid(column=0, row=0, sticky='nswe')

        # (Frame Info Lugar)
        self.frame_lugar = customtkinter.CTkFrame(
            self, fg_color=self.c_naranja_quemado)
        self.frame_lugar.grid(column=1, row=0, sticky='nswe')
        self.frame_lugar.columnconfigure(0, weight=1)
        self.frame_lugar.rowconfigure(0, weight=1)

        # (Frame Info Lugar): Informacion sobre el lugar seleccionado
        self.lugar_label = customtkinter.CTkLabel(
            self.frame_lugar, text="", font= ('Open Sans',13))
        self.lugar_label.grid(column=0, row=0, sticky='nswe')

        # Inicializar
        self.cambiar_frame(self.frame_menu)

    def mostrar_info_lugar(self, lugar):
        info = f"nombre: {lugar.nombre},\ntipo_cocina: {lugar.tipo_cocina},\ningredientes: {lugar.ingredientes},\nprecio_minimo: {lugar.precio_minimo},\nprecio_maximo: {lugar.precio_maximo},\npopularidad: {lugar.popularidad}"
        self.lugar_label.configure(text=info)

    def cambiar_frame(self, frame_destino):
        frame_destino.tkraise()

    def agregar_marcador_mapa(self, latitud, longitud, texto, imagen=None):
        return self.mapa.set_marker(latitud, longitud, text=texto, image=imagen, command=self.controlador.seleccionar_ubicacion)
