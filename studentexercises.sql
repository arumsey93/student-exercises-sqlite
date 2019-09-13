-- This will create and open a completely blank SQLite database. In this chapter, you are going to be learning the usage of the following SQL statements.

-- CREATE TABLE
-- INSERT INTO

CREATE TABLE Cohort (
    Id	   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name   TEXT NOT NULL UNIQUE
);

CREATE TABLE Student (
    Id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    FirstName VARCHAR(55) NOT NULL,
    LastName VARCHAR(55) NOT NULL,
    SlackHandle VARCHAR(55) NOT NULL,
    CohortId INT NOT NULL,
    CONSTRAINT FK_CohortId FOREIGN KEY(CohortId) REFERENCES Cohort(Id)
);

CREATE TABLE Instructor (
    Id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    FirstName VARCHAR(55) NOT NULL,
    LastName VARCHAR(55) NOT NULL,
    SlackHandle VARCHAR(55) NOT NULL,
    CohortId INT,
    Specialty VARCHAR(55),
    CONSTRAINT FK_CohortIdInstructor FOREIGN KEY(CohortId) REFERENCES Cohort(Id)
);

CREATE TABLE Exercise (
    Id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name VARCHAR(55) NOT NULL,
    Language VARCHAR(55) NOT NULL
);

CREATE TABLE StudentExercise (
    Id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    StudentId INT NOT NULL,
    ExerciseId INT NOT NULL,
    CONSTRAINT FK_StudentId FOREIGN KEY(StudentId) REFERENCES Student(Id),
    CONSTRAINT FK_ExerciseId FOREIGN KEY(ExerciseId) REFERENCES Exercise(Id)
);

-- create cohorts
INSERT INTO Cohort (Name) VALUES ('c33');
INSERT INTO Cohort (Name) VALUES ('c34');
INSERT INTO Cohort (Name) VALUES ('c35');

-- create students
INSERT INTO Student (FirstName, LastName, SlackHandle, CohortId) VALUES ('Alex','Rumsey', 'Alex', 1);
INSERT INTO Student (FirstName, LastName, SlackHandle, CohortId) VALUES ('Tyler','C', 'Tyler', 2);
INSERT INTO Student (FirstName, LastName, SlackHandle, CohortId) VALUES ('Sam','LastName', 'Sam', 2);
INSERT INTO Student (FirstName, LastName, SlackHandle, CohortId) VALUES ('Matthew','M', 'Matty Matt', 3);
INSERT INTO Student (FirstName, LastName, SlackHandle, CohortId) VALUES ('Drew','Lalapalooza', 'Lil Drew', 3);
INSERT INTO Student (FirstName, LastName, SlackHandle, CohortId) VALUES ('Danny','Barker', 'DB', 1);
INSERT INTO Student (FirstName, LastName, SlackHandle, CohortId) VALUES ('Sydney','Noh', 'Syd', 1);
INSERT INTO Student (FirstName, LastName, SlackHandle, CohortId) VALUES ('Shane','Name', 'Shane', 3);
INSERT INTO Student (FirstName, LastName, SlackHandle, CohortId) VALUES ('Scott','Silver', 'SSilver', 2);

-- create instructors
INSERT INTO Instructor (FirstName, LastName, SlackHandle, CohortId, Specialty) VALUES ('Maddie', 'Pepper', 'MissPepper', 3, 'JavaScript');
INSERT INTO Instructor (FirstName, LastName, SlackHandle, CohortId, Specialty) VALUES ('Mo', 'Silvera', 'MoMo', 1, 'C#');
INSERT INTO Instructor (FirstName, LastName, SlackHandle, CohortId, Specialty) VALUES ('Steve', 'Brownlee', 'coach', 2, 'Full Stack');
INSERT INTO Instructor (FirstName, LastName, SlackHandle, CohortId, Specialty) VALUES ('Joe', 'Shepherd', 'joe', 2, 'Python');
INSERT INTO Instructor (FirstName, LastName, SlackHandle, CohortId, Specialty) VALUES ('Leah', 'Hoefling', 'leah', 1, 'C#');
INSERT INTO Instructor (FirstName, LastName, SlackHandle, CohortId, Specialty) VALUES ('Kristen', 'Norris', 'KNorris', 3, 'JavaScript');

-- create exercises
INSERT INTO Exercise (Name, Language) VALUES ('Chicken Monkey', 'JavaScript');
INSERT INTO Exercise (Name, Language) VALUES ('Animal Kennel', 'React');
INSERT INTO Exercise (Name, Language) VALUES ('Kandy Korner', 'React');
INSERT INTO Exercise (Name, Language) VALUES ('StudentExercises', 'SQL');
INSERT INTO Exercise (Name, Language) VALUES ('Keahua Arboretum', 'Python');

-- create student's exercises
INSERT INTO  StudentExercise (StudentId, ExerciseId) VALUES (1,3);
INSERT INTO  StudentExercise (StudentId, ExerciseId) VALUES (1,2);
INSERT INTO  StudentExercise (StudentId, ExerciseId) VALUES (2,1);
INSERT INTO  StudentExercise (StudentId, ExerciseId) VALUES (2,4);
INSERT INTO  StudentExercise (StudentId, ExerciseId) VALUES (3,5);
INSERT INTO  StudentExercise (StudentId, ExerciseId) VALUES (3,1);
INSERT INTO  StudentExercise (StudentId, ExerciseId) VALUES (4,2);
INSERT INTO  StudentExercise (StudentId, ExerciseId) VALUES (4,3);
INSERT INTO  StudentExercise (StudentId, ExerciseId) VALUES (5,1);
INSERT INTO  StudentExercise (StudentId, ExerciseId) VALUES (5,4);
INSERT INTO  StudentExercise (StudentId, ExerciseId) VALUES (6,2);
INSERT INTO  StudentExercise (StudentId, ExerciseId) VALUES (6,3);
INSERT INTO  StudentExercise (StudentId, ExerciseId) VALUES (7,2);
INSERT INTO  StudentExercise (StudentId, ExerciseId) VALUES (7,5);
INSERT INTO  StudentExercise (StudentId, ExerciseId) VALUES (8,1);
INSERT INTO  StudentExercise (StudentId, ExerciseId) VALUES (8,4);
INSERT INTO  StudentExercise (StudentId, ExerciseId) VALUES (9,3);
INSERT INTO  StudentExercise (StudentId, ExerciseId) VALUES (9,5);