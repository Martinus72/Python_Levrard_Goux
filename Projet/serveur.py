from bottle import get, post, request, run, template, route, static_file
import sqlite3

"""
File create and manage a bottle server
"""

# Creation or/and connection to the database
connexion = sqlite3.connect('paysdelaloire.db')

cursor = connexion.cursor()

@route('/static/<filename>', name='static')
def server_static(filename):
    return static_file(filename, root='static')

@get('/')
def form():

    cursor.execute("SELECT DISTINCT city FROM installation ORDER BY city asc")
    city_tab = cursor.fetchall()

    cursor.execute("SELECT DISTINCT name FROM activity ORDER BY name asc")
    activity_tab = cursor.fetchall()

    return template('templates/template', city_tab = city_tab, activity_tab = activity_tab)


@post('/')
def do_search():
    activity = str(request.forms.get('activity')).decode('utf-8')
    city = str(request.forms.get('city')).decode('utf-8')

    if city == "empty" and activity == "empty":
        answer_list = []
    elif activity == "empty":
        cursor.execute("SELECT i.name, e.name, a.name, i.city, i.id FROM INSTALLATION i JOIN EQUIPEMENT e ON i.id = e.installation_id JOIN EQUIPEMENT_ACTIVITY ea ON e.id = ea.equipement_id JOIN activity a ON ea.activity_id = a.id WHERE i.city = ?", (city,))
        answer_list = cursor.fetchall()
    elif city == "empty":
        cursor.execute("SELECT i.name, e.name, a.name, i.city, i.id FROM INSTALLATION i JOIN EQUIPEMENT e ON i.id = e.installation_id JOIN EQUIPEMENT_ACTIVITY ea ON e.id = ea.equipement_id JOIN activity a ON ea.activity_id = a.id WHERE a.name LIKE '%"+activity+"%'")
        answer_list = cursor.fetchall()
    else:
        cursor.execute("SELECT i.name, e.name, a.name, i.city, i.id FROM INSTALLATION i JOIN EQUIPEMENT e ON i.id = e.installation_id JOIN EQUIPEMENT_ACTIVITY ea ON e.id = ea.equipement_id JOIN activity a ON ea.activity_id = a.id WHERE i.city = ? AND a.name LIKE '%"+activity+"%'", (city,))
        answer_list = cursor.fetchall()

    return template('templates/template2', answer = answer_list)

@get('/maps/<id_installation>')
def build_maps(id_installation):
    cursor.execute("SELECT i.name, i.city,i.postcode, i.streetNumber,i.street, i.latitude , i.longitude  FROM INSTALLATION i WHERE i.id = ? ", (id_installation,))
    answer_list = cursor.fetchall()

    return template('templates/template3', answer = answer_list)


run(host='localhost', port=8080)
