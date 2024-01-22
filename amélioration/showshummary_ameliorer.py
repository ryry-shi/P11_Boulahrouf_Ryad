import json
from flask import Flask,render_template,request, flash
import server

clubs = server.loadClubs()
competitions = server.loadCompetitions()


def showSummary():
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
        return render_template('welcome.html',club=club,competitions=competitions)
    except IndexError:
        flash("Désolé, cet e-mail n'a pas été trouvé")
        return render_template('index.html')