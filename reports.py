import sqlite3

class Student():

    def __init__(self, first, last, handle, cohort):
        self.first_name = first
        self.last_name = last
        self.slack_handle = handle
        self.cohort = cohort

    def __repr__(self):
        return f'{self.first_name} {self.last_name} is in {self.cohort}'

class Instructor():

    def __init__(self, first, last, handle, cohort, specialty):
        self.firstName = first
        self.lastName = last
        self.slackHandle = handle
        self.cohort = cohort
        self.specialty = specialty

    def __repr__(self):
        return f'{self.firstName} {self.lastName} teaches the {self.cohort} Cohort and is great at {self.specialty}.'

 

class Cohorts():

    def __init__(self, cohort):
        self.cohort = cohort

    def __repr__(self):
        return f'{self.cohort}'

class Exercises():

    def __init__(self, exercise, language):
        self.exercise = exercise
        self.language = language

    def __repr__(self): 
        return f'{self.exercise} is done in {self.language}'

class JavaScript():

    def __init__(self, javascript):
        self.javascript = javascript

    def __repr__(self):
        return f'{self.javascript} is a JS exercise.'

class Python():

    def __init__(self, python):
        self.python = python

    def __repr__(self):
        return f'{self.python} is a Python exercise.'

class React():

    def __init__(self, react):
        self.react = react

    def __repr__(self):
        return f'{self.react} is a React exercise.'


class ReactExercises():

    def __init__(self):
        self.db_path = "C:\\Users\\alexr_ku9a8gr\\Workspace\\python\\StudentExercises\\studentexercises.db"

    def all_react(self):

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda curser, row: React(
                row[1]
            )

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select e.Id,
                e.Name
            from Exercise e
            where e.language = 'React'
            order by e.Id
            """)

            all_react = db_cursor.fetchall()

            for react in all_react:
                print(react)


class PyExercises():

    def __init__(self):
        self.db_path = "C:\\Users\\alexr_ku9a8gr\\Workspace\\python\\StudentExercises\\studentexercises.db"

    def all_py(self):

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda curser, row: Python(
                row[1]
            )

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select e.Id,
                e.Name
            from Exercise e
            where e.language = 'Python'
            order by e.Id
            """)

            all_py = db_cursor.fetchall()

            for python in all_py:
                print(python)


class JSExercises():

    def __init__(self):
        self.db_path = "C:\\Users\\alexr_ku9a8gr\\Workspace\\python\\StudentExercises\\studentexercises.db"

    def all_js(self):

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda curser, row: JavaScript(
                row[1]
            )

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select e.Id,
                e.Name
            from Exercise e
            where e.language = 'JavaScript'
            order by e.Id
            """)

            all_js = db_cursor.fetchall()

            for javascript in all_js:
                print(javascript)

class AllExercises():

    def __init__(self):
        self.db_path = "C:\\Users\\alexr_ku9a8gr\\Workspace\\python\\StudentExercises\\studentexercises.db"

    def all_exercises(self):

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda curser, row: Exercises(
                row[1], row[2]
            )

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select e.Id,
                e.Name,
                e.Language
            from Exercise e
            order by e.Id
            """)

            all_exercises = db_cursor.fetchall()

            for exercise in all_exercises:
                print(exercise)

class DisplayCohorts():

    def __init__(self):
        self.db_path = "C:\\Users\\alexr_ku9a8gr\\Workspace\\python\\StudentExercises\\studentexercises.db"

    def all_cohorts(self):

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda curser, row: Cohorts(
                row[1]
            )

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select c.Id, 
                c.Name
            from Cohort c
            order by c.Id
            """)

            all_cohorts = db_cursor.fetchall()

            for cohort in all_cohorts:
                print(cohort)


class Instructors():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "C:\\Users\\alexr_ku9a8gr\\Workspace\\python\\StudentExercises\\studentexercises.db"

    def all_instructors(self):

        """Retrieve all students with the cohort name"""
            
        with sqlite3.connect(self.db_path) as conn:
            # conn.row_factory = self.create_student
            conn.row_factory = lambda cursor, row: Instructor(
                row[1], row[2], row[6], row[6], row[5]
            )
            
            
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select i.Id,
                i.FirstName,
                i.LastName,
                i.SlackHandle,
                i.CohortId,
                i.Specialty,
                c.Name
            from Instructor i
            join Cohort c on i.CohortId = c.Id
            order by i.CohortId
            """)

            all_instructors = db_cursor.fetchall()

            # for student in all_students:
            #     print(f'{student[1]} {student[2]} is in {student[5]}')

            # for student in all_students:
            #     print(f'{student[1]} {student[2]} is in {student[5]}')

            for instructor in all_instructors:
                print(instructor)

class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "C:\\Users\\alexr_ku9a8gr\\Workspace\\python\\StudentExercises\\studentexercises.db"

    def all_students(self):

        """Retrieve all students with the cohort name"""
            
        with sqlite3.connect(self.db_path) as conn:
            # conn.row_factory = self.create_student
            conn.row_factory = lambda cursor, row: Student(
                row[1], row[2], row[3], row[5]
            )
            
            
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select s.Id,
                s.FirstName,
                s.LastName,
                s.SlackHandle,
                s.CohortId,
                c.Name
            from Student s
            join Cohort c on s.CohortId = c.Id
            order by s.CohortId
            """)

            all_students = db_cursor.fetchall()

            # for student in all_students:
            #     print(f'{student[1]} {student[2]} is in {student[5]}')

            # for student in all_students:
            #     print(f'{student[1]} {student[2]} is in {student[5]}')

            for student in all_students:
                print(student)



class NewClass():
    def __init__(self):
        self.db_path = "C:\\Users\\alexr_ku9a8gr\\Workspace\\python\\StudentExercises\\studentexercises.db"

    def newfunc(self):
        
        exercises = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
                select
                    e.Id ExerciseId,
                    e.Name,
                    s.Id,
                    s.FirstName,
                    s.LastName
                from Exercise e
                join StudentExercise se on se.ExerciseId = e.Id
                join Student s on s.Id = se.StudentId
            """)

            dataset = db_cursor.fetchall()

            for row in dataset:
                exercise_id = row[0]
                exercise_name = row[1]
                student_id = row[2]
                student_name = f'{row[3]} {row[4]}'

                if exercise_name not in exercises:
                    exercises[exercise_name] = [student_name]
                else:
                    exercises[exercise_name].append(student_name)

            for exercise_name, students in exercises.items():
                print(exercise_name)
                for student in students:
                    print(f'\t* {student}')

            # print(exercises) 

athing = NewClass()
athing.newfunc()

# reports = StudentExerciseReports()
# reports.all_students()

# list_cohorts = DisplayCohorts()
# list_cohorts.all_cohorts()

# list_exercises = AllExercises()
# list_exercises.all_exercises()

# list_javascript = JSExercises()
# list_javascript.all_js()

# list_python = PyExercises()
# list_python.all_py()

# list_react = ReactExercises()
# list_react.all_react()

# list_int = Instructors()
# list_int.all_instructors()

# student = Student('Bart', 'Simpson', '@bart', 'Cohort 8')
# print(f'{student.first_name} {student.last_name} is in {student.cohort}')