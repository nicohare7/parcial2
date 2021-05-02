from src.models.estudiantes import StudentsModel, CourseModel, SessionModel

studentsModel = StudentsModel()
courseModel = CourseModel()
sessionModel = SessionModel()


class StudentsController():

    def createStudents(self, uid, nombre, apellido, telefono, email, semestre, curso):
        studentsModel.createStudents(
            uid, nombre, apellido, telefono, email, semestre, curso)

    def listStudents(self):
        return studentsModel.listStudents()

    def deleteStudents(self, id):
        studentsModel.deleteStudents(id)

    def listStudentsUnique(self, id):
        return studentsModel.listStudentsUnique(id)

    def updateStudents(self, uid, nombre, apellido, telefono, email, semestre, curso, id):
        studentsModel.updateStudents(
            uid, nombre, apellido, telefono, email, semestre, curso, id)

class CourseController():

    def createCourse(self, materia, semestre):
        courseModel.createCourse(materia, semestre)

    def listCourses(self):
        return courseModel.listCourses()

    def deleteCourse(self, id):
        courseModel.deleteCourse(id)


class SessionController():

    def createSession(self, course, date, starttime, endtime):
        sessionModel.createSession(course, date, starttime, endtime)

    def listSessions(self):
        return sessionModel.listSessions()

    def deleteSession(self, id):
        sessionModel.deleteSession(id)
