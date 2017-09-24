'''
Created on Sep 22, 2017

@author: mohommad_belal
'''

class Student_Util(object):
    '''
    classdocs
    '''

    def __init__(self):
        pass
        '''
        Constructor
        '''

    def save_Details_To_DB(self, student):
        #connection
        print(student)
        print("creating connection")
        #cursor
        print("create cursor")
        #insert student
        print("inserting data")
        #check
        print("checking the validation")
        #con close
        result = "pass"
        a = 3
        if a >= 5:
            result = "fail"
        print("returning the result")
        return result

    def update_Details_To_DB(self, student_id, student):
        print(student)
        print(student_id)
        return "success"

    def delete_Details_From_DB(self,student_id):
        print(student_id)
        return "success"

    def retreive_Details_From_DB(self):
        print("Get Student list from databse")

    def retreive_Details_From_DB_By_Id(self, trainer_id):
        print("Get Student details by ID")
