grades = ["A", "B+", "B", "C+", "C", "D+", "D", "E", "F"]  # Valid grades (uppercase) for error handling

def calculate_grade_sum(calculation_dict, inputted_grades):
  """Calculates the sum of grade values based on a dictionary and input grades.
  Args:
      calculation_dict: A dictionary mapping grades (strings) to their corresponding values.
      inputted_grades: A list of strings representing the entered grades.

  Returns:
      The total sum of grade values based on the input grades.

  Raises:
      ValueError: If an invalid grade is encountered.
  """

  total_sum = 0

  for grade in inputted_grades:
    grade = grade.upper()  # Ensure case-insensitive comparison
    if grade not in grades:
      raise ValueError(f"Invalid grade: {grade}. Please enter a valid grade from A to F.")

    total_sum += calculation_dict.get(grade, 0)  # gets the value of all the inputed grades

  return total_sum

calculation_dict = {
    "A": 12,
    "B+": 10.5,
    "B": 9,
    "C+": 7.5,
    "C": 6,
    "D+": 4.5,
    "D": 3,
    "E": 1.5,
    "F": 0
}

inputted_grades = []

while True:
  try:
    no_grades = int(input("How many grades do you have released? "))
    break
  except ValueError:
    print("Enter a numerical value:")

for i in range(no_grades):
  while True:
    try:
            grade = input("Enter grade: ")
            if grade.upper() not in grades:
                raise ValueError("Invalid grade. Please enter a valid grade from A to F.")
            else:
                inputted_grades.append(grade.upper())
            break

    except ValueError:
        print("Enter a valid grade")

total_grade_sum = calculate_grade_sum(calculation_dict, inputted_grades)
ideal_grade = no_grades*12
gpa = (f"{(total_grade_sum/ideal_grade)*4:.2f}")
print("GPA:", gpa)
