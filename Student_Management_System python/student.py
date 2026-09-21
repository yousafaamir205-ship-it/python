class Student:
    def __init__(self, name, age, roll_no, course, marks):
        self.name = name
        self.age = age
        self.roll_no = roll_no
        self.course = course
        self.marks = marks

    def calculate_percentage(self):
        return self.marks

    def calculate_grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 50:
            return "D"
        else:
            return "F"

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "roll_no": self.roll_no,
            "course": self.course,
            "marks": self.marks
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["age"],
            data["roll_no"],
            data["course"],
            data["marks"]
        )

    def __str__(self):
        return (
            f"Roll No : {self.roll_no}\n"
            f"Name    : {self.name}\n"
            f"Age     : {self.age}\n"
            f"Course  : {self.course}\n"
            f"Marks   : {self.marks}\n"
            f"Grade   : {self.calculate_grade()}"
        )