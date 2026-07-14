# CLI Student record manager project
# File Handling

# Grade Calculate Function
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "Fail"


# Add Student Function
def add_student():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    marks = int(input("Enter Marks: "))

    grade = calculate_grade(marks)

    with open("students.txt", "a") as file:
        file.write(f"{name},{age},{marks},{grade}\n")

    print("Student Saved Successfully!")    


# View Students Function
def view_students():
    try:
        with open("students.txt", "r") as file:
            lines = file.readlines()

        if len(lines) == 0:
            print("No student records found!")
            return

        print("\n===== Student Records =====")

        for line in lines:
            data = line.strip().split(",")

            print("----------------------")
            print("Name  :", data[0])
            print("Age   :", data[1])
            print("Marks :", data[2])
            print("Grade :", data[3])

    except FileNotFoundError:
        print("No student records found!")


# Search Student Function
def search_student():
    search_name = input("Enter student name to search: ")

    found = False

    try:
        with open("students.txt", "r") as file:
            lines = file.readlines()

        for line in lines:
            data = line.strip().split(",")

            if data[0].lower() == search_name.lower():
                print("\nStudent Found")
                print("----------------------")
                print("Name  :", data[0])
                print("Age   :", data[1])
                print("Marks :", data[2])
                print("Grade :", data[3])

                found = True
                break

        if not found:
            print("Student not found!")

    except FileNotFoundError:
        print("No student records found!")


# Update Student Function
def update_student():
    update_name = input("Enter student name to update: ")

    found = False

    try:
        with open("students.txt", "r") as file:
            lines = file.readlines()

        with open("students.txt", "w") as file:

            for line in lines:
                data = line.strip().split(",")

                if data[0].lower() == update_name.lower():

                    print("\nCurrent Details")
                    print("Name  :", data[0])
                    print("Age   :", data[1])
                    print("Marks :", data[2])
                    print("Grade :", data[3])

                    new_age = int(input("Enter New Age: "))
                    new_marks = int(input("Enter New Marks: "))

                    new_grade = calculate_grade(new_marks)

                    file.write(
                        f"{data[0]},{new_age},{new_marks},{new_grade}\n"
                    )

                    found = True

                else:
                    file.write(line)

        if found:
            print("Student updated successfully!")
        else:
            print("Student not found!")

    except FileNotFoundError:
        print("No student records found!")


# Delete Student Function
def delete_student():
    delete_name = input("Enter student name to delete: ")

    found = False

    try:
        with open("students.txt", "r") as file:
            lines = file.readlines()

        with open("students.txt", "w") as file:

            for line in lines:
                data = line.strip().split(",")

                if data[0].lower() != delete_name.lower():
                    file.write(line)
                else:
                    found = True

        if found:
            print("Student deleted successfully!")
        else:
            print("Student not found!")

    except FileNotFoundError:
        print("No student records found!")


# Menu Function
def show_menu():
    print("\n===== Student Record Manager =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")


# Main Function
def main():

    while True:
        show_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("Program Closed")
            break

        else:
            print("Invalid Choice")


# Program Start
main()