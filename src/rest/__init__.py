from flask import Flask, jsonify
from flask.globals import request
from beans.Trainer import Trainer
from util.TrainerUtil import TrainerUtil


app = Flask(__name__)

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

@app.route('/students', methods = ['POST'])
def saveStudentDetails():
    #Save the data to database
    student = request.get_json()
    print("Saving the Data to DataBase")
    print(student)
    return "Success"
if __name__ == '__main__':
    app.run()
