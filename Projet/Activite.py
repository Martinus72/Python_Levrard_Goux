class Activite:


    def __init__(self, numero, nom, numero_equipement):
        self.numero = numero
        self.nom = nom
        self.numero_equipement = numero_equipement


    def display_numero(self):
        return str(self.numero)

    def set_numero(self, nouveau_numero):
        self.numero = nouveau_numero

    def display_nom(self):
        return str(self.nom)

    def set_nom(self, nouveau_nom):
        self.nom = nouveau_nom
