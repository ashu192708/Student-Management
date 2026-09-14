import json
import os

FILE_NAME = "students.json"


# -------------------------------
# Load students from file
# -------------------------------
def load_students():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


# -------------------------------
# Save students to file
# -------------------------------
def save_students(students):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(students, file, indent=4)
        return True
    except OSError:
        return False


# -------------------------------
# Calculate grade
# -------------------------------
def calculate_grade(marks):
    average = sum(marks) / len(marks)

    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


# -------------------------------
# Add student
# -------------------------------
def add_student(students):
    print("\n========== ADD STUDENT ==========")

    student_id = input("Enter Student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    # Check duplicate ID
    for student in students:
        if student["id"] == student_id:
            print("A student with this ID already exists.")
            return

    name = input("Enter Student Name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    course = input("Enter Course: ").strip()

    if not course:
        print("Course cannot be empty.")
        return

    # Enter marks
    marks = []

    print("\nEnter marks for 5 subjects:")

    for i in range(1, 6):
        while True:
            try:
                mark = float(input(f"Subject {i} marks (0-100): "))

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    average = sum(marks) / len(marks)
    grade = calculate_grade(marks)

    student = {
        "id": student_id,
        "name": name,
        "course": course,
        "marks": marks,
        "average": round(average, 2),
        "grade": grade
    }

    students.append(student)

    if save_students(students):
        print("\nStudent added successfully!")
        print("Average:", student["average"])
        print("Grade:", student["grade"])
    else:
        print("Error while saving student data.")


# -------------------------------
# View all students
# -------------------------------
def view_students(students):
    print("\n========== ALL STUDENTS ==========")

    if not students:
        print("No students found.")
        return

    for student in students:
        print("\n------------------------------")
        print("Student ID :", student["id"])
        print("Name       :", student["name"])
        print("Course     :", student["course"])
        print("Marks      :", student["marks"])
        print("Average    :", student["average"])
        print("Grade      :", student["grade"])
        print("------------------------------")


# -------------------------------
# Search student
# -------------------------------
def search_student(students):
    print("\n========== SEARCH STUDENT ==========")

    search_id = input("Enter Student ID: ").strip()

    for student in students:
        if student["id"] == search_id:
            print("\nStudent Found!")
            print("------------------------------")
            print("Student ID :", student["id"])
            print("Name       :", student["name"])
            print("Course     :", student["course"])
            print("Marks      :", student["marks"])
            print("Average    :", student["average"])
            print("Grade      :", student["grade"])
            print("------------------------------")
            return

    print("Student not found.")


# -------------------------------
# Update student
# -------------------------------
def update_student(students):
    print("\n========== UPDATE STUDENT ==========")

    student_id = input("Enter Student ID to update: ").strip()

    for student in students:
        if student["id"] == student_id:

            print("\nCurrent Name:", student["name"])
            new_name = input("Enter new name (press Enter to keep old): ").strip()

            if new_name:
                student["name"] = new_name

            print("Current Course:", student["course"])
            new_course = input(
                "Enter new course (press Enter to keep old): "
            ).strip()

            if new_course:
                student["course"] = new_course

            choice = input(
                "\nDo you want to update marks? (y/n): "
            ).strip().lower()

            if choice == "y":
                new_marks = []

                print("\nEnter new marks for 5 subjects:")

                for i in range(1, 6):
                    while True:
                        try:
                            mark = float(
                                input(f"Subject {i} marks (0-100): ")
                            )

                            if 0 <= mark <= 100:
                                new_marks.append(mark)
                                break
                            else:
                                print(
                                    "Marks must be between 0 and 100."
                                )

                        except ValueError:
                            print("Please enter a valid number.")

                student["marks"] = new_marks
                student["average"] = round(
                    sum(new_marks) / len(new_marks), 2
                )
                student["grade"] = calculate_grade(new_marks)

            if save_students(students):
                print("\nStudent updated successfully!")
            else:
                print("Error while saving data.")

            return

    print("Student not found.")


# -------------------------------
# Delete student
# -------------------------------
def delete_student(students):
    print("\n========== DELETE STUDENT ==========")

    student_id = input("Enter Student ID to delete: ").strip()

    for student in students:
        if student["id"] == student_id:

            print("\nStudent found:")
            print("Name:", student["name"])
            print("Course:", student["course"])

            confirmation = input(
                "Are you sure you want to delete this student? (y/n): "
            ).strip().lower()

            if confirmation == "y":
                students.remove(student)

                if save_students(students):
                    print("Student deleted successfully!")
                else:
                    print("Error while saving data.")
            else:
                print("Delete operation cancelled.")

            return

    print("Student not found.")


# -------------------------------
# Main program
# -------------------------------
def main():
    students = load_students()

    while True:

        print("\n")
        print("========================================")
        print("       STUDENT MANAGEMENT SYSTEM")
        print("========================================")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        print("========================================")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            delete_student(students)

        elif choice == "6":
            print("\nThank you for using Student Management System!")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 6.")


# -------------------------------
# Program starts here
# -------------------------------
if __name__ == "__main__":
    main()