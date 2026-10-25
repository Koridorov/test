class Student():

    cnt=0

    def __init__(self, name:str, grade:float):
        self.name = name
        Student.cnt+=1
        self.grade = grade

    @staticmethod
    def isvalid_name(name):
        return len(name)<=30

    @staticmethod
    def isvalid_grade(grade):
        return 2<=grade<=6

    def print_student(self):
        print(self.name, self.grade)


def generate_list_of_students(n):
    student_list=[]
    for _ in range (n):
        Name=input("Enter your name: ")
        while not Student.isvalid_name(Name):
            Name=input("Enter a valid name: ")

        avg_grade=float(input("Enter your average grade: "))
        while not Student.isvalid_grade(avg_grade):
            avg_grade=float(input("Enter a valid grade: "))
        student_list.append(Student(Name, avg_grade))
    student_list.sort(key=lambda x: x.grade, reverse=True)
    student_list[0].print_student()
    student_list[-1].print_student()

n=int(input("Enter how many student entries you would like to make: "))

generate_list_of_students(n)


