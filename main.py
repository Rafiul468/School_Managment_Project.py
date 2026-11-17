from school import School
from person import Student,Teacher
from subject import Subject
from classroom import ClassRoom

school = School("ABC", "Dhaka")

#Adding Classroom
eight = ClassRoom("Eight")
nine = ClassRoom("Nine")
ten = ClassRoom("Ten")

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)


#Adding Student

rahim = Student("Rahim", eight)
korim = Student("Karim", nine)
fahim = Student("Fahim", ten)
rahat = Student("Rahat", eight)
rakib = Student("Rakib", ten)
rasik = Student("Rasik", ten)


school.student_admission(rahim)
school.student_admission(korim)
school.student_admission(fahim)
school.student_admission(rahat)
school.student_admission(rakib)
school.student_admission(rasik)


#Adding Teachers

abul = Teacher("Abul Khan")
kabul = Teacher("kabul Miya")
babul = Teacher("babul Hok")
abbas = Teacher("abbas Ali")
sadh = Teacher("Sadh Islam")

#Adding Subject

bangla = Subject("Bangla", abul)
english = Subject("English", kabul)
mathmatic = Subject("Mathmatic", babul)
physics = Subject("Physics", abbas)
chamistry = Subject("Chamistry", sadh)


eight.add_subject(bangla)
eight.add_subject(english)
eight.add_subject(mathmatic)
nine.add_subject(physics)
nine.add_subject(chamistry)
ten.add_subject(chamistry)
ten.add_subject(physics)
ten.add_subject(bangla)
ten.add_subject(mathmatic)


eight.take_semester_final_exam()
nine.take_semester_final_exam()
ten.take_semester_final_exam()
print(school)