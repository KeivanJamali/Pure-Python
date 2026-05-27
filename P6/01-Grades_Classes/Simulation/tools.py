import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

class Student:
    def __init__(self, name: str, student_id: str):
        self.name = name
        self.student_id = student_id
        self.q_grades = {}
        self.h_grades = {}
        self.p_grades = {}
        self.f_grades = {}  # Final exam grades
        
    def add_queez(self, q_number: int, grade: float):
        self.q_grades[q_number] = grade
        
    def add_homework(self, h_number: int, grade: float):
        self.h_grades[h_number] = grade
        
    def add_project(self, p_number: int, grade: float):
        self.p_grades[p_number] = grade
    
    def add_final(self, grade: float):
        self.f_grades[1] = grade
    
    def get_mean(self, grade_type: str) -> float:
        """Calculate mean of grades for a specific type (q, h, p, f)"""
        if grade_type == "q":
            grades = list(self.q_grades.values())
        elif grade_type == "h":
            grades = list(self.h_grades.values())
        elif grade_type == "p":
            grades = list(self.p_grades.values())
        elif grade_type == "f":
            grades = list(self.f_grades.values())
        else:
            return 0
        
        return np.mean(grades) if grades else 0
        
class Course:
    def __init__(self, name: str, course_id: str):
        self.name = name
        self.id = course_id
        self.students = {}
        self.q_weight = 0
        self.h_weight = 0
        self.p_weight = 0
        self.f_weight = 0
        
    def add_student(self, name: str, student_id: str):
        s = Student(name, student_id)
        self.students[name] = s
        
    def add_queez(self, student_name: str, n: int, g: float):
        self.students[student_name].add_queez(n, g)
    
    def add_homework(self, student_name: str, n: int, g: float):
        self.students[student_name].add_homework(n, g)
        
    def add_project(self, student_name: str, n: int, g: float):
        self.students[student_name].add_project(n, g)
    
    def add_final(self, student_name: str, g: float):
        self.students[student_name].add_final(g)
        
    def set_new_rule(self, item, rate):
        """Set weight for each grade type
        item: 'q' (quiz), 'h' (homework), 'p' (project), 'f' (final)
        rate: weight (0-1)
        """
        assert item in "qhpf", "Item must be 'q', 'h', 'p', or 'f'"
        assert 0 <= rate <= 1, "Rate must be between 0 and 1"
        if item == "q":
            self.q_weight = rate
        elif item == "h":
            self.h_weight = rate
        elif item == "p":
            self.p_weight = rate
        elif item == "f":
            self.f_weight = rate
    
    def validate_weights(self) -> bool:
        """Check if total weights equal 1"""
        total = self.q_weight + self.h_weight + self.p_weight + self.f_weight
        return abs(total - 1.0) < 0.001
    
    def get_student_cumulative(self, student_name: str) -> float:
        """Calculate cumulative grade for a student based on weights"""
        if student_name not in self.students:
            return 0
        
        student = self.students[student_name]
        cumulative = (
            student.get_mean("q") * self.q_weight +
            student.get_mean("h") * self.h_weight +
            student.get_mean("p") * self.p_weight +
            student.get_mean("f") * self.f_weight
        )
        return round(cumulative, 2)
            
    def show_list(self, type_: str = "a"):
        """Display grades
        'q': quizzes, 'h': homework, 'p': projects, 'f': final, 'a': all
        """
        assert type_ in "qhpfa", "Type must be 'q', 'h', 'p', 'f', or 'a'"
        
        data = {}
        
        if type_ == "q":
            for name, student in self.students.items():
                data[name] = student.q_grades
        elif type_ == "h":
            for name, student in self.students.items():
                data[name] = student.h_grades
        elif type_ == "p":
            for name, student in self.students.items():
                data[name] = student.p_grades
        elif type_ == "f":
            for name, student in self.students.items():
                data[name] = student.f_grades
        elif type_ == "a":
            for name, student in self.students.items():
                data[name] = {
                    "Quiz Mean": student.get_mean("q"),
                    "Homework Mean": student.get_mean("h"),
                    "Project Mean": student.get_mean("p"),
                    "Final Grade": student.get_mean("f"),
                    "Cumulative": self.get_student_cumulative(name)
                }
        
        list_ = pd.DataFrame.from_dict(data, orient='index')

        print(f"\n{type_.upper()} Grade Report for {self.name}:")
        print(list_.fillna("-"))
    
    def show_summary(self):
        """Show comprehensive summary for all students"""
        print(f"\n{'='*80}")
        print(f"Course: {self.name} ({self.id})")
        print(f"{'='*80}\n")
        print(f"Grade Weights:")
        print(f"  Quiz: {self.q_weight*100:.1f}%")
        print(f"  Homework: {self.h_weight*100:.1f}%")
        print(f"  Project: {self.p_weight*100:.1f}%")
        print(f"  Final: {self.f_weight*100:.1f}%")
        print(f"  Total: {(self.q_weight + self.h_weight + self.p_weight + self.f_weight)*100:.1f}%")
        
        if not self.validate_weights():
            print(f"\n⚠️  WARNING: Weights do not sum to 100%!")
        
        print(f"\n{'-'*80}")
        print(f"{'Student':<20} {'Quiz':<10} {'Homework':<10} {'Project':<10} {'Final':<10} {'Cumulative':<12}")
        print(f"{'-'*80}\n")
        
        for name, student in self.students.items():
            q_mean = student.get_mean("q")
            h_mean = student.get_mean("h")
            p_mean = student.get_mean("p")
            f_mean = student.get_mean("f")
            cumulative = self.get_student_cumulative(name)
            
            print(f"{name:<20} {q_mean:<10.2f} {h_mean:<10.2f} {p_mean:<10.2f} {f_mean:<10.2f} {cumulative:<12.2f}")
        
        print(f"{'-'*80}\n")
        
    def save_student_grades(self, file_path: str, student_name: str = None):
        """Save a comprehensive grade report to a text file for a specific student or all students."""
        if student_name is not None and student_name not in self.students:
            print(f"Error: Student '{student_name}' not found.")
            return

        targets = [student_name] if student_name else list(self.students.keys())
        p = Path(file_path)

        for s_name in targets:
            student = self.students[s_name]
            
            # Determine output file path
            if student_name is None:
                out_path = p.with_name(f"{p.stem}_{s_name}{p.suffix}")
            else:
                out_path = p
                
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(f"{'='*90}\n")
                f.write(f"Course: {self.name} ({self.id})\n")
                f.write(f"Student: {student.name} (ID: {student.student_id})\n")
                f.write(f"{'='*90}\n\n")
                
                f.write("Grade Weights:\n")
                f.write(f"  Quiz:     {self.q_weight*100:.1f}%\n")
                f.write(f"  Homework: {self.h_weight*100:.1f}%\n")
                f.write(f"  Project:  {self.p_weight*100:.1f}%\n")
                f.write(f"  Final:    {self.f_weight*100:.1f}%\n")
                total = (self.q_weight + self.h_weight + self.p_weight + self.f_weight) * 100
                f.write(f"  Total:    {total:.1f}%\n\n")
                
                f.write(f"{'-'*90}\n")
                f.write(f"{'Quiz Mean':<15} | {'Homework Mean':<15} | {'Project Mean':<15} | {'Final':<10} | {'Cumulative':<15}\n")
                f.write(f"{'-'*90}\n")
                
                q_mean = student.get_mean("q")
                h_mean = student.get_mean("h")
                p_mean = student.get_mean("p")
                f_mean = student.get_mean("f")
                cumulative = self.get_student_cumulative(s_name)
                
                f.write(f"{q_mean:<15.2f} | {h_mean:<15.2f} | {p_mean:<15.2f} | {f_mean:<10.2f} | {cumulative:<15.2f}\n")
                
                f.write(f"{'-'*90}\n\n")
                
                f.write("Detailed Grades Breakdown:\n")
                f.write(f"{'='*90}\n")
                f.write(f"  * Quizzes:   {student.q_grades if student.q_grades else 'None'}\n")
                f.write(f"  * Homeworks: {student.h_grades if student.h_grades else 'None'}\n")
                f.write(f"  * Projects:  {student.p_grades if student.p_grades else 'None'}\n")
                f.write(f"  * Final:     {student.f_grades if student.f_grades else 'None'}\n")
