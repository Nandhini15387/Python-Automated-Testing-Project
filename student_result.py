# Student Result Management System

def validate_marks(marks):
    if not isinstance(marks, (int, float)):
        raise TypeError("Marks must be numeric")

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100")

    return True


def calculate_average(marks):
    if not marks:
        raise ValueError("Marks list cannot be empty")

    for mark in marks:
        validate_marks(mark)

    return sum(marks) / len(marks)


def calculate_grade(average):
    validate_marks(average)

    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "F"


def process_result(name, marks):
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Student name cannot be empty")

    average = calculate_average(marks)
    grade = calculate_grade(average)

    return {
        "name": name,
        "average": round(average, 2),
        "grade": grade
    }


# Main program
if __name__ == "__main__":
    student_marks = [85, 90, 78]

    result = process_result("Nandhini", student_marks)

    print("Student Result")
    print("Name:", result["name"])
    print("Average:", result["average"])
    print("Grade:", result["grade"])