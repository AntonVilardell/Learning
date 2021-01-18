# Connectar a una BDD de MySQL a través de Python
# link: https://www.freecodecamp.org/news/connect-python-with-sql/

#Paquet instal·lació: mysql-connector-python

import mysql.connector
from mysql.connector import Error
import pandas as pd

#Conexió al servidor de la BDD
def create_server_connection(host_name, port, database, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=database,
            port=port
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

connection = create_server_connection("db4free.net", "3306", "anton_python", "antonv", "anton123")

def execute_query(connection, name_query, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query %s successful" %name_query)
    except Error as err:
        print(f"Query %S - Error: '{err}'" %name_query)

#String creació taules BDD
create_teacher_table = """
    CREATE TABLE teacher (
        teacher_id      INT PRIMARY KEY,
        first_name      VARCHAR(40) NOT NULL,
        last_name       VARCHAR(40) NOT NULL,
        language_1      VARCHAR(3) NOT NULL,
        language_2      VARCHAR(3),
        dob             DATE,
        tax_id          INT UNIQUE,
        phone_no        VARCHAR(20)
    );
 """

create_client_table='''
    CREATE TABLE client (
        client_id   INT PRIMARY KEY,
        client_name VARCHAR(40) NOT NULL,
        address     VARCHAR(60) NOT NULL,
        industry    VARCHAR(20)
    );
'''

create_participant_table='''
    CREATE TABLE participant (
        participant_id  INT PRIMARY KEY,
        first_name      VARCHAR(40) NOT NULL,
        last_name       VARCHAR(40) NOT NULL,
        phone_no        VARCHAR(20),
        client          INT
    );
'''

create_course_table='''
    CREATE TABLE course (
        course_id       INT PRIMARY KEY,
        course_name     VARCHAR(40) NOT NULL,
        language        VARCHAR(3),
        level           VARCHAR(2),
        course_lenght_week  INT,
        stard_date      DATE,
        in_school       BOOLEAN,
        teacher         INT,
        client          INT
        
    );
'''

execute_query(connection, 'create_teacher_table', create_teacher_table) # Execute our defined query: teacher
execute_query(connection, 'create_client_table', create_client_table) # Execute our defined query: client
execute_query(connection, 'create_participant_table', create_participant_table) # Execute our defined query: participant
execute_query(connection, 'create_course_table', create_course_table) # Execute our defined query: course

#Creació de relacions entre taules
alter_participant='''
    ALTER TABLE participant
    ADD FOREIGN KEY (client)
        REFERENCES client(client_id)
        ON DELETE SET NULL;
'''

alter_course='''
    ALTER TABLE course
    ADD FOREIGN KEY (client)
        REFERENCES client(client_id)
        ON DELETE SET NULL
    ;
'''

alter_course_2='''
    ALTER TABLE course
    ADD FOREIGN KEY (teacher)
        REFERENCES teacher(teacher_id)
        ON DELETE SET NULL
    ;
'''
create_takescourse_table = '''
    CREATE TABLE takes_course (
      participant_id INT,
      course_id INT,
      PRIMARY KEY(participant_id, course_id),
      FOREIGN KEY(participant_id) REFERENCES participant(participant_id) ON DELETE CASCADE,
      FOREIGN KEY(course_id) REFERENCES course(course_id) ON DELETE CASCADE
    );
'''

execute_query(connection, 'alter_participant', alter_participant) # Execute our defined query
execute_query(connection, 'alter_course', alter_course) # Execute our defined query
execute_query(connection, 'alter_course_2', alter_course_2) # Execute our defined query
execute_query(connection, 'create_takescourse_table', create_takescourse_table) # Execute our defined query

#Insertar dades a les taules
pop_teacher = """
    INSERT INTO teacher VALUES
        (1,  'James', 'Smith', 'ENG', NULL, '1985-04-20', 12345, '+491774553676'),
        (2, 'Stefanie',  'Martin',  'FRA', NULL,  '1970-02-17', 23456, '+491234567890'), 
        (3, 'Steve', 'Wang',  'MAN', 'ENG', '1990-11-12', 34567, '+447840921333'),
        (4, 'Friederike',  'Müller-Rossi', 'DEU', 'ITA', '1987-07-07',  45678, '+492345678901'),
        (5, 'Isobel', 'Ivanova', 'RUS', 'ENG', '1963-05-30',  56789, '+491772635467'),
        (6, 'Niamh', 'Murphy', 'ENG', 'IRI', '1995-09-08',  67890, '+491231231232');
"""
pop_client = """
    INSERT INTO client VALUES
        (101, 'Big Business Federation', '123 Falschungstraße, 10999 Berlin', 'NGO'),
        (102, 'eCommerce GmbH', '27 Ersatz Allee, 10317 Berlin', 'Retail'),
        (103, 'AutoMaker AG',  '20 Künstlichstraße, 10023 Berlin', 'Auto'),
        (104, 'Banko Bank',  '12 Betrugstraße, 12345 Berlin', 'Banking'),
        (105, 'WeMoveIt GmbH', '138 Arglistweg, 10065 Berlin', 'Logistics');
"""

pop_participant = """
    INSERT INTO participant VALUES
        (101, 'Marina', 'Berg','491635558182', 101),
        (102, 'Andrea', 'Duerr', '49159555740', 101),
        (103, 'Philipp', 'Probst',  '49155555692', 102),
        (104, 'René',  'Brandt',  '4916355546',  102),
        (105, 'Susanne', 'Shuster', '49155555779', 102),
        (106, 'Christian', 'Schreiner', '49162555375', 101),
        (107, 'Harry', 'Kim', '49177555633', 101),
        (108, 'Jan', 'Nowak', '49151555824', 101),
        (109, 'Pablo', 'Garcia',  '49162555176', 101),
        (110, 'Melanie', 'Dreschler', '49151555527', 103),
        (111, 'Dieter', 'Durr',  '49178555311', 103),
        (112, 'Max', 'Mustermann', '49152555195', 104),
        (113, 'Maxine', 'Mustermann', '49177555355', 104),
        (114, 'Heiko', 'Fleischer', '49155555581', 105);
"""

pop_course = """
    INSERT INTO course VALUES
        (12, 'English for Logistics', 'ENG', 'A1', 10, '2020-02-01', TRUE,  1, 105),
        (13, 'Beginner English', 'ENG', 'A2', 40, '2019-11-12',  FALSE, 6, 101),
        (14, 'Intermediate English', 'ENG', 'B2', 40, '2019-11-12', FALSE, 6, 101),
        (15, 'Advanced English', 'ENG', 'C1', 40, '2019-11-12', FALSE, 6, 101),
        (16, 'Mandarin für Autoindustrie', 'MAN', 'B1', 15, '2020-01-15', TRUE, 3, 103),
        (17, 'Français intermédiaire', 'FRA', 'B1',  18, '2020-04-03', FALSE, 2, 101),
        (18, 'Deutsch für Anfänger', 'DEU', 'A2', 8, '2020-02-14', TRUE, 4, 102),
        (19, 'Intermediate English', 'ENG', 'B2', 10, '2020-03-29', FALSE, 1, 104),
        (20, 'Fortgeschrittenes Russisch', 'RUS', 'C1',  4, '2020-04-08',  FALSE, 5, 103);
"""

pop_takescourse = """
    INSERT INTO takes_course VALUES
        (101, 15),
        (101, 17),
        (102, 17),
        (103, 18),
        (104, 18),
        (105, 18),
        (106, 13),
        (107, 13),
        (108, 13),                      
        (109, 14),
        (109, 15),
        (110, 16),
        (110, 20),
        (111, 16),
        (114, 12),
        (112, 19),
        (113, 19);
"""

execute_query(connection, 'pop_teacher', pop_teacher)
execute_query(connection, 'pop_client', pop_client)
execute_query(connection, 'pop_participant', pop_participant)
execute_query(connection, 'pop_course', pop_course)
execute_query(connection, 'pop_takescourse', pop_takescourse)

# Lectura BDD

def read_query(connection, name_query, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Query %s - Error: '{err}'" % name_query)


query1 = '''
    SELECT 
        t1.course_id,
        t1.course_name,
        t2.first_name,
        t2.last_name
    FROM course t1
    INNER JOIN teacher t2 on (t1.teacher = t2.teacher_id)
    ;
'''

# Returns a list of lists and then creates a pandas DataFrame
from_db = []

results = read_query(connection, 'query1', query1)

for result in results:
    result = list(result)
    from_db.append(result)

columns = ["course_id", "course_name", "first_name", "last_name"]
df = pd.DataFrame(from_db, columns=columns)

print(df)

