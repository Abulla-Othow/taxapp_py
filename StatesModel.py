from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app

#Create Database Object

db = SQLAlchemy(app)
class Tax(db.Model):
    __tablename__ = "states"
    id = db.Column(db.Integer,primary_key=True)
    stateAbbr = db.Column(db.String(2))
    stateName = db.Column(db.String(80)) 
    revenuePerCapita= db.Column(db.Float)
    revenuePerCapitaRank= db.Column(db.Float)