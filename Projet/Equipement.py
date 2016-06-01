class Equipement:


    def __init__(self, numero_install, numero_equipement, nom_equipement):
    	self.numero_install = numero_install
    	self.numero_equipement = numero_equipement
    	self.nom_equipement = nom_equipement

    def display_numero_install(self):
        return str(self.numero_install)

    def set_numero_install(self, nouveau_numero):
        self.numero_install = nouveau_numero

    def display_numero_equipement(self):
        return str(self.numero_equipement)

    def set_numero_equipement(self, nouveau_numero_equipement):
        self.numero_equipement = nouveau_numero_equipement

    def display_nom_equipement(self):
        return str(self.nom_equipement)

    def set_nom_equipement(self, nouveau_nom_equipement):
        self.nom_equipement = nouveau_nom_equipement
