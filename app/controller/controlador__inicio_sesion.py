from models.modelo__usuario import Usuario


class ControladorInicioSesion:
    def __init__(self) -> None:
        # Defino los colores
        self.c_naranja_quemado = '#FF5722'
        self.c_gris_azulado = '#607D8B'
        self.c_verde = '#4CAF50'
        self.c_gris_claro = '#EEEEEE'

        self.usuarios = Usuario.cargar_de_json('data/usuarios.json')
    
    def comprobar_usuario(self, nombre_usuario, contrasenna):
        for usuario in self.usuarios:
            if nombre_usuario == usuario.nombre_usuario:
                if contrasenna == usuario.contrasenna:
                    return {'Nombre Usuario': nombre_usuario, 'Id usuario': usuario.id}
                break
        else:
            return False
        