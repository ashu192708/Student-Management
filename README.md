# Electricity Demand Prediction System

A simple **Electricity Demand Prediction System** built using Python. This project allows users to predict electricity demand based on temperature, humidity, hour of the day, and previous electricity demand through a command-line interface (CLI).

## Features

* Add a new electricity demand prediction
* View all prediction records
* Search predictions using a date
* Generate sample electricity data
* Display electricity demand summary
* Classify demand into LOW, NORMAL, HIGH, and CRITICAL levels
* Save prediction records using JSON
* Simple menu-driven interface
* No external Python libraries required

## Requirements

Before running the project, make sure Python is installed on your computer.

Check the Python version:

```bash
python --version

On macOS / Linux, you can also use:
python3 --version

The project works with Python 3.x.

Project Structure
Electricity-Demand-Prediction/
│
├── electricity_prediction.py
└── README.md

When the program saves prediction records, it automatically creates:
electricity_data.json

Installation
1. Clone or download the project

If you have downloaded the project, open the project folder in your terminal.

If using Git:
git clone <repository-url>

Then enter the project directory:
cd Electricity-Demand-Prediction

2. No additional packages required

This project uses only Python's built-in features, so you do not need to run pip install.

How to Run
Windows

Open Command Prompt or PowerShell and navigate to the project folder:
cd Desktop\Electricity-Demand-Prediction

Run the program:
python electricity_prediction.py

If python doesn't work, try:
py electricity_prediction.py

macOS / Linux
Open Terminal and navigate to the project folder:
cd ~/Desktop/Electricity-Demand-Prediction
Yesterday 11:50 PM
Origin_Hackathon_Problem_Statements_(3).pdf
PDF
except ps 6 which can make as a project for academic using python only  
see
Student-Management-main.zip
Zip Archive
see 
see
why i get error 
lol u suggest na what should be folder and file name, see left side github  repo  

Yep 😂 — for exactly this project:

Folder: Electricity-Demand-Prediction
Python file: electricity_prediction.py
README: README.md
Basic Python only
electricity_data.json is created automatically when the program runs

Copy this into README.md:

# Electricity Demand Prediction System

## Overview

The Electricity Demand Prediction System is a basic Python project that predicts electricity demand using simple input-based rules.

The system considers factors such as:

- Temperature
- Humidity
- Hour of the day
- Previous electricity demand

It then calculates the predicted electricity demand and classifies it as LOW, NORMAL, HIGH, or CRITICAL.

This project is implemented using basic Python concepts and does not use machine learning libraries.

---

## Problem Statement

Electricity demand changes according to different conditions such as weather, time of day, and previous demand.

The purpose of this project is to create a simple system that can estimate electricity demand based on these factors.

---

## Objectives

- Predict electricity demand using basic Python logic.
- Use temperature, humidity, time, and previous demand as inputs.
- Classify electricity demand into different levels.
- Store prediction records for future use.
- Search prediction records by date.
- Generate sample electricity data.
- Display a summary of electricity demand.

---

## Features

### 1. Add New Prediction

The user can enter:

- Date
- Temperature
- Humidity
- Hour
- Previous electricity demand

The system calculates the predicted demand.

### 2. View All Predictions

Displays all saved electricity prediction records.

### 3. Search Prediction

Allows the user to search for prediction records using a date.

### 4. Generate Sample Data

Automatically generates sample electricity prediction records for testing the system.

### 5. Show Demand Summary

Displays:

- Total number of records
- Average demand
- Highest demand
- Lowest demand
- Grid capacity warning

---

## Demand Levels

The predicted electricity demand is classified into four levels:

| Demand | Level |
|---|---|
| Below 4500 MW | LOW |
| 4500–6499 MW | NORMAL |
| 6500–7499 MW | HIGH |
| 7500 MW or above | CRITICAL |

---

## Technologies Used

- Python 3
- JSON
- File Handling
- Functions
- Conditional Statements
- Loops
- Lists
- Dictionaries
- Exception Handling
- Random Number Generation

No external Python libraries are required.

---

## Project Structure

```text
Electricity-Demand-Prediction/
│
├── electricity_prediction.py
└── README.md
Runtime Data File

When the program runs and data is saved, it automatically creates:

electricity_data.json

This file stores the prediction records.

How the System Works

The system first asks the user for electricity-related information.

The prediction calculation considers:

Temperature
Humidity
Hour of the day
Previous electricity demand

Higher temperatures and humidity can increase the estimated demand.

Morning and evening hours also increase the estimated demand, while late-night and early-morning hours can reduce it.

A small random variation is also added to make the generated predictions different.

