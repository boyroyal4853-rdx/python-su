# Each student = (roll_no, name, marks_tuple)
# marks_tuple = (math, science, english)

students = [
    (101, "Amit", (78, 85, 90)),
    (102, "Riya", (88, 79, 92)),
    (103, "Rahul", (67, 72, 70)),
    (104, "Sneha", (90, 91, 89)),
    (105, "Karan", (56, 60, 58))
]

# Function to calculate average marks
def calculate_average(marks):
    return sum(marks) / len(marks)

# Function to assign grade
def get_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "Fail"

# Display all students
def display_students():
    print("\n--- Student Records ---")
    for student in students:
        roll, name, marks = student
        avg = calculate_average(marks)
        grade = get_grade(avg)
        
        print(f"Roll: {roll}, Name: {name}")
        print(f"Marks: {marks}")
        print(f"Average: {avg:.2f}, Grade: {grade}")
        print("-" * 30)

# Search student by roll number
def search_student(roll_no):
    for student in students:
        if student[0] == roll_no:
            roll, name, marks = student
            avg = calculate_average(marks)
            grade = get_grade(avg)
            
            print("\nStudent Found:")
            print(f"Roll: {roll}, Name: {name}")
            print(f"Marks: {marks}")
            print(f"Average: {avg:.2f}, Grade: {grade}")
            return
    print("\nStudent not found!")

# Find topper
def find_topper():
    topper = None
    highest_avg = 0
    
    for student in students:
        avg = calculate_average(student[2])
        if avg > highest_avg:
            highest_avg = avg
            topper = student
    
    if topper:
        print("\n--- Topper ---")
        print(f"Roll: {topper[0]}, Name: {topper[1]}")
        print(f"Average: {highest_avg:.2f}")

# Main menu
while True:
    print("\n===== MENU =====")
    print("1. Display All Students")
    print("2. Search Student")
    print("3. Find Topper")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        display_students()
        
    elif choice == "2":
        roll = int(input("Enter Roll Number: "))
        search_student(roll)
        
    elif choice == "3":
        find_topper()
        
    elif choice == "4":
        print("Exiting program...")
        break
        
    else:
        print("Invalid choice! Try again.")