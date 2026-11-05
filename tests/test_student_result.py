import pytest

from student_result import (
    validate_marks,
    calculate_average,
    calculate_grade,
    process_result
)


# Test 1: Valid marks
def test_validate_marks():
    assert validate_marks(85) == True


# Test 2: Invalid marks
def test_invalid_marks():
    with pytest.raises(ValueError):
        validate_marks(120)


# Test 3: Calculate average
def test_calculate_average():
    assert calculate_average([80, 90, 100]) == 90


# Test 4: Empty marks list
def test_empty_marks():
    with pytest.raises(ValueError):
        calculate_average([])


# Test 5: Grade calculation
def test_calculate_grade():
    assert calculate_grade(95) == "A"
    assert calculate_grade(80) == "B"
    assert calculate_grade(60) == "C"
    assert calculate_grade(40) == "F"


# Test 6: Invalid grade input
def test_invalid_grade():
    with pytest.raises(ValueError):
        calculate_grade(110)


# Test 7: Process student result
def test_process_result():
    result = process_result("Nandhini", [85, 90, 78])

    assert result == {
        "name": "Nandhini",
        "average": 84.33,
        "grade": "B"
    }


# Test 8: Empty student name
def test_empty_student_name():
    with pytest.raises(ValueError):
        process_result("", [80, 90])


   # Test 9: Minimum marks
def test_minimum_marks():
    assert validate_marks(0) == True


# Test 10: Maximum marks
def test_maximum_marks():
    assert validate_marks(100) == True


# Test 11: Negative marks
def test_negative_marks():
    with pytest.raises(ValueError):
        validate_marks(-10)


# Test 12: Non-numeric marks
def test_non_numeric_marks():
    with pytest.raises(TypeError):
        validate_marks("eighty")


# Test 13: Invalid student name
def test_invalid_student_name():
    with pytest.raises(ValueError):
        process_result("   ", [80, 90])


# Test 14: Grade boundary testing
def test_grade_boundaries():
    assert calculate_grade(90) == "A"
    assert calculate_grade(75) == "B"
    assert calculate_grade(50) == "C"
    assert calculate_grade(49) == "F"


def test_grade_boundary_correction():
    assert calculate_grade(90) == "A"
    assert calculate_grade(75) == "B"
    assert calculate_grade(50) == "C"