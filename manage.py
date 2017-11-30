from flask_script import Manager
from resume import app, db, Professor, Course

manager = Manager(app)


# Reset database and create three professors
@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    harry_wang = Professor(name='Harry Wang', department='Management Information Systems')
    t_lynch = Professor(name='T Lynch', department='Computer and Information Sciences')
    bryan_crissinger = Professor(name='Bryan Crissinger', department='Mathematics')
    MISY350 = Course(course_number=350, title='Business Application Development II', description='Covers concepts related to client side development, including cascading style sheets and JavaScript.', professor=harry_wang)
    CISC355 = Course(course_number=355, title='Computers, Ethics, and Society', description='Explains relationships among information technology, society, and ethics by examining issues raised by increasingly widespread use of computers. Topics include ethics for computer professionals, computer impact on factory work, office work, personal privacy, and social power distribution.', professor=t_lynch)
    MATH201 = Course(course_number=201, title='Introduction to Statistical Methods I', description='Exploratory data analysis, basic probability, discrete and continuous distributions, sampling distributions and confidence intervals, and one- and two-sample hypothesis tests on means and proportions. Emphasis on applications in business and economics. Statistical computing is an integral part of this course.', professor=bryan_crissinger)
    db.session.add(harry_wang)
    db.session.add(t_lynch)
    db.session.add(bryan_crissinger)
    db.session.add(MISY350)
    db.session.add(CISC355)
    db.session.add(MATH201)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
