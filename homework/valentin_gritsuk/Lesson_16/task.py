import os
import csv
import mysql.connector as mysql
import dotenv


dotenv.load_dotenv()

# base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
# data_path = os.path.join(base_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')
# with open(data_path, newline='') as csv_file:
with open('data_for_check.csv', newline='') as csv_file:
    file_data = csv.reader(csv_file)
    data = []
    for row in file_data:
        data.append(row)
keys_data = data[0]
files_data = []
for row in data[1:]:
    files_data.append(dict(zip(keys_data, row)))

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)
cursor = db.cursor(dictionary=True)
select_query = '''
SELECT s.name, s.second_name, g.title AS group_title, b.title AS book_title,
        su.title AS subject_title, l.title AS lesson_title, m.value AS mark_value
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
'''
cursor.execute(select_query)
db_data = cursor.fetchall()
db.close()

common_dicts = [dicti for dicti in files_data if dicti in db_data]
print(common_dicts)
