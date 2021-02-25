# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 18:56:56 2021

@author: SANA
"""

class Person(object):
    def __init__(self, firstName, lastName, idNum):
        self.firstName = firstName
        self.lastName = lastName
        self.idNum = idNum
    

    def getFullName(self):
        return self.firstName + ' ' + self.lastName
    
    def getFullInfo(self):
        return 'Name: ' + self.firstName + ' ' + self.lastName + ' | ID: ' + self.idNum