"""Code using Flask to link with website """


import os
import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/students')
def student_courses():
    """ Query for Students courses """
    dbpath = '/E:/Software Engineering/Stevens Project/810_startup.db'

    try:
        db = sqlite3.connect(dbpath)
    except sqlite3.OperationalError:
        return f'Error: Unable to open database at path {dbpath}'
    else:
        query = """select instructors.CWID, instructors.Name, instructors.Dept, Grades.Course, count(*) as Students 
                    from instructors join Grades 
                    on instructors.CWID = Grades.InstructorCWID 
                    group by instructors.Name, Grades.Course;
                """
        data = [{'cwid': cwid, 'name': name, 'dept': dept, 'courses': course, 'students': students} for cwid, name, dept, course, students in db.execute(query)]

        db.close()

        return render_template(
            'Sit.html',
            title = 'Stevens Repository',
            table_title = 'Number of completed courses by Student',
            students = data)
    
app.run(debug=True)