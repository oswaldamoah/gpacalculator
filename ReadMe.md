# University of Ghana GPA Calculator

This program calculates the Grade Point Average (GPA) based on manually inputted grades according to the grading system of the University of Ghana.

## How it Works

The program prompts the user to enter the number of grades they have received. Then, it prompts the user to input each grade. It validates each grade entered to ensure it falls within the valid range of grades (A to F). If an invalid grade is entered, it raises a `ValueError`.

The GPA is calculated based on the sum of grade values and the total number of grades entered. The formula used for GPA calculation is derived from the University of Ghana's grading system.

## Prerequisites

- Python 3.x

## Usage

1. Run the program in a Python environment.
2. Enter the number of grades you have received when prompted.
3. Enter each grade one by one as prompted.
4. The program will calculate and display your GPA.

## Valid Grades

The valid grades accepted by the program are:

- A
- B+
- B
- C+
- C
- D+
- D
- E
- F

## GPA Calculation Formula

The GPA is calculated using the following formula:
`GPA = (Total Grade Sum / Ideal Grade) * 4`

Where:
- `Total Grade Sum`: Sum of grade values based on the input grades.
- `Ideal Grade`: Maximum possible grade value (12) multiplied by the number of grades entered.

## Error Handling

The program includes error handling to ensure that only valid grades are accepted as input. If an invalid grade is entered, a `ValueError` will be raised, and the user will be prompted to enter a valid grade.

## Moving Forward
The next version of this program will require the user to enter the various numbers of each grade, for a faster user experience



## Credits

This program was created by Oswald Amoah.
