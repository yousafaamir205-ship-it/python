import json
import os
FILE_NAME="student.py"

def load_student():
    if not os.path.exist(FILE_NAME):
        with open(FILE_NAME,"w")as file:
            json.dump([],file,indent=4)
        return
    try:
        with open(FILE_NAME,"r")as file:
            return json.load(file)
    except json.JSONDecodeError:
        return[]
def save_students(students):
    with open(FILE_NAME ,"w")as file:
        json.dump(students,file,indent=4)
