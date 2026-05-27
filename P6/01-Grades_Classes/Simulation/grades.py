from tools import Course

simulation = Course("simulation Analysis", "20-561")

simulation.set_new_rule("q", 0.20)  # Quiz: 20%
simulation.set_new_rule("h", 0.30)  # Homework: 30%
simulation.set_new_rule("p", 0.50)  # Project: 50%
simulation.set_new_rule("f", 0.0)  # Final: 0%

# ---------------------------------------
st_name = "Ali MohammadPour"
st_number = "404302083"
simulation.add_student(st_name, st_number)

simulation.add_homework(st_name, 1, 100)
simulation.add_homework(st_name, 2, 100)
simulation.add_homework(st_name, 3, 92) # Question 1(if and only if)
simulation.add_homework(st_name, 4, 100)

simulation.add_project(st_name, 1, 90) # The code is not dynamic. How can you decide on how many people will be at the first case? 
simulation.add_project(st_name, 2, 0)

# ---------------------------------------
st_name = "Fereshte Nassaj"
st_number = "404204505"
simulation.add_student(st_name, st_number)

simulation.add_homework(st_name, 1, 100)
simulation.add_homework(st_name, 2, 100)
simulation.add_homework(st_name, 3, 100)
simulation.add_homework(st_name, 4, 100)

simulation.add_project(st_name, 1, 90) # The code is not dynamic. How can you decide on how many people will be at the first case?
simulation.add_project(st_name, 2, 0)

# ---------------------------------------
st_name = "Mahdi SattariAghdam"
st_number = "404300863"
simulation.add_student(st_name, st_number)

simulation.add_homework(st_name, 1, 100)
simulation.add_homework(st_name, 2, 100)
simulation.add_homework(st_name, 3, 92) # Question 1(if and only if)
simulation.add_homework(st_name, 4, 90) # The final Question is not completed...

simulation.add_project(st_name, 1, 100)
simulation.add_project(st_name, 2, 0)

# ---------------------------------------
st_name = "Navid Kashani"
st_number = "404204119"
simulation.add_student(st_name, st_number)

simulation.add_homework(st_name, 1, 90) # Average count in queue is calculated wrong all over the homework
simulation.add_homework(st_name, 2, 90) # 4.23 wrong final number
simulation.add_homework(st_name, 3, 92) # Question 1(if and only if)
simulation.add_homework(st_name, 4, 0)

simulation.add_project(st_name, 1, 100)
simulation.add_project(st_name, 2, 0)

# ---------------------------------------
simulation.show_summary()
file_path = r"/Users/keivanjamali/Projects/Pure-Python/P6/01-Grades_Classes/Simulation/student_grades.txt"
simulation.save_student_grades(file_path)
# simulation.show_list("q")
