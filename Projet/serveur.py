from bottle import get, post, request, run, template, route, static_file
import sqlite3


connexion = sqlite3.connect('paysdelaloire.db')

curseur = connexion.cursor()

@route('/static/<filename>', name='static')
def server_static(filename):
    return static_file(filename, root='static')

@get('/')
def form():

    curseur.execute("SELECT DISTINCT ville FROM installation ORDER BY ville asc")
    city_tab = curseur.fetchall()

    curseur.execute("SELECT DISTINCT nom FROM activite ORDER BY nom asc")
    activity_tab = curseur.fetchall()

    return template('template', city_tab = city_tab, activity_tab = activity_tab)


@post('/')
def do_recherche():
    activite = str(request.forms.get('activity')).decode('utf-8')
    ville = str(request.forms.get('city')).decode('utf-8')

    if ville == "empty" and activite == "empty":
        answer_list = []
    elif activite == "empty":
        curseur.execute("SELECT i.nom, e.nom, a.nom, i.ville, i.numero FROM INSTALLATION i JOIN EQUIPEMENT e ON i.numero = e.numero_installation JOIN EQUIPEMENT_ACTIVITE ea ON e.numero = ea.numero_equipement JOIN ACTIVITE a ON ea.numero_activite = a.numero WHERE i.ville = ?", (ville,))
        answer_list = curseur.fetchall()
    elif ville == "empty":
        curseur.execute("SELECT i.nom, e.nom, a.nom, i.ville, i.numero FROM INSTALLATION i JOIN EQUIPEMENT e ON i.numero = e.numero_installation JOIN EQUIPEMENT_ACTIVITE ea ON e.numero = ea.numero_equipement JOIN ACTIVITE a ON ea.numero_activite = a.numero WHERE a.nom LIKE '%"+activite+"%'")
        answer_list = curseur.fetchall()
    else:
        curseur.execute("SELECT i.nom, e.nom, a.nom, i.ville, i.numero FROM INSTALLATION i JOIN EQUIPEMENT e ON i.numero = e.numero_installation JOIN EQUIPEMENT_ACTIVITE ea ON e.numero = ea.numero_equipement JOIN ACTIVITE a ON ea.numero_activite = a.numero WHERE i.ville = ? AND a.nom LIKE '%"+activite+"%'", (ville,))
        answer_list = curseur.fetchall()

    return template('template2', answer = answer_list)

@get('/maps/<id_installation>')
def build_maps(id_installation):
    curseur.execute("SELECT i.nom, i.ville,i.code_postal, i.numeroRue,i.rue, i.latitude , i.longitude  FROM INSTALLATION i WHERE i.numero = ? ", (id_installation,))
    answer_list = curseur.fetchall()

    return template('template3', answer = answer_list)


run(host='localhost', port=8080)
