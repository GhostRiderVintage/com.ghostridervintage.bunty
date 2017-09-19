'''
Created on Sep 19, 2017

@author: mohommad_belal
'''
from beans.Trainer import Trainer
from util.TrainerUtil import TrainerUtil

from rest import app
from flask.globals import request

class MyClass(object):
    '''
    classdocs
    '''
    trainer_beans = Trainer()


    def __init__(self, params):
        '''
        Constructor
        '''
