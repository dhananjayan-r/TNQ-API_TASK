import csv
import json
from flask.json import jsonify

class calculator:
    def __init__(self):
        print("done")

    def _compute(self,a,b):
        temp = {}
        #Addition
        add = a+b
        temp['Added'] = add
        print ("Addition: %d" %add)
        #Subtraction
        sub = a - b
        temp['Subtracted'] = sub
        print ("Subtraction: %d" %sub)
        #Multiplication
        mul = a * b
        temp['Multiplication'] = mul
        print ("Multiplication: %d" %mul)
        #Division
        div = a / b
        temp['Division'] = div
        print ("Division: %.2f" %div)   

        return temp    

        


