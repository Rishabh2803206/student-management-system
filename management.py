students = ["rishu"]

def show_menu():
    print('-' * 40)
    print("     STUDENT MANAGEMENT SYSTEM     ")
    print('-' * 40)
    print("1. Show students")
    print("2. Add student")
    print("3. Find student")
    print("4. Remove student")
    print("5. Exit")
def show():
    if students:
        print("Students list:", students)
    else:
        print("No students available.")

def add():
    name = input("Enter student name to add: ").lower().strip()
    
    if name == "":
        print("Name cannot be empty.")
        return
    
    if name not in students:
        students.append(name)
        print(f"{name} added successfully.")
    else:
        print("Student already exists.")

def find():
    name = input("Enter student name to find: ").lower().strip()
    
    if name == "":
        print("Name cannot be empty.")
        return
    
    if name in students:
        print(f"{name} is in the list.")
    else:
        print(f"{name} is NOT in the list.")

def rem():
    name = input("Enter student name to remove: ").lower().strip()
    
    if name == "":
        print("Name cannot be empty.")
        return
    
    if name in students:
        students.remove(name)
        print(f"{name} removed successfully.")
    else:
        print("Student not found.")

# looping time

while True:
    show_menu()
    choice = input("Enter choice (1-5): ").strip()

    if choice == '1':
        show()
    elif choice == '2':
        add()
    elif choice == '3':
        find()
    elif choice == '4':
        rem()
    elif choice == '5':
        print("Exiting program...")
        break
    else:
        print("Invalid choice, try again.")