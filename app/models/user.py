class Usuario:
    def __init__(self, id, nombre, correo, rol_id):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.rol_id = rol_id

    def es_administrador(self):
        return self.rol_id == 1
