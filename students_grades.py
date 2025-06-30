class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

    def status(self):
        return "Passed" if self.average() >= 60 else "Failed"

# Example data (instead of reading from a file)
data = [
    ("Lana", [89, 75, 92]),
    ("Ahmed", [65, 70, 58]),
    ("Sara", [100, 98, 97]),
    ("Omar", [50, 45, 60])
]

students = [Student(name, grades) for name, grades in data]

# Print report
print("Student Report\n" + "-" * 30)
for student in students:
    avg = student.average()
    print(f"{student.name}: Average = {avg:.2f}, Status = {student.status()}")
