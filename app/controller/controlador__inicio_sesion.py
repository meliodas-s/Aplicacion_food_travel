from models.modelo__usuario import Usuario


class ControladorInicioSesion:
    def __init__(self, app) -> None:
        # Defino los colores
        self.c_naranja_quemado = '#FF5722'
        self.c_gris_azulado = '#607D8B'
        self.c_verde = '#4CAF50'
        self.c_gris_claro = '#EEEEEE'

        self.app = app
        self.usuarios = Usuario.cargar_de_json('data/usuarios.json')

    def comprobar_usuario(self):
        nombre_usuario = self.app.vista_inicio_sesion.entradas[0].get()
        contrasenna = self.app.vista_inicio_sesion.entradas[1].get()
        for usuario in self.usuarios:
            if nombre_usuario == usuario.nombre_usuario:
                if contrasenna == usuario.contrasenna:
                    self.ir_menu()
                    print('Nueva sesion inciada')
                    return {'Nombre Usuario': nombre_usuario, 'Id usuario': usuario.id}
                break
        else:
            print('Usuario o contraseña incorrectos')
            return False

    # Ir al menu inicio secion
    def ir_menu(self):
        self.app.cambiar_frame(self.app.vista_inicio)

    # Ir a la pestaña registrare
    def ir_registrarse(self):
        self.app.cambiar_frame(self.app.vista_registrarse)
