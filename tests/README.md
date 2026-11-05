# Writing Automated Tests for Python Applications

## 1. Project Overview

This project focuses on developing and testing a Student Result Management System using Python and Pytest.

The application validates student marks, calculates average marks, assigns grades and processes student results.

Automated testing is used to verify the correctness, reliability and expected behaviour of the application.

## 2. Objectives

- Understand automated software testing.
- Develop a Python application.
- Implement unit testing using Pytest.
- Identify and correct logical errors.
- Perform positive, negative and boundary-value testing.
- Improve application reliability through automated testing.

## 3. Technologies Used

- Python
- Visual Studio Code
- Pytest
- Git and GitHub

## 4. Project Structure

```text
Python_Automated_Testing_Project/
│
├── student_result.py
├── tests/
│   ├── __init__.py
│   └── test_student_result.py
├── screenshots/
├── requirements.txt
└── README.md
```

## 5. Application Features

1. Mark validation.
2. Average calculation.
3. Grade assignment.
4. Student result processing.
5. Invalid input handling.

## 6. Testing Methodology

The project uses the following testing methods:

- Positive Testing: Checks valid inputs.
- Negative Testing: Checks invalid inputs.
- Boundary Value Testing: Checks minimum and maximum marks.
- Unit Testing: Tests individual functions independently.

## 7. Bug Identification and Correction

An incorrect comparison operator in the original grade calculation caused boundary values to receive incorrect grades.

The greater-than operator (>) was replaced with the greater-than-or-equal-to operator (>=).

This ensured accurate grade assignment at boundary values.

## 8. Execution Instructions

Install Pytest:

```bash
python -m pip install pytest
```

Run the application:

```bash
python student_result.py
```

Run automated tests:

```bash
python -m pytest -v
```

## 9. Testing Results

A total of 15 automated test cases were implemented.

The tests cover valid inputs, invalid inputs, grade calculations and boundary conditions.

## 10. Conclusion

This project provided practical experience in Python application development and automated software testing.

Using Pytest helped identify logical errors, verify application functionality and improve code reliability.

The project also demonstrated the importance of systematic testing in software development.