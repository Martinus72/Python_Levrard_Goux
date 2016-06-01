import sqlite3
import json
import Installation as install
import Equipement as equipe
import Activite as activ

connexion = sqlite3.connect('paysdelaloire.db')

curseur = connexion.cursor()

curseur.execute("DROP TABLE IF EXISTS installation")
curseur.execute("DROP TABLE IF EXISTS equipement")
curseur.execute("DROP TABLE IF EXISTS equipement_activite")
curseur.execute("DROP TABLE IF EXISTS activite")

curseur.execute('''CREATE TABLE installation
             (numero INTEGER PRIMARY KEY, nom text, numeroRue text, rue text, code_postal text, ville text, latitude real, longitude real)''')

curseur.execute('''CREATE TABLE equipement
             (numero INTEGER PRIMARY KEY, nom text, numero_installation INTEGER, FOREIGN KEY(numero_installation) REFERENCES installation(numero))''')

curseur.execute('''CREATE TABLE activite
             (numero INTEGER PRIMARY KEY, nom text)''')

curseur.execute('''CREATE TABLE equipement_activite
             (numero_equipement INTEGER, numero_activite INTEGER, FOREIGN KEY(numero_equipement) REFERENCES equipement(numero), FOREIGN KEY(numero_activite) REFERENCES activite(numero))''')

connexion.commit()




with open("../bd_installations.json") as json_installation:

    json_installation_data = json.load(json_installation)

    for item in json_installation_data["data"]:
        installation = install.Installation(item["InsNumeroInstall"], item["InsPartLibelle"], item["InsNoVoie"], item["InsLibelleVoie"], item["InsCodePostal"], item["ComLib"], item["Latitude"], item["Longitude"])
        curseur.execute('''INSERT INTO installation VALUES (?, ?, ?, ?, ?, ?, ?,?)''', (installation.numero, installation.nom, installation.numeroRue, installation.rue, installation.code_postal, installation.ville, installation.latitude, installation.longitude))

connexion.commit()

print("Data Installation Finish")

#for row in curseur.execute('SELECT * FROM installation ORDER BY nom'):
#   print(row)

with open("../bd_equipements.json") as json_equipement:
    json_equipement_data = json.load(json_equipement)

    for item in json_equipement_data["data"]:
        equipement = equipe.Equipement(item["InsNumeroInstall"], item["EquipementId"], item["EquNom"])
        curseur.execute('''INSERT INTO equipement VALUES (?, ?, ?)''', ( equipement.numero_equipement, equipement.nom_equipement, equipement.numero_install ))

connexion.commit()

#for row in curseur.execute('SELECT * FROM equipement ORDER BY nom'):
#    print(row)

print("Data Equipement Finish")

with open("../bd_activites.json") as json_activite:
    json_activite_data = json.load(json_activite)

    for item in json_activite_data["data"]:
        activite = activ.Activite(item["ActCode"], item["ActLib"], item["EquipementId"])
        curseur.execute('''INSERT OR IGNORE INTO activite VALUES (?, ?)''', (activite.numero, activite.nom))
        curseur.execute('''INSERT INTO equipement_activite VALUES (?,?)''', (activite.numero_equipement, activite.numero))

connexion.commit()

print("Data Activite Finish")
print("Data Equipement_activite Finish")
#for row in curseur.execute('SELECT * FROM equipement_activite'):
#    print(row)

#requete = '''SELECT i.numero, i.nom, e.numero, e.nom, a.numero, a.nom FROM INSTALLATION i JOIN EQUIPEMENT e ON i.numero = e.numero_installation JOIN EQUIPEMENT_ACTIVITE ea ON e.numero = ea.numero_equipement JOIN ACTIVITE a ON ea.numero_activite = a.numero WHERE i.ville = 'Angers' AND a.nom LIKE '%Football%' '''

#for row in curseur.execute(requete):
#	print(row)

connexion.close()
