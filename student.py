# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 18:56:26 2021

@author: SANA
"""
from person import Person

class Student(Person):
    def __init__(self, firstName, lastName, idNum, studentId, formClass):
        Person.__init__(self, firstName, lastName, idNum)
        self.studentId = studentId
        self.formClass = formClass
    

    def getFullInfo(self):
        return super().getFullInfo() + ' | Student ID: ' + self.studentId + ' | Form Class: ' + self.formClass
    
    
    
    def update(self, field, newValue):
        oldInfo = self.getFullInfo()
        if field == 1:
            self.firstName = newValue
        if field == 2:
            self.lastName = newValue
        if field == 3:
            self.idNum = newValue
        if field == 4:
            self.studentId = newValue
        if field == 5:
            self.formClass = newValue
        newInfo = self.getFullInfo()
        
        print ("Updated: \n" + oldInfo + "\nto:\n" + newInfo)