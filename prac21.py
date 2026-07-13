student={
    "name":"yousaf",
    "age":21,
    "student1":{
        "name":"ali"

    }
}
# print(student["age"])
# student.update({"city":"lahore"})
# print(student)
# print(student["city"])

student2=student.copy()
# print(student2["name"])

print(student2["student1"]["name"])