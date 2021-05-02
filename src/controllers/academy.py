from flask import render_template
from src import app

@app.route('/student')
def students():
    return render_template('students/create.html')

@app.route('/crearMaterias')
def courses():
    return render_template('materias/create.html')

@app.route('/session')
def session():
    return render_template('sessions/list.html')

@app.route('/session/create')
def sessionsNew():
    return render_template('sessions/create.html')