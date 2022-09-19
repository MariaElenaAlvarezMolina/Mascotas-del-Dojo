from Mascota import Mascota

class Ninja:

    def __init__(self, nombre, apellido, premio, comida_mascota, name, tipo, golosinas):
        self.nombre = nombre
        self.apellido = apellido
        self.premio = premio
        self.comida_mascota = comida_mascota
        self.mascota = Mascota("Rocky", "perro", "croquetas")


    def caminar(self):
        if self.mascota.salud >= 95:
            print(self.nombre,self.apellido,"sacará a pasear a",self.mascota.name,"y le dará un",self.premio)
        else:
            print(self.mascota.name,"no está listo para pasear aún")

    def alimentar(self):
        if (self.mascota.energia <= 75 and self.mascota.salud <= 85):
            print(self.nombre,self.apellido,"debe alimentar a",self.mascota.name,"con",self.comida_mascota)
        else:
            print(self.mascota.name,"ya ha comido suficiente")

    def bañar(self):
        if self.mascota.salud > 95:
            print(self.mascota.name,"ya está listo para que",self.nombre,self.apellido,"le de un baño")
        else:
            print(self.mascota.name,"aún no está listo para que",self.nombre,self.apellido,"le de un baño")