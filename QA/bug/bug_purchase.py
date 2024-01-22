from fichier_client import client
from flask import app, render_template, request, flash
import server

clubs = server.loadClubs()
competitions = server.loadCompetitions()

def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])
    ##Divers bug aucunes restriction pour ne pas mettre de nombre négatif
    ##Ou ne pas mettre un nombre dans le formulaire supérieur au nombre de place que possède l'utilisateur
    ##Ou prendre plus de place que possède qu'il y en a dans la compétition
    competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
    flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)

