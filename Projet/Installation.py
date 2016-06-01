class Installation:


    def __init__(self, numero, nom, numeroRue,rue, code_postal, ville, latitude, longitude):
        self.numero = numero
        self.nom = nom
        self.numeroRue = numeroRue
        self.rue = rue
        self.code_postal = code_postal
        self.ville = ville
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return "{} - {}".format(self.numero, self.nom)

    def display_numero(self):
        return str(self.numero)

    def set_numero(self, t):
        self.numero = t

    def display_nom(self):
        return str(self.nom)

    def set_nom(self, t):
        self.nom = t

    def display_numeroRue(self):
        return str(self.adresse)

    def set_numeroRue(self, t):
        self.adresse = t

    def display_rue(self):
        return str(self.adresse)

    def set_rue(self, t):
        self.adresse = t

    def display_code_postal(self):
        return str(self.code_postal)

    def set_code_potstal(self, t):
        self.code_postal = t

    def display_ville(self):
        return str(self.ville)

    def set_ville(self, t):
        self.ville = t

    def display_latitude(self):
        return str(self.latitude)

    def set_latitude(self, t):
        self.latitude = t

    def display_longitude(self):
        return str(self.longitude)

    def set_longitude(self, t):
        self.longitude = t