The final value is then assigned a demand level.

How to Run
Step 1: Open Terminal

Navigate to the project folder:

cd ~/Desktop/Electricity-Demand-Prediction
Step 2: Run the Python program
python3 electricity_prediction.py
Program Menu

After running the program, the following menu is displayed:

1. Add New Prediction
2. View All Predictions
3. Search Prediction
4. Generate Sample Data
5. Show Demand Summary
6. Exit

Enter the number corresponding to the required operation.

Example

For example, the user may enter:

Temperature: 35
Humidity: 80
Hour: 19
Previous Demand: 5000

The system processes these values and displays a predicted electricity demand along with its demand level.

Data Storage

Prediction records are stored automatically in:

electricity_data.json

The program uses Python's built-in JSON and file-handling features to save and load the records.

Limitations
The project uses rule-based calculations rather than a trained machine learning model.
Predictions are for educational purposes.
The sample data is generated randomly.
Real electricity demand prediction would require larger and more reliable datasets.
Future Improvements

Possible future improvements include:

Using real electricity consumption datasets.
Adding machine learning models.
Adding graphical data visualization.
Adding more weather and energy-related parameters.
Improving prediction accuracy.
Developing a graphical or web-based interface.
Academic Purpose

This project demonstrates the practical use of basic Python programming concepts such as:

Variables
Input and output
Functions
Lists
Dictionaries
Loops
Conditional statements
File handling
JSON
Exception handling
Random number generation
Author

Ashu

Integrated M.Tech (AI)
VIT Bhopal University

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


bash
python --version


On Windows, you can also use:


bash
py --version


The project works with **Python 3.x**.

## Project Structure


text
StudentManagement/
│
├── student_management.py
└── README.md


## Installation

### 1. Clone or download the project

If you have downloaded the project, open the project folder in your terminal.

If using Git:


bash
git clone <repository-url>


Then enter the project directory:


bash
cd StudentManagement


### 2. No additional packages required

This project uses only Python's built-in features, so you do not need to run pip install.

## How to Run

### Windows

Open Command Prompt or PowerShell and navigate to the project folder:


bash
cd Desktop\StudentManagement


Run the program:


bash
python student_management.py


If python doesn't work, try:


bash
py student_management.py


### macOS / Linux

Open Terminal and navigate to the project folder:


bash
cd ~/Desktop/StudentManagement


Run:


bash
python3 student_management.py


## Main Menu

When the program starts, you will see:


text
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


Enter the number corresponding to the operation you want to perform.

## Usage

### 1. Add Student

Select:


text
1


Then enter the student's information:


text
Enter Roll Number: 101
Enter Student Name: Rahul
Enter Age: 18
Enter Course: BCA


The program will display:


text
Student added successfully!


### 2. Update Student

Select:


text
2


Enter the roll number of the student:


text
Enter Roll Number to update: 101


Then enter the updated information.

### 3. Delete Student

Select:


text
3


Enter the roll number:


text
Enter Roll Number to delete: 101


The student record will be removed.

### 4. Search Student

Select:


text
4


Enter the roll number:


text
Enter Roll Number to search: 101


The student's details will be displayed.

### 5. Display All Students

Select:


text
5


The program displays all currently stored student records.

### 6. Exit

Select:


text
6


The program will close.

## Example


text
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


Searching for the student:


text
Enter your choice: 4
Enter Roll Number to search: 101

----- Student Details -----
Roll Number : 101
Name        : Rahul
Age         : 18
Course      : BCA


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

This project is intended for educational and learning purposes.  just like this format mujhe mere code ka redeame do lol

😂 Got it. You want the same simple README style, structure, and level of detail as your Student Management README — but written specifically for your Electricity Demand Prediction code.

Copy this directly into README.md:

# Electricity Demand Prediction System

A simple **Electricity Demand Prediction System** built using Python. This project allows users to predict electricity demand based on temperature, humidity, hour of the day, and previous electricity demand through a command-line interface (CLI).

## Features

* Add a new electricity demand prediction
* View all prediction records
* Search predictions using a date
* Generate sample electricity data
* Display electricity demand summary
* Classify demand into LOW, NORMAL, HIGH, and CRITICAL levels
* Save prediction records using JSON
* Simple menu-driven interface
* No external Python libraries required

## Requirements

Before running the project, make sure Python is installed on your computer.

Check the Python version:

