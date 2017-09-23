'''
Created on Sep 23, 2017

@author: mohommad_belal
'''

class LibraryUtil(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        pass

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

    def retreive_Details_From_DB(self, key_word):
        print("Get Book list from databse based on key_word")

    def retreive_Details_From_DB_By_Id(self, book_id):
        print("Get ebook value by ID")

