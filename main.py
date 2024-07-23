import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from migration import db, Student

load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize db with the app
db.init_app(app)

@app.route('/api/v1/students/', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([student.studentJSON() for student in students]), 200

@app.route('/api/v1/students/', methods=['POST'])
def add_student():
    data = request.get_json()
    new_student = Student(
        name=data['name'],
        matric_number=data['matriculation_number']
    )
    db.session.add(new_student)
    db.session.commit()
    return jsonify({'message': 'Student added successfully'}), 201

@app.route('/api/v1/students/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get_or_404(id)
    return jsonify(student.studentJSON()), 200

@app.route('/api/v1/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = Student.query.get_or_404(id)
    data = request.get_json()
    student.name = data['name']
    student.matric_number = data['matriculation_number']
    db.session.commit()
    return jsonify({'message': 'Student record updated successfully'})

@app.route('/api/v1/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({'message': 'Student deleted successfully'}), 200

@app.route('/healthcheck', methods=['Get'])
def healthcheck():
    return jsonify({"status": "ok", "message": "Deployment Succssful!!!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
