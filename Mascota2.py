from Mascota import Mascota

class Mascota2(Mascota):

    def __init__(self, name, tipo, golosinas):
        super().__init__(name, tipo, golosinas)
        self.salud = 85
        self.energia = 50


    def dormir(self):
        self.energia += 40
        print("Luego de dormir, la energía de",self.name,"es de:",self.energia,"puntos")