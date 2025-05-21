# initialising dictionary
students_grades = { }

# add a new student
def add_student(name, grade):
    students_grades[name] = grade
    # [satyam] = 100
    print(f"added {name} with a {grade}")
    # added satyam with a grade 100

# update a student
def update_student(name, grade):
    if name in students_grades:
        students_grades[name] = grade
        # satyam = 200
        print(f"{name} with a marks are updated {grade}")

    else:
        print("Name is not found..!")

# deleting a student
def delete_student(name):
    if name in students_grades:
        del students_grades[name]
        print(f"{name} has been successfully deleted")
    else:
        print("Name is not found..!")

# view all students
def display_all_students():
    if students_grades:
        for name, grade in students_grades.items():
            print(f"{name} : {grade}")
    else:
        print("No students found/added..!")

def main():
    while True:
        print("\nSTUDENTS GRADES MANAGEMENT SYSTEM")
        print("1. Add student")
        print("2. Update student")
        print("3. Delete student")
        print("4. Display all students")
        print("5. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter student name: ")
            grade = int(input("Enter student grade: "))
            add_student(name, grade)

        elif choice == 2:
            name = input("Enter a student name you want to update: ")
            grade = int(input("Enter student's updated grade: "))
            update_student(name, grade)

        elif choice == 3:
            name = input("Enter a student name you want to delete: ")
            delete_student(name)

        elif choice == 4:
            display_all_students()

        elif choice == 5:
            print("Thank you for using this program")
            break

        else:
            print("Invalid choice..!")

if __name__ == "__main__":
    main()

