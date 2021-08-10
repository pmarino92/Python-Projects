class Person: #Creating parent class called "Person"
    name = "No Name Given"
    height = ""
    weight = ""

class Student(Person): #Child Class named "Student"
                       #Adding two new attributes 
    student_id = 1234
    gpa = 4.0

class Teacher(Person): #Child Class named "Teacher"
    salary = 40.00 # Adding two new attributes 
    department = ''
                       
    
