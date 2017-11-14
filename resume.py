from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/courses')
def show_all_courses():
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
