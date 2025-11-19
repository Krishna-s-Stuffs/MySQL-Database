import mysql.connector as sql

# Connect to MySQL
mycon = sql.connect(host='localhost', user='', passwd='', database='cims')
if mycon.is_connected():
    print("Successfully Connected")

cursor = mycon.cursor()

print("\n===== Computer Institute Management System =====\n")
print("1. Enrolling For A Course")
print("2. Edit Enrollments (as admin)")
print("3. Display Details")
print("4. Exit")

choice = int(input("\nEnter your choice (1-4): "))

if choice == 1:
    # Enrolling For A Course
    admno = int(input("\nEnter the Admission Number: "))
    candidatename = input("Enter your name : ")
    print("\nAvailable Courses:")
    print("1. JAVA\n2. PYTHON\n3. C\n4. BASIC\n5. HTML\n")
    course = input("Enter the Course Name: ").upper()
    SQL_Insert = "INSERT INTO candidate_details (adm_no, candidate_name, course) VALUES (%s, %s, %s)"
    values = (admno, candidatename, course)
    cursor.execute(SQL_Insert, values)
    mycon.commit()
    print(f"\nYou are Enrolled Mr. {candidatename}. Congrats!!!")
    print(f"Your enrollment for {course} course is successful!\n")

elif choice == 2:
    # Edit Enrollments (as admin)
    uname = input("Enter Username: ")
    passwd = input("Enter Password: ")
    u_name = 'abc'
    pass_wd = '123'

    if uname == u_name and passwd == pass_wd:
        print("\nPassword Accepted\n")
        print("1. Delete An Enrollment")
        print("2. Edit Name")
        print("3. Edit Course\n")
        option = int(input("Which of the above options would you like to choose ? "))

        if option == 1:
            change_adm_no = int(input("Enter the admission number of the candidate to be removed: "))
            cursor.execute("DELETE FROM candidate_details WHERE adm_no = %s", (change_adm_no,))
            mycon.commit()
            print("\nSuccessfully removed\n")

        elif option == 2:
            adm_no = int(input("Enter the admission number of the candidate whose name is to be changed: "))
            change_name = input("Enter the desired name: ")
            cursor.execute("UPDATE candidate_details SET candidate_name = %s WHERE adm_no = %s", (change_name, adm_no))
            mycon.commit()
            print("\nSuccessfully edited\n")

        elif option == 3:
            adm_no = int(input("Enter the admission number of the candidate whose course is to be changed: "))
            print("\nAvailable Courses:")
            print("1. JAVA\n2. PYTHON\n3. C\n4. BASIC\n5. HTML\n")
            change_course = input("Enter the Course Name: ").upper()
            cursor.execute("UPDATE candidate_details SET course = %s WHERE adm_no = %s", (change_course, adm_no))
            mycon.commit()
            print("\nSuccessfully modified\n")
    else:
        print("\nWrong Username or Password")

elif choice == 3:
    # Display Entries
    cursor.execute("SELECT * FROM candidate_details")
    data = cursor.fetchall()
    print("\n======= Candidates Details =====\n")
    for row in data:
        print("  Admission Number : ", row[0])
        print("  Candidate Name   : ", row[1])
        print("  Course Selected  : ", row[2], "\n")
elif choice == 4:
    print('\nThank You :) \n')
else:
    print("Invalid Choice")

mycon.close()
