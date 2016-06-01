import sqlite3
import json
import Installation as install
import Equipement as equipe
import Activity as activ

"""
File which allows to create the database
"""

# Creation or/and connection to the database
connection = sqlite3.connect('paysdelaloire.db')

cursor = connection.cursor()

# Clean database before updates
cursor.execute("DROP TABLE IF EXISTS installation")
cursor.execute("DROP TABLE IF EXISTS equipement")
cursor.execute("DROP TABLE IF EXISTS equipement_activity")
cursor.execute("DROP TABLE IF EXISTS activity")

cursor.execute('''CREATE TABLE installation
             (id INTEGER PRIMARY KEY, name text, streetNumber text, street text, postcode text, city text, latitude real, longitude real)''')

cursor.execute('''CREATE TABLE equipement
             (id INTEGER PRIMARY KEY, name text, installation_id INTEGER, FOREIGN KEY(installation_id) REFERENCES installation(id))''')

cursor.execute('''CREATE TABLE activity
             (id INTEGER PRIMARY KEY, name text)''')

cursor.execute('''CREATE TABLE equipement_activity
             (equipement_id INTEGER, activity_id INTEGER, FOREIGN KEY(equipement_id) REFERENCES equipement(id), FOREIGN KEY(activity_id) REFERENCES activity(id))''')

connection.commit()


# installation table data insertion
with open("../bd_installations.json") as json_installation:

    json_installation_data = json.load(json_installation)

    for item in json_installation_data["data"]:
        installation = install.Installation(item["InsNumeroInstall"], item["InsPartLibelle"], item["InsNoVoie"], item["InsLibelleVoie"], item["InsCodePostal"], item["ComLib"], item["Latitude"], item["Longitude"])
        cursor.execute('''INSERT INTO installation VALUES (?, ?, ?, ?, ?, ?, ?,?)''', (installation.id, installation.name, installation.streetNumber, installation.street, installation.postcode, installation.city, installation.latitude, installation.longitude))

connection.commit()

print("Data Installation Finish")


# equipement table data insertion
with open("../bd_equipements.json") as json_equipement:
    json_equipement_data = json.load(json_equipement)

    for item in json_equipement_data["data"]:
        equipement = equipe.Equipement(item["InsNumeroInstall"], item["EquipementId"], item["EquNom"])
        cursor.execute('''INSERT INTO equipement VALUES (?, ?, ?)''', ( equipement.equipement_id, equipement.name, equipement.installation_id ))

connection.commit()

print("Data Equipement Finish")

# activity table data insertion
with open("../bd_activites.json") as json_activity:
    json_activity_data = json.load(json_activity)

    for item in json_activity_data["data"]:
        activity = activ.Activity(item["ActCode"], item["ActLib"], item["EquipementId"])
        cursor.execute('''INSERT OR IGNORE INTO activity VALUES (?, ?)''', (activity.id, activity.name))
        cursor.execute('''INSERT INTO equipement_activity VALUES (?,?)''', (activity.equipement_id, activity.id))

connection.commit()

print("Data activity Finish")
print("Data equipement_activity Finish")

connection.close()
