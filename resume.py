import os
from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SECRET_KEY'] = 'myresumesecretkey'

# SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)


# Database tables
class Professor(db.Model):
    __tablename__ = 'professors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    department = db.Column(db.Text)
    courses = db.relationship('Course', backref='professor')


class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    course_number = db.Column(db.Integer)
    title = db.Column(db.String(256))
    description = db.Column(db.Text)
    professor_id = db.Column(db.Integer, db.ForeignKey('professors.id'))


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/professors')
def show_all_professors():
    professors = Professor.query.all()
    return render_template('professor-all.html', professors=professors)


@app.route('/professor/add', methods=['GET', 'POST'])
def add_professorss():
    if request.method == 'GET':
        return render_template('professor-add.html')
    if request.method == 'POST':
        # Get data from form
        name = request.form['name']
        department = request.form['department']
        # Insert data into database
        professor = Professor(name=name, department=department)
        db.session.add(professor)
        db.session.commit()
        return redirect(url_for('show_all_professors'))


@app.route('/professor/edit/<int:id>', methods=['GET', 'POST'])
def edit_professors(id):
    professor = Professor.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('professor-edit.html', professor=professor)
    if request.method == 'POST':
        # Get data from form
        professor.name = request.form['name']
        professor.department = request.form['department']
        db.session.commit()
        return redirect(url_for('show_all_professors'))


@app.route('/courses')
def show_all_courses():
    courses = Course.query.all()
    return render_template('course-all.html', courses=courses)


@app.route('/course/add', methods=['GET', 'POST'])
def add_courses():
    if request.method == 'GET':
        return render_template('course-add.html')
    if request.method == 'POST':
        # Get data from form
        course_number = request.form['course_number']
        title = request.form['title']
        description = request.form['description']
        professor_name = request.form['professor_name']
        # Insert data into database
        professor = Professor.query.filter_by(name=professor_name).first()
        course = Course(course_number=course_number, title=title, description=description, professor=professor)
        db.session.add(course)
        db.session.commit()
        return redirect(url_for('show_all_courses'))


@app.route('/course/edit/<int:id>', methods=['GET', 'POST'])
def edit_courses(id):
    course = Course.query.filter_by(id=id).first()
    professors = Professor.query.all()
    if request.method == 'GET':
        return render_template('course-edit.html', course=course, professors=professors)
    if request.method == 'POST':
        # Get data from form
        course.course_number = request.form['course_number']
        course.title = request.form['title']
        course.description = request.form['description']
        professor_name = request.form['professor_name']
        professor = Professor.query.filter_by(name=professor_name).first()
        course.professor = professor
        db.session.commit()
        return redirect(url_for('show_all_courses'))


@app.route('/my-courses')
def get_all_courses():
    courses = [
        'MISY350 Business Application Development II',
        'CISC355 Computers, Ethics, and Society',
        'MATH201 Introduction to Statistical Methods I'
    ]
    return render_template('courses.html', courses=courses)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
