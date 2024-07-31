import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    matric_number = db.Column(db.String(50), nullable=False, unique=True)

    def studentJSON(self):
        return {
            'id': self.id,
            'name': self.name,
            'matric_number': self.matric_number
        }

if __name__ == "__main__":
    app.run(debug=True)
