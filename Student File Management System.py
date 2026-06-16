def add_student():
    stu_id=input("Enter Student ID: ")
    stu_name=input("Enter Student name: ")
    stu_course=input("Enter Student Course: ")
    with open("students_details.txt","a") as f:
        f.write(f"{stu_id},{stu_name},{stu_course}\n")
    print("Student data added successfully...")
# add_student()
def view_students():
    try:
        with open("students_details.txt","r") as f:
            print("\nStudent Details: " )
            print(f.read())
    except FileNotFoundError:
        print("students_details file not found")
#view_students()
def search_student():
    stu_id=input("Enter student id to search:")
    try:
        with open("students_details.txt","r") as f:
            found=False
            for line in f:
                data=line.strip().split(",")
                if data[0]==stu_id:
                    print("\nstudent id =",data[0])
                    print("student name=",data[1])
                    print("student course=",data[2])
                    return
            print("Student not found")
    except FileNotFoundError:
        print("File not found")
#search_student()
def count_students():
    try:
        with open("students_details.txt","r") as f:
            lines=f.readlines()
        print("\nTotal students=",len(lines))
    except FileNotFoundError:
        print("file not found")
#count_students()
#def delete_student():

while True:
    print("\n\n....Student file management system.......")
    print("1.Add student")
    print("2.View student")
    print("3.Search student")
    print("4.Count of students")
    print("5.Exit")
    choice = input("Enter your choice : ")
    if choice=="1":
        print("\n Add student")
        add_student() 
    elif choice=="2":
        print("View students")
        view_students()
    elif choice=="3":
        print("Search student")
        search_student()
    elif choice=="4":
        print("count of students..")
        count_students()
    elif choice=="5":
        print("Program Ended ")
        break
    else:print("Invalid choice Try again!!!")



