from src import app
from src.controllers.estudiantes import StudentsController, CourseController, SessionController
from flask import make_response, session, jsonify, request, render_template, redirect, flash, url_for

studentsController = StudentsController()
courseController = CourseController()
sessionController = SessionController()


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/crearMaterias', methods=['POST', 'GET'])
def createCourse():

    materia = request.form['materia']
    semestre = request.form['semestre']  

    courseController.createCourse(materia, semestre)
    return render_template('materias/create.html')


@app.route('/materias/list', methods=['POST', 'GET'])
def listCourses():
    courses = courseController.listCourses()
    return render_template('materias/list.html', courses=courses)


@app.route('/course/delete/<id>', methods=['POST', 'GET'])
def deleteCourse(id):
    courseController.deleteCourse(id)
    return redirect(url_for('listCourses'))

@app.route('/crearEstudiantes', methods=['POST', 'GET'])
def crearEstudiantes():
    courses = courseController.listCourses()
    print(courses)
    return render_template('estudiantes/create.html', courses=courses)


@app.route('/student', methods=['POST', 'GET'])
def createStudent():
    uid = request.form['uid']
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    telefono = request.form['telefono']
    email = request.form['email']
    semestre = request.form['semestre']
    curso = request.form['curso']

    studentsController.createStudents(
        uid, nombre, apellido, telefono, email, semestre, curso)
    return redirect(url_for('crearEstudiantes'))


@app.route('/student/list', methods=['POST', 'GET'])
def listStudent():
    students = studentsController.listStudents()
    return render_template('estudiantes/list.html', students=students)


@app.route('/delete/<id>', methods=['POST', 'GET'])
def deleteStudent(id):
    studentsController.deleteStudents(id)
    return redirect(url_for('listStudent'))


@app.route('/updatetemp/<id>', methods=['POST', 'GET'])
def updateStudentTemp(id):
    students = studentsController.listStudentsUnique(id)
    id = students[0]
    uid = students[1]
    nombre = students[2]
    apellido = students[3]
    telefono = students[4]
    email = students[5]
    semestre = students[6]
    curso = students[7]
    print(students)

    return render_template('estudiantes/update.html', id=id, uid=uid, nombre=nombre, apellido=apellido, telefono=telefono, email=email, semestre=semestre, curso=curso)


@app.route('/update/<id>', methods=['PUT', 'GET', 'POST'])
def updateStudent(id):
    uid = request.form['uid']
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    telefono = request.form['telefono']
    email = request.form['email']
    semestre = request.form['semestre']
    curso = request.form['curso']
    studentsController.updateStudents(uid,nombre,apellido,telefono,email,semestre,curso,id)
    return redirect(url_for('listStudent'))

@app.route('/session/create', methods=['POST', 'GET'])
def createSession():
    course = request.form['course']
    date = request.form['date']
    starttime = request.form['starttime']
    endtime = request.form['endtime']

    sessionController.createSession(course, date, starttime, endtime)

    return redirect(url_for('listSessionPreview'))


@app.route('/crearSesiones', methods=['POST', 'GET'])
def crearSesiones():
    courses = courseController.listCourses()
    return render_template('sesiones/create.html', courses=courses)


@app.route('/crearSesion', methods=['POST', 'GET'])
def listSessionPreview():
    sessions = sessionController.listSessions()
    return render_template('sesiones/list.html', sessions=sessions)


@app.route('/session/delete/<id>', methods=['POST', 'GET'])
def deleteSession(id):
    sessionController.deleteSession(id)
    return redirect(url_for('listSessionPreview'))
