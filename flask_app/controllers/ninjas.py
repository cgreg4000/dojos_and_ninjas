from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def ninjas():

    dojos = Dojo.get_all_dojos()

    return render_template('new_ninja.html', dojos=dojos)

@app.route('/create/ninja', methods=['POST'])
def create_ninja():

    Ninja.create_ninja(request.form)

    return redirect(f"/dojos/{request.form['dojo_id']}")
