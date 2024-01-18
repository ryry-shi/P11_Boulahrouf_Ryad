import server
from flask import render_template, flash, app, request

competitions = server.loadCompetitions()
clubs = server.loadClubs()


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])
    ##Divers bug aucunes restriction pour ne pas mettre de nombre négatif ou une string
    ##Ou ne pas mettre un nombre dans le formulaire supérieur au nombre de place que possède l'utilisateur
    ##Ou prendre plus de place que possède qu'il y en a dans la compétition
    competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
    flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)

