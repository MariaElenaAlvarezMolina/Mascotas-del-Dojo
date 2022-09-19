class Mascota:

    def __init__(self, name, tipo, golosinas):
        self.name = name
        self.tipo = tipo
        self.golosinas = golosinas
        self.salud = 85
        self.energia = 50


    def dormir(self):
        self.energia += 25
        print("Luego de dormir, la energía de",self.name,"es de:",self.energia,"puntos")

    def comer(self):
        self.energia += 5
        print("Después de comer",self.golosinas,"la energía de",self.name,"es de:",self.energia,"puntos")
        self.salud += 10
        print("Después de comer",self.golosinas,"la salud de",self.name,"se eleva a:",self.salud,"puntos")

    def jugar(self):
        self.salud += 5
        print("Después de jugar, la salud de",self.name,"se eleva a:",self.salud,"puntos")

    def sonido(self):
        if self.salud >= 95:
            print(self.name,"está feliz y sano y dice fuerte 'woof!'")
        else:
            print(self.name,"necesita comer y dormir")