class Empleado:
    def set_sucesor(self,sucesor):
        self.sucesor = sucesor
    def responder(self):
        pass

class Profesor(Empleado):
    def responder(self,reclamo):
        if reclamo.puntos < 2:
            print("Resuelve el Profesor")
            return True
        else:
            return self.sucesor.responder(reclamo)

class Coordinador(Empleado):
    def responder(self, reclamo):
        if reclamo.puntos < 5:
            print("Resuelve el Coordinador")
            return True
        else:
            return self.sucesor.responder(reclamo)

class SecretarioAcademico(Empleado):
    def responder(self, reclamo):
        if reclamo.puntos < 7:
            print("Resuelve el Secretario Academico")
            return True
        else:
            return self.sucesor.responder(reclamo)

class Director(Empleado):
    def responder(self,reclamo):
        print("Resuelve el Director")
        return True

class Reclamo:
    def __init__(self, puntos):
        self.puntos = puntos

def main():
    #Definir jerarquía 
    profesor = Profesor()
    coordinador = Coordinador()
    secretario = SecretarioAcademico()
    director = Director()

    profesor.set_sucesor(coordinador)
    coordinador.set_sucesor(secretario)
    secretario.set_sucesor(director)

    #Atención
    reclamo = Reclamo(3)
    profesor.responder(reclamo)

if __name__ == "__main__":
    main()
