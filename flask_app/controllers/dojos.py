from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/dojos')
def all_dojos():

    dojos = Dojo.get_all_dojos()

    return render_template('dojos.html', dojos = dojos)