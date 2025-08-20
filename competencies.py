# --- 1. VARIABLES, DATA TYPES, AND BASIC I/O ---
print("Welcome to the Student Grade Manager!")

# Get the number of students
try:
    num_students = int(input("Enter the number of students: "))
except ValueError:
    print("Invalid input! Defaulting to 3 students.")
    num_students = 3

# --- 2. LISTS AND DICTIONARIES TO STORE DATA ---
students = []  # list of student names
grades = {}    # dictionary mapping student names to list of grades

# --- 3. LOOPS AND USER INPUT ---
for i in range(num_students):
    name = input(f"Enter name of student {i + 1}: ")
    students.append(name)

    grades[name] = []
    for j in range(3):  # 3 grades per student
        while True:
            try:
                grade = float(input(f"Enter grade {j + 1} for {name}: "))
                if 0 <= grade <= 100:
                    grades[name].append(grade)
                    break
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid grade. Please enter a number.")

# --- 4. FUNCTIONS ---
def calculate_average(grade_list):
    return sum(grade_list) / len(grade_list)

def get_letter_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

# --- 5. DISPLAY RESULTS ---
print("\n--- Student Report ---")
for name in students:
    avg = calculate_average(grades[name])
    letter = get_letter_grade(avg)
    print(f"{name}: Grades = {grades[name]}, Average = {avg:.2f}, Letter Grade = {letter}")

# --- 6. BASIC ERROR HANDLING (try/except used above) ---

# --- 7. OPTIONAL: SIMPLE ALGORITHM (SORT STUDENTS BY AVERAGE) ---
print("\n--- Top Students ---")
sorted_students = sorted(students, key=lambda x: calculate_average(grades[x]), reverse=True)

for i, name in enumerate(sorted_students):
    avg = calculate_average(grades[name])
    print(f"{i + 1}. {name} - Average: {avg:.2f}")
