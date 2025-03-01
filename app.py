from flask import Flask, request, jsonify
import json
import os
from sqlalchemy import create_engine, Column, Integer, String
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

database_url = os.environ.get('DATABASE_URL', 'postgresql://tallerPostgres:Laura2002@db:5432/students_db')
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'students'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    edad = db.Column(db.String(3), nullable=False)
    carrera = db.Column(db.String(100), nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'edad': self.edad,
            'carrera': self.carrera
        }

with app.app_context():
    db.create_all()
    
    if Student.query.count() == 0 and os.path.exists('students.json'):
        try:
            with open('students.json', 'r') as file:
                students_data = json.load(file)
                for student_data in students_data:
                    existing = Student.query.filter_by(id=student_data['id']).first()
                    if not existing:
                        student = Student(
                            id = student_data['id'],
                            nombre = student_data['nombre'],
                            edad = student_data['edad'],
                            carrera = student_data['carrera']
                        )
                        db.session.add(student)
                db.session.commit()
        except Exception as e:
            print(f"Error al cargar datos iniciales: {str(e)}")

@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([student.to_dict() for student in students])

@app.route('/students', methods=['POST'])
def add_student():
    if not request.is_json:
        return jsonify({"error": "No se encontro el JSON inicial"}), 400
    
    data = request.get_json()
    
    required_fields = ['id', 'nombre', 'edad', 'carrera']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Campo necesario '{field}' ingrese"}), 400
    
    existing = Student.query.filter_by(id=data['id']).first()
    if existing:
        return jsonify({"error": f"Ya existe un estudiante con este ID {data['id']}"}), 400
    
    new_student = Student(
        id = data['id'],
        nombre = data['nombre'],
        edad = data['edad'],
        carrera = data['carrera']
    )
    
    db.session.add(new_student)
    db.session.commit()
    
    return jsonify(new_student.to_dict()), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)