from flask_sqlalchemy import SQLAlchemy 

from app import db                                         


class Employee(db.Model):
    __tablename__ = 'employee'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    age = db.Column(db.String())
    dept = db.Column(db.String())

    def __init__(self, name, age, dept):
        self.name = name
        self.age = age
        self.dept = dept

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'name': self.name,
            'age': self.age,
            'dept':self.dept
        }

