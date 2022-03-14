from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import ForeignKey
from wtforms import HiddenField, StringField, SubmitField, DateField, SelectField
from wtforms.validators import InputRequired, Length, Regexp, NumberRange


app = Flask(__name__)

app.config['SECRET_KEY'] = 'MLXH243GssUWwKdTWS7FDhdwYF56wPj8'

Birthdays = 'birthdays.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///birthdays.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

#parent table
class Birthdays(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    relation = db.Column(db.String(400), nullable=False)
    dateofbirth = db.Column(db.Date, "%A, %B, %d, %Y", nullable=False)
    my_zodiac = db.relationship('Zodiac', backref=my_zodiac)
    my_planet = db.relationship()
    
    def __init__(self, name, email, relation, dateofbirth, my_zodiac):
        self.name = name
        self.email = email
        self.relation = relation
        self.dateofbirth = dateofbirth
        self.my_zodiac = my_zodiac
    
class Zodiac (db.Model):
    my_zodiac = db.Column(db.String, db.ForeignKey(my_zodiac, backref=Birthdays))
    name = db.relationship(db.String, db.Foreignkey('name', backref=Birthdays))
    dateofbirth = db.Column(db.String, db.ForeignKey('dateofbirth.Birthdays'), 'backref=Birthday_Diary')
    my_planet = db.Column(db.String)

    def __init__(self, my_zodiac, zodiac_sign, planet):
        self.zodiac = my_zodiac
        self.zodiacsign = zodiac_sign
        self.planet = planet

@app.route('/read', method= ['GET'])
class read_entries_by_zodiac(FlaskForm):
    birthdays_by_zodiac = SelectField("Please choose a zodiac to view birthdays entries: ", [InputRequired()],
    choices=[("Aries"), ("Taurus"), ("Gemini"), ("Cancer"), 
                    ("Leo"), ("Virgo"), ("Libra"), ("Scorpio"), ("Sagittarius"), 
                    ("Capricorn"), ("Aquarius"), ("Pisces")])
    read_entries = SubmitField("Search birthdays_by_zodiac")
    
        
                          

# __init_(self, select_zodiac):
  #      self.select_zodiac = select_zodiac
  ##      from my_zodiac in my Birthdays#

    


db.drop_all()
db.create_all()

@app.route('/Add_Birthday', method=['GET', 'POST'])
def Add_Birthday(FlaskForm):
    id_field = HiddenField()
    name = StringField("Name: ", [InputRequired])
    email = StringField("Email: ", [InputRequired])
    relation = StringField("Relation: ", [InputRequired])
    dateofbirth = DateField("Please enter your date of birth (YY-MM-DD):", [InputRequired])
    submit = SubmitField(f"{Birthdays.name}, has been submitted: <br> {Add_Birthday}") 


if __name__ == '__main__':
     app.run(debug=True)

# 'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virog', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces')