# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 18:56:40 2021

@author: SANA
"""

from person import Person
class Teacher(Person):
    def __init__(self, firstName, lastName, idNum, staffId, dept):
        Person.__init__(self, firstName, lastName, idNum)
        self.staffId = staffId
        self.dept = dept
        
    def getFullInfo(self):
        return super().getFullInfo() + ' | Staff ID: ' + self.staffId + ' | Department: ' + self.dept
    
    def update(self, field, newValue):
        oldInfo = self.getFullInfo()
        if field == 1:
            self.firstName = newValue
        if field == 2:
            self.lastName = newValue
        if field == 3:
            self.idNum = newValue
        if field == 4:
            self.staffId = newValue
        if field == 5:
            self.dept = newValue
        newInfo = self.getFullInfo()
        
        print ("Updated: \n" + oldInfo + "\nto:\n" + newInfo)