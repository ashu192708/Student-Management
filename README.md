# Student Management System

A simple **Student Management System** built using Python. This project allows users to add, update, delete, search, and display student records through a command-line interface (CLI).

## Features

* Add a new student
* Update existing student details
* Delete a student record
* Search for a student using their roll number
* Display all student records
* Simple menu-driven interface
* No external Python libraries required

## Requirements

Before running the project, make sure Python is installed on your computer.

Check the Python version:

```bash
python --version
```

On Windows, you can also use:

```bash
py --version
```

The project works with **Python 3.x**.

## Project Structure

```text
StudentManagement/
│
├── student_management.py
└── README.md
```

## Installation

### 1. Clone or download the project

If you have downloaded the project, open the project folder in your terminal.

If using Git:

```bash
git clone <repository-url>
```

Then enter the project directory:

```bash
cd StudentManagement
```

### 2. No additional packages required

This project uses only Python's built-in features, so you do not need to run `pip install`.

## How to Run

### Windows

Open Command Prompt or PowerShell and navigate to the project folder:

```bash
cd Desktop\StudentManagement
```

Run the program:

```bash
python student_management.py
```

If `python` doesn't work, try:

```bash
py student_management.py
```

### macOS / Linux

Open Terminal and navigate to the project folder:

```bash
cd ~/Desktop/StudentManagement
```

Run:

```bash
python3 student_management.py
```

## Main Menu

When the program starts, you will see:

```text
==============================
   STUDENT MANAGEMENT SYSTEM
==============================
1. Add Student
2. Update Student
3. Delete Student
4. Search Student
5. Display All Students
6. Exit
==============================
Enter your choice:
```

Enter the number corresponding to the operation you want to perform.

## Usage

### 1. Add Student

Select:

```text
1
```

Then enter the student's information:

```text
Enter Roll Number: 101
Enter Student Name: Rahul
Enter Age: 18
Enter Course: BCA
```

The program will display:

```text
Student added successfully!
```

### 2. Update Student

Select:

```text
2
```

Enter the roll number of the student:

```text
Enter Roll Number to update: 101
```

Then enter the updated information.

### 3. Delete Student

Select:

```text
3
```

Enter the roll number:

```text
Enter Roll Number to delete: 101
```

The student record will be removed.

### 4. Search Student

Select:

```text
4
```

Enter the roll number:

```text
Enter Roll Number to search: 101
```

The student's details will be displayed.

### 5. Display All Students

Select:

```text
5
```

The program displays all currently stored student records.

### 6. Exit

Select:

```text
6
```

The program will close.

## Example

```text
==============================
   STUDENT MANAGEMENT SYSTEM
==============================
1. Add Student
2. Update Student
3. Delete Student
4. Search Student
5. Display All Students
6. Exit
==============================

Enter your choice: 1

Enter Roll Number: 101
Enter Student Name: Rahul
Enter Age: 18
Enter Course: BCA

Student added successfully!
```

Searching for the student:

```text
Enter your choice: 4
Enter Roll Number to search: 101

----- Student Details -----
Roll Number : 101
Name        : Rahul
Age         : 18
Course      : BCA
```

## Data Storage

Currently, student records are stored in a Python dictionary while the program is running.

**Important:** Data is not permanently stored. When the program is closed, all student records are lost.

## Future Improvements

The project can be extended with:

* SQLite or MySQL database
* Graphical User Interface (GUI)
* Student attendance management
* Marks and grade management
* Login/authentication system
* Export records to CSV or Excel
* Input validation
* Permanent data storage

## Technologies Used

* **Python 3**
* **Python Dictionary**
* **Command Line Interface (CLI)**

## Author

**Student Management System**

Created as a Python programming project.

## License

This project is intended for educational and learning purposes.
