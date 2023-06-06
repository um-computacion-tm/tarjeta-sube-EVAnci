class NoHaySaldoException(Exception):
    pass

class EstadoNoExistenteException(Exception):
    pass

class UsuarioDesactivadoException(Exception):
    pass

PRECIO_TICKET = 70
PRIMARIO = 0.5
SECUNDARIO = 0.6
UNIVERSITARIO = 0.7
JUBILADO = 0.75

ACTIVADO = 'activado'
DESACTIVADO = 'desactivado'

class Sube():
    def __init__(self):
        self.saldo = 0
        self.grupo_beneficiario = None
        self.estado = 'activado'

    def obtener_precio_ticket(self):
        if self.grupo_beneficiario != None:
            self.precio_ticket = PRECIO_TICKET * self.grupo_beneficiario
        else:
            self.precio_ticket = PRECIO_TICKET
        return self.precio_ticket

    def pagar_pasaje(self):
        if self.estado == 'activado':
            costo = self.obtener_precio_ticket()
            if self.saldo >= costo:
                self.saldo -= costo
            else:
                raise NoHaySaldoException()
        else:
            raise UsuarioDesactivadoException()

    def cambiar_estado(self, estado):
        if estado != 'pendiente':
            self.estado = estado
        else:
            raise EstadoNoExistenteException()