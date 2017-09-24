'''
Created on Sep 23, 2017

@author: mohommad_belal
'''

class CourseUtil(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        pass
        '''
        Constructor
        '''

    def save_Details_To_DB(self, details):
        #connection
        print(details)
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

    def update_Details_To_DB(self, detail_id, details):
        print(details)
        print(detail_id)
        return "success"

    def delete_Details_From_DB(self,detail_id):
        print(detail_id)
        return "success"

    def retreive_Details_From_DB(self):
        print("Get Student list from databse")

    def retreive_Details_From_DB_By_Id(self, detail_id):
        print("Get Student details by ID")
