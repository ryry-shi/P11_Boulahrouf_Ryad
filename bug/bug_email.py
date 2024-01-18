import server
from flask import render_template, app, request

competitions = server.loadCompetitions()
clubs = server.loadClubs()

@app.route('/showSummary',methods=['POST'])
def showSummary():
    club = [club for club in clubs if club['email'] == request.form['email']][0]
    ## bug Lorsque on tape une mauvaise adresse email aucune restriction
    return render_template('welcome.html',club=club,competitions=competitions)
