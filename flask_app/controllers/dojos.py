from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/dojos')
def all_dojos():

    dojos = Dojo.get_all_dojos()

    return render_template('dojos.html', dojos = dojos)

@app.route('/create/dojo', methods=['POST'])
def create_dojo():

    Dojo.create_dojo(request.form)

    return redirect('/dojos')

@app.route('/dojos/<int:dojo_id>')
def show_dojo(dojo_id):

    data = {
        'dojo_id'  :dojo_id
    }

    dojo = Dojo.get_one_dojo(data)

    return render_template('dojo_show.html', dojo = dojo)
