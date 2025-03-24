import mysql.connector as mysql


db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)
cursor = db.cursor(dictionary=True)
# 1
cursor.execute("INSERT INTO students (name, second_name, group_id) VALUES ('Valentin', 'Hrytsuk', NULL)")
student_id = cursor.lastrowid
# 2
cursor.execute(f"INSERT INTO books (title, taken_by_student_id) VALUES ('Warcraft', {student_id})")
cursor.execute(f"INSERT INTO books (title, taken_by_student_id) VALUES ('Adventures of the morning', {student_id})")
cursor.execute(f"INSERT INTO books (title, taken_by_student_id) VALUES ('Bright tower', {student_id})")
# 3
cursor.execute(
    "INSERT INTO `groups` (title, start_date, end_date) VALUES ('Hrytsuk`s group', 'march 2025', 'april 2025')"
)
group_id = cursor.lastrowid
cursor.execute(f"UPDATE students SET group_id = {group_id} WHERE id = {student_id}")
# 4
cursor.execute("INSERT INTO subjets (title) VALUES ('AQA for dreamers')")
first_sub_id = cursor.lastrowid
cursor.execute("INSERT INTO subjets (title) VALUES ('How to break the brain')")
second_sub_id = cursor.lastrowid
cursor.execute("INSERT INTO subjets (title) VALUES ('More than `Hello world`')")
third_sub_id = cursor.lastrowid
# 5
cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('1. Be afraid', {first_sub_id})")
sub_1 = cursor.lastrowid
cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('2. Outroducing in QA', {first_sub_id})")
sub_2 = cursor.lastrowid
cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('1. Drinking of another way', {second_sub_id})")
sub_3 = cursor.lastrowid
cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('2. You are not unique', {second_sub_id})")
sub_4 = cursor.lastrowid
cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('1. Why to print `Hello Universe', {third_sub_id})")
sub_5 = cursor.lastrowid
cursor.execute(f"INSERT INTO lessons (title, subject_id) VALUES ('2. Why to hack the PENTAGON', {third_sub_id})")
sub_6 = cursor.lastrowid
# 6
cursor.execute(f"INSERT INTO marks (value, lesson_id, student_id) VALUES ('10/10', {sub_1}, {student_id})")
cursor.execute(f"INSERT INTO marks (value, lesson_id, student_id) VALUES ('10/10', {sub_2}, {student_id})")
cursor.execute(f"INSERT INTO marks (value, lesson_id, student_id) VALUES ('10/10', {sub_3}, {student_id})")
cursor.execute(f"INSERT INTO marks (value, lesson_id, student_id) VALUES ('10/10', {sub_4}, {student_id})")
cursor.execute(f"INSERT INTO marks (value, lesson_id, student_id) VALUES ('10/10', {sub_5}, {student_id})")
cursor.execute(f"INSERT INTO marks (value, lesson_id, student_id) VALUES ('10/10', {sub_6}, {student_id})")
# All_marks
select_query = f'''
SELECT s.name, s.second_name, l.title, m.value
FROM students s
JOIN marks m
ON s.id = m.student_id
JOIN lessons l
ON l.id = m.lesson_id
WHERE s.id = {student_id}
'''
cursor.execute(select_query)
print(cursor.fetchall())
# All_books
select_query = f'''
SELECT s.name, s.second_name, b.title
FROM students s
JOIN books b
ON s.id = b.taken_by_student_id
WHERE s.id = {student_id}
'''
cursor.execute(select_query)
print(cursor.fetchall())
# All
select_query = f'''
SELECT g.title AS g_title, s.name, s.second_name, b.title AS b_title, su.title AS su_title, l.title AS l_title, m.value
FROM students s
JOIN marks m
ON s.id = m.student_id
JOIN lessons l
ON l.id = m.lesson_id
JOIN `groups` g
ON g.id = s.group_id
JOIN books b
ON s.id = b.taken_by_student_id
JOIN subjets su
ON su.id = l.subject_id
WHERE s.id = {student_id}
'''
cursor.execute(select_query)
print(cursor.fetchall())
db.commit()
db.close()
