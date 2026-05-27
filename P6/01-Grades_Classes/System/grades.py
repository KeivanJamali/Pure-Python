from tools import Course

system = Course("System Analysis", "20-575")

system.set_new_rule("q", 0.20)  # Quiz: 20%
system.set_new_rule("h", 0.30)  # Homework: 30%
system.set_new_rule("p", 0.50)  # Project: 50%
system.set_new_rule("f", 0.0)  # Final: 0%

# ---------------------------------------
st_name = "Ali Akbarloo"
st_number = "404202334"
system.add_student(st_name, st_number)

system.add_queez(st_name, 1, 100)
system.add_queez(st_name, 2, 100)

system.add_homework(st_name, 1, 100)
system.add_homework(st_name, 2, 100)
system.add_homework(st_name, 3, 90) # Not solving the KTT correct way(Q3)
system.add_homework(st_name, 4, 100)

system.add_project(st_name, 1, 100)
system.add_project(st_name, 2, 90) # Wrong second part 900%
system.add_project(st_name, 3, 90) # First of the important numbers where wrong
system.add_project(st_name, 3, 75 + 20) 

# ---------------------------------------
st_name = "Hamed Mostafavi"
st_number = "403206113"
system.add_student(st_name, st_number)

system.add_queez(st_name, 1, 100)
system.add_queez(st_name, 2, 100)

system.add_homework(st_name, 1, 100)
system.add_homework(st_name, 2, 100)
system.add_homework(st_name, 3, 100)
system.add_homework(st_name, 4, 100)

system.add_project(st_name, 1, 100)
system.add_project(st_name, 2, 100)
system.add_project(st_name, 3, 100)
system.add_project(st_name, 4, 75 + 20)

# ---------------------------------------
st_name = "Fereshte Nassaj"
st_number = "404204505"
system.add_student(st_name, st_number)

system.add_queez(st_name, 1, 100)
system.add_queez(st_name, 2, 100)

system.add_homework(st_name, 1, 100)
system.add_homework(st_name, 2, 100)
system.add_homework(st_name, 3, 100)
system.add_homework(st_name, 4, 100)

system.add_project(st_name, 1, 100)
system.add_project(st_name, 2, 100)
system.add_project(st_name, 3, 100)
system.add_project(st_name, 4, 75 + 23)

# ---------------------------------------
st_name = "Sarina Ahmadi"
st_number = "404206455"
system.add_student(st_name, st_number)

system.add_queez(st_name, 1, 100)
system.add_queez(st_name, 2, 100)

system.add_homework(st_name, 1, 100)
system.add_homework(st_name, 2, 100)
system.add_homework(st_name, 3, 100)
system.add_homework(st_name, 4, 100)

system.add_project(st_name, 1, 100)
system.add_project(st_name, 2, 100)
system.add_project(st_name, 3, 100)
system.add_project(st_name, 3, 75 + 24)

# ---------------------------------------
st_name = "Shokohikia"
st_number = "404300874"
system.add_student(st_name, st_number)

system.add_queez(st_name, 1, 100)
system.add_queez(st_name, 2, 100)

system.add_homework(st_name, 1, 100)
system.add_homework(st_name, 2, 100)
system.add_homework(st_name, 3, 100)
system.add_homework(st_name, 4, 100)

system.add_project(st_name, 1, 90) # Wrong hash algorithm
system.add_project(st_name, 2, 100)
system.add_project(st_name, 3, 100)
system.add_project(st_name, 3, 65 + 25) # Wrong numbers in report.(You said demand is 16866 but it actually is 10144)

# ---------------------------------------
st_name = "Morvarid Tavakol"
st_number = "404202237"
system.add_student(st_name, st_number)

system.add_queez(st_name, 1, 100)
system.add_queez(st_name, 2, 100)

system.add_homework(st_name, 1, 100)
system.add_homework(st_name, 2, 100)
system.add_homework(st_name, 3, 90) # No solving the KTT correct way(Q3)
system.add_homework(st_name, 4, 100)

system.add_project(st_name, 1, 100)
system.add_project(st_name, 2, 100)
system.add_project(st_name, 3, 100)
system.add_project(st_name, 3, 75 + 23)

# ---------------------------------------
st_name = "Rasol Mirshafii"
st_number = "404208059"
system.add_student(st_name, st_number)

system.add_queez(st_name, 1, 100)
system.add_queez(st_name, 2, 100)

system.add_homework(st_name, 1, 100)
system.add_homework(st_name, 2, 100)
system.add_homework(st_name, 3, 90) # Not solving the KTT correct way(Q3)
system.add_homework(st_name, 4, 100)

system.add_project(st_name, 1, 100)
system.add_project(st_name, 2, 90) # Wrong second part (67% error)
system.add_project(st_name, 3, 100)
system.add_project(st_name, 3, 75 + 22)

# ---------------------------------------
st_name = "Navid Kashani"
st_number = "404204119"
system.add_student(st_name, st_number)

system.add_queez(st_name, 1, 100)
system.add_queez(st_name, 2, 100)

system.add_homework(st_name, 1, 100)
system.add_homework(st_name, 2, 100)
system.add_homework(st_name, 3, 90) # Not solving the KTT correct way(Q3)
system.add_homework(st_name, 4, 100)

system.add_project(st_name, 1, 100)
system.add_project(st_name, 2, 100)
system.add_project(st_name, 3, 100)
system.add_project(st_name, 3, 75 + 19)

# ---------------------------------------
# system.show_summary()
file_path = r"/Users/keivanjamali/Projects/Pure-Python/P6/01-Grades_Classes/System/student_grades.txt"
system.save_student_grades(file_path)
# system.show_list("q")
