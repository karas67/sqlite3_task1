# Написать SQL запрос который возвращает id и name всех курсов которые посещают
# более 25 студентов.

import sqlite3

with sqlite3.connect('db_new.sqlite3') as db:
    cursor = db.cursor()
    # Таблица студентов
    cursor.execute("""CREATE TABLE IF NOT EXISTS Student (
	student_id INT PRIMARY KEY,
	full_name VARCHAR
        )""")
    # Таблица курсов
    cursor.execute("""CREATE TABLE IF NOT EXISTS Course (
	course_id INT PRIMARY KEY,
	name VARCHAR
        )""")
    # Таблица зачисление на курс
    cursor.execute("""CREATE TABLE IF NOT EXISTS CourseEnrollment (
	course_id INT NOT NULL REFERENCES Course(course_id),
	student_id INT NOT NULL REFERENCES Student(student_id)
        )""")
    db.commit()

with sqlite3.connect('db_new.sqlite3') as db:
    cursor = db.cursor()

    query = """SELECT CourseEnrollment.course_id, Course.name, COUNT(*) as count FROM Course
    JOIN CourseEnrollment ON Course.course_id = CourseEnrollment.course_id 
    GROUP BY CourseEnrollment.course_id HAVING count >= 25  """

    cursor.execute(query)

    for res in cursor:
        print("id:", res[0], "name:", res[1])

