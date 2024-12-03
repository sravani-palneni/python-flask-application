# In flask, all the database information and the models are stored in a separate file called model.py
# It contains information regarding the table structure

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class EmployeeDetails(db.Model):          # A model in a python class represents a table in the database
    __tablename__ = "emp_table"
    
    employee_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    age = db.Column(db.Integer())
    position = db.Column(db.String(80))

    def __init__(self, employee_id, name, age, position):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.position = position

    def __repr__(self):
        return f"{self.name}:{self.employee_id}"
