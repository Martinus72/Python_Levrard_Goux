<!DOCTYPE html>
<html>
    <head>
        <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
        <!--Mon Javascript-->
        <script type="text/javascript" src="/static/maps.js"></script>

        <!--Librairie Gmaps.js-->
        <script src="http://maps.google.com/maps/api/js?v=3&amp"></script>
        <script src="/static/gmaps.js"></script>

        <!--Bootstrap-->
        <!-- Latest compiled and minified CSS -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">

        <!-- Optional theme -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap-theme.min.css" integrity="sha384-fLW2N01lMqjakBkx3l/M9EahuwpSfeNvV63J5ezn3uZzapT0u7EYsXMjQV+0En5r" crossorigin="anonymous">

        <!-- Latest compiled and minified JavaScript -->
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js" integrity="sha384-0mSbJDEHialfmuBBQP6A4Qrprq5OVfW37PRR3j5ELqxss1yVqOtnepnHVP9aJ7xS" crossorigin="anonymous"></script>

        <link rel="stylesheet" href="/static/style.css" type="text/css">

    </head>
    <body>
        <div class="row">
            <div class="col-lg-1"></div>
            <div class="col-lg-10">
            <h1>Sport Advisor</h1>
            <form action="http://localhost:8080/">
                <label for="mySubmit" class="btn"><i class="glyphicon glyphicon-search"></i> Nouvelle Recherche</label>
                <input id="mySubmit" type="submit" value="Go" class="hidden" />
            </form>
            %if len(answer) > 0:
            <table class="table">
                <thead>
                    <tr>
                        <th>Nom de l'installation</th>
                        <th>Equipement</th>
                        <th>Activité</th>
                        <th>Ville</th>
                        <th>Map</th>
                    </tr>
                </thead>
                <tbody>
                    %for option in answer:
                        <tr>
                            <td>{{option[0]}}</td>
                            <td>{{option[1]}}</td>
                            <td>{{option[2]}}</td>
                            <td>{{option[3]}}</td>
                            <td><a href="./maps/{{option[4]}}">Let's go</a></td>
                        </tr>
                    %end
                </tbody>
            </table>
            %else:
                <p> Il n'y a pas de résultat pour votre requête</p>
            %end
            </div>
        </div>
    </body>
</html>
