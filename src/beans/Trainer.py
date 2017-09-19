'''
Created on Sep 17, 2017

@author: mohommad_belal
'''


class Trainer(object):
    '''
    classdocs
    '''

    trainer_id = 0
    name ="boy"
    age =-1
    email = ""
    phone = ""
    gender =""
    dob = ""
    address = ""

    def setTrainer(self,trainerTup):
        print(trainerTup)
        self.trainer_id,self.name,self.age,self.email,self.phone,self.gender,self.dob,self.address = trainerTup

    def display(self):
        print(self.trainer_id,self.name,self.age,self.email,self.phone,self.gender,self.dob,self.email,self.address)

    def __init__(self):
        '''
        Constructor
        '''
        self.__name = "Belal"
        print(self.__name)





