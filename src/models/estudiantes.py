from src.connection_db.db import mysql


class StudentsModel():

    def createStudents(self, uid, nombre, apellido, telefono, email, semestre, curso):
        cursor = mysql.get_db().cursor()
        cursor.execute('INSERT INTO registro_estudiantes (uid, nombre,apellido,telefono,email,semestre, curso) VALUES (%s, %s,%s,%s,%s,%s,%s)',
                       (uid, nombre, apellido, telefono, email, semestre, curso,))
        mysql.get_db().commit()
        cursor.close()

    def deleteStudents(self, id):
        cursor = mysql.get_db().cursor()
        cursor.execute("DELETE FROM registro_estudiantes WHERE id = %s", (id,))
        mysql.get_db().commit()
        cursor.close()

    def listStudents(self):
        cursor = mysql.get_db().cursor()
        cursor.execute("SELECT * FROM registro_estudiantes")
        students = cursor.fetchall()
        cursor.close()
        return students

    def listStudentsUnique(self, id):
        cursor = mysql.get_db().cursor()
        cursor.execute(
            "SELECT * FROM registro_estudiantes WHERE id = %s", (id,))
        students = cursor.fetchone()
        cursor.close()
        return students

    def updateStudents(self, uid, nombre, apellido, telefono, email, semestre, curso, id):
        cursor = mysql.get_db().cursor()
        cursor.execute("UPDATE registro_estudiantes SET uid = %s, nombre = %s, apellido = %s, telefono = %s, email = %s, semestre = %s, curso = %s WHERE id = %s",
                    (uid, nombre, apellido, telefono, email, semestre, curso, id,))
        mysql.get_db().commit()
        cursor.close()


class CourseModel():
    def createCourse(self, materia, semestre):
        cursor = mysql.get_db().cursor()
        cursor.execute('INSERT INTO materias (materia,semestre) VALUES (%s,%s)',
                       (materia, semestre,))
        mysql.get_db().commit()
        cursor.close()

    def listCourses(self):
        cursor = mysql.get_db().cursor()
        cursor.execute("SELECT * FROM materias")
        courses = cursor.fetchall()
        cursor.close()
        return courses

    def deleteCourse(self, id):
        cursor = mysql.get_db().cursor()
        cursor.execute("DELETE FROM materias WHERE id = %s", (id,))
        mysql.get_db().commit()
        cursor.close()


class SessionModel():
    def createSession(self, course, date, starttime, endtime):
        cursor = mysql.get_db().cursor()
        cursor.execute('INSERT INTO session (course,date,start_time,end_time) VALUES (%s,%s,%s,%s)',
                       (course, date, starttime, endtime,))
        mysql.get_db().commit()
        cursor.close()

    def listSessions(self):
        cursor = mysql.get_db().cursor()
        cursor.execute("SELECT * FROM session")
        sessions = cursor.fetchall()
        cursor.close()
        return sessions

    def deleteSession(self, id):
        cursor = mysql.get_db().cursor()
        cursor.execute("DELETE FROM session WHERE id = %s", (id,))
        mysql.get_db().commit()
        cursor.close()
