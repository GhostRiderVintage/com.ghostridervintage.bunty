from flask import Flask, jsonify
from flask.globals import request
from util import Student_Util,CourseUtil,LibraryUtil,SchedulingUtil,SkillUtil, ElearningUtil, TrainerUtil,CertificateUtil
from builtins import str

app = Flask(__name__)
s_util = Student_Util.Student_Util()
c_util = CourseUtil.CourseUtil()
cer_util = CertificateUtil.CertificateUtil()
l_util = LibraryUtil.LibraryUtil()
sc_util = SchedulingUtil.SchedulingUtil()
e_util = ElearningUtil.ElearningUtil()
t_util = TrainerUtil.TrainerUtil()
skill_util = SkillUtil.SkillUtil()
@app.route('/hello')
def hello():
    return "Hello Bhootnike"

@app.route('/bye')
def bye():
    return "Bye Bhootnike"

@app.route('/hi', methods = ["POST"])
def sayHi():
    print("hi")
    return jsonify({"1":"Belal", "2":"Aftab"})

#Student
@app.route('/students', methods = ['POST'])
def insertStudentDetails():
    #Save the data to database
    student = request.get_json()
    print(student)
    print("Saving the Data to DataBase")
    result = s_util.save_Details_To_DB(student)
    return result

@app.route('/students/<student_id>', methods = ['PUT'])
def updateStudentDetails(student_id):
    #Update the data to database)
    student = request.get_json()
    print("Updating the Data to DataBase")
    result = s_util.update_Details_To_DB(student_id, student)
    return result

@app.route('/students/<student_id>', methods = ['DELETE'])
def deleteStudentDetails(student_id):
    #delete the data from database
    result = s_util.delete_Details_From_DB(student_id)
    return result

@app.route('/students', methods = ['GET'])
def retreiveAllStudentDetails():
    #Retreive the from from database
    result = s_util.retreive_Details_From_DB()
    return result

@app.route('/students/<student_id>', methods = ['GET'])
def retreiveStudentDetailsById(student_id):
    #Update the data to database
    result = s_util.retreive_Details_From_DB_By_Id(student_id)
    return result

#Courses
@app.route('/courses/<trainer_id>/<course_id>', methods = ['PUT'])
def updateCourseTrainerTable(trainer_id, course_id):
    print("update course-trainer table")
    data = request.get_json()
    result = c_util.update_Details_To_DB(trainer_id, course_id, data)
    return result

@app.route('/courses/<trainer_id>', methods = ['GET'])
def retreiveAllCourseDetailsForTrainer(trainer_id):
    #Retreive the from from database
    result = c_util.retreive_Details_From_DB(trainer_id)
    return result

@app.route('/courses/<trainer_id>/<course_id>', methods = ['GET'])
def retreiveCourseDetailsForTrainer(trainer_id, course_id):
    #Update the data to database
    result = c_util.retreive_Details_From_DB_By_Id(trainer_id, course_id)
    return result

#Scheduling
@app.route('/scheduling/<trainer_id>', methods = ['GET'])
def retreiveAllTimeTables(trainer_id):
    #Update the data to database
    result = sc_util.retreive_Details_From_DB_By_Id(trainer_id)
    return result

#Library
@app.route('/library/<key_word>', methods = ['GET'])
def retreiveAllBooks(key_word):
    #Retreive the from from database
    result = l_util.retreive_Details_From_DB(key_word)
    return result

@app.route('/library/<book_id>', methods = ['GET'])
def retreiveEbookByID(book_id):
    #Update the data to database
    result = l_util.retreive_Details_From_DB_By_Id(book_id)
    return result

#E-Learning
@app.route('/elearning', methods = ['GET'])
def retreiveAllELearning():
    #Retreive the from from database
    result = e_util.retreive_Details_From_DB()
    return result

@app.route('/elearning/<elearning_id>', methods = ['GET'])
def retreiveELearningByID(elearning_id):
    #Update the data to database
    result = e_util.retreive_Details_From_DB_By_Id(elearning_id)
    return result

@app.route('/elearning/<trainer_id>/<elearning_id>', methods = ['PUT'])
def updateELearningTrainerTable(trainer_id, elearning_id):
    print("update course-trainer table")
    data = request.get_json()
    result = e_util.update_Details_To_DB(trainer_id, elearning_id, data)
    return result

#Certification
@app.route('/certificates', methods = ['GET'])
def retreiveAllCertificates():
    #Retreive the from from database
    result = cer_util.retreive_Details_From_DB()
    return result

@app.route('/certificates/<certificate_id>', methods = ['GET'])
def retreiveCertificateByID(certificate_id):
    #Update the data to database
    result = cer_util.retreive_Details_From_DB_By_Id(certificate_id)
    return result

@app.route('/certificates/<trainer_id>/<certificate_id>', methods = ['PUT'])
def updateCertificateTrainerTable(trainer_id, certificate_id):
    print("update course-trainer table")
    data = request.get_json()
    result = cer_util.update_Details_To_DB(trainer_id, certificate_id, data)
    return result

#trainer
@app.route('/trainers', methods = ['GET'])
def retreiveAllTrainer():
    #Retreive the from from database
    result = t_util.retreive_Details_From_DB()
    return result

@app.route('/trainers/<trainer_id>', methods = ['GET'])
def retreiveTrainerByID(trainer_id):
    #Update the data to database
    result = t_util.retreive_Details_From_DB_By_Id(trainer_id)
    return result

@app.route('/skills/<trainer_id>', methods = ['GET'])
def retreiveTrainerSkillsById(trainer_id):
    result = skill_util.retreive_Details_From_DB_By_Id(trainer_id)
    return result

if __name__ == '__main__':
    app.run()