```bash
python --version

On macOS / Linux, you can also use:

python3 --version

The project works with Python 3.x.

Project Structure
Electricity-Demand-Prediction/
│
├── electricity_prediction.py
└── README.md

When the program saves prediction records, it automatically creates:

electricity_data.json
Installation
1. Clone or download the project

If you have downloaded the project, open the project folder in your terminal.

If using Git:

git clone <repository-url>

Then enter the project directory:

cd Electricity-Demand-Prediction
2. No additional packages required

This project uses only Python's built-in features, so you do not need to run pip install.

How to Run
Windows

Open Command Prompt or PowerShell and navigate to the project folder:

cd Desktop\Electricity-Demand-Prediction

Run the program:

python electricity_prediction.py

If python doesn't work, try:

py electricity_prediction.py
macOS / Linux

Open Terminal and navigate to the project folder:

cd ~/Desktop/Electricity-Demand-Prediction

Run:
python3 electricity_prediction.py

Main Menu

When the program starts, you will see:

==================================================
 ELECTRICITY DEMAND PREDICTION SYSTEM
==================================================
1. Add New Prediction
2. View All Predictions
3. Search Prediction
4. Generate Sample Data
5. Show Demand Summary
6. Exit

Enter the number corresponding to the operation you want to perform.

Usage
1. Add New Prediction

Select:
1
Then enter the required information:

Enter date (YYYY-MM-DD): 2026-09-21
Enter temperature (°C): 35
Enter humidity (%): 80
Enter hour (0-23): 19
Enter previous demand (MW): 5000

The system will calculate the predicted electricity demand and display its demand level.

Example:

Prediction generated successfully!
--------------------------------
Predicted Demand : 6150 MW
Demand Level     : NORMAL
--------------------------------
2. View All Predictions

Select:
2

The program displays all saved electricity prediction records, including:

Date
Temperature
Humidity
Hour
Previous demand
Predicted demand
Demand level
3. Search Prediction

Select:
3
Enter date (YYYY-MM-DD): 2026-09-21

The program displays the prediction records available for that date.

4. Generate Sample Data

Select:
4
The program automatically generates sample electricity prediction records.

This feature can be used for testing the system without entering every record manually.

5. Show Demand Summary

Select:
5
The program displays:

Total number of records
Average electricity demand
Highest electricity demand
Lowest electricity demand
Grid capacity warning

Example:
========== DEMAND SUMMARY ==========

Total Records    : 10
Average Demand   : 5235.4 MW
Highest Demand   : 6810 MW
Lowest Demand    : 3920 MW

Grid Capacity Check:
WARNING: High electricity demand detected.

========== DEMAND SUMMARY ==========

Total Records    : 10
Average Demand   : 5235.4 MW
Highest Demand   : 6810 MW
Lowest Demand    : 3920 MW

Grid Capacity Check:
WARNING: High electricity demand detected.

6. Exit

Select:
6

The program will close.

Demand Levels

The system classifies predicted electricity demand into four levels:

Below 4500 MW       → LOW
4500 - 6499 MW     → NORMAL
6500 - 7499 MW     → HIGH
7500 MW or above   → CRITICAL

How Prediction Works

The system calculates electricity demand using:

Temperature
Humidity
Hour of the day
Previous electricity demand

Temperature and humidity can increase the estimated demand.

Morning and evening hours also increase demand, while late-night and early-morning hours can reduce demand.

A small random variation is added to the calculated demand.

The final predicted demand is then classified into a demand level.

Example
==================================================
 ELECTRICITY DEMAND PREDICTION SYSTEM
==================================================
1. Add New Prediction
2. View All Predictions
3. Search Prediction
4. Generate Sample Data
5. Show Demand Summary
6. Exit

Enter your choice: 1
Enter date (YYYY-MM-DD): 2026-09-21
Enter temperature (°C): 35
Enter humidity (%): 80
Enter hour (0-23): 19
Enter previous demand (MW): 5000

Prediction generated successfully!

--------------------------------
Predicted Demand : 6150 MW
Demand Level     : NORMAL
--------------------------------

Data Storage

Prediction records are stored automatically in:

electricity_data.json

The program uses Python's built-in JSON and file handling features to save and load prediction records.

The JSON file is created automatically when prediction data is saved.

Future Improvements

The project can be extended with:

Real electricity consumption datasets
Machine learning-based prediction
Graphical data visualization
Weather data integration
More electricity demand factors
Graphical User Interface (GUI)
Web-based interface
Improved prediction accuracy


Technologies Used
Python 3
JSON
Python Lists
Python Dictionaries
Functions
File Handling
Conditional Statements
Loops
Exception Handling
Command Line Interface (CLI)

Author

ASHU

Integrated M.Tech (AI)
VIT Bhopal University

License

This project is intended for educational and learning purposes.








