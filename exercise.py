students = []  

def add_student():
    ids = input("Enter your student ID: ")
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    courses = input("Enter your course: ")

    st = {
        "id": ids,
        "name": name,
        "age": age,
        "courses": courses
    }
    students.append(st)
    print("Student added")

def view_students():
    if not students:
        print("No students found.")
    else:
        for st in students:
            print(f"id: {st['id']}")
            print(f"name: {st['name']}")
            print(f"age: {st['age']}")
            print(f"courses: {st['courses']}")
          

def search_student():
    searching = input("Enter student id: ")
    found = False
    for st in students:
        if st["id"] == searching:
            print(st)
            found = True
            break
    if not found:
        print("Student not found.")

def get_unique_courses():
    course_set = set()
    for st in students:
        course_set.add(st["courses"])
    print("Unique courses:")
    for course in course_set:
        print(course)

def remove_student():
    remove = input("Enter student id to remove: ")
    for st in students:
        if st["id"] == remove:
            students.remove(st)
            print("Student removed")
            return
    print("Student not found.")

# Main menu loop
while True:
    print("======MENU======")
    print("1. Add student")
    print("2. View students")
    print("3. Search student")
    print("4. Get unique courses")
    print("5. Remove student")
    print("6. Exit")

    option = input("Enter option: ")

    if option == "1":
        add_student()
    elif option == "2":
        view_students()
    elif option == "3":
        search_student()
    elif option == "4":
        get_unique_courses()
    elif option == "5":
        remove_student()
    elif option == "6":
        print("Exiting.....")
        break
    else:
        print("Invalid option. Please try again.")
