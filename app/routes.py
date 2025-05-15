from flask import Blueprint, render_template, request, redirect, url_for
from . import mongo

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/patients', methods=['GET', 'POST'])
def patients():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        condition = request.form['condition']
        mongo.db.patients.insert_one({'name': name, 'age': age, 'condition': condition})
        return redirect(url_for('main.patients'))
    
    patients = mongo.db.patients.find()
    return render_template('patients.html', patients=patients)

@main.route('/appointments', methods=['GET', 'POST'])
def appointments():
    if request.method == 'POST':
        patient_name = request.form['patient_name']
        date = request.form['date']
        doctor = request.form['doctor']
        mongo.db.appointments.insert_one({'patient_name': patient_name, 'date': date, 'doctor': doctor})
        return redirect(url_for('main.appointments'))

    appointments = mongo.db.appointments.find()
    return render_template('appointments.html', appointments=appointments)
