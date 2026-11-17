class ClassRoom:
    def __init__(self, name):
        self.name = name
        self.subjects = []  #list of subject objects
        self.students = []  #list of student objects
    
    def add_student(self, student):    #rahim = calss 8 
        roll_no = f"{self.name} -{len(self.students)+1}"    #8class = 1+1 = 2
        student.id = roll_no
        self.students.append(student)
    def add_subject(self, subject):
        self.subjects.append(subject)

    def take_semester_final_exam(self):
        for subject in self.subjects:
            subject.exam(self.students)
        for student in self.students:
            student.calcuate_final_grade()