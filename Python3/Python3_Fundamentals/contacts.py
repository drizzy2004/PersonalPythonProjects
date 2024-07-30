contacts = {
    "number": 4,
    "students": 
    [
        {"name": "Sarah H", "email": "sarah@example.com"},
        {"name": "Harry P", "email": "harry@example.com"},
        {"name": "Hermione G", "email": "hermione@example.com"},
        {"name": "Ron W", "email": "ron@example.com"}
    ]
}

print("Student emails:")
for student in contacts["students"]:
    print(student["email"])