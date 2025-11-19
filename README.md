## WIP

The `Computer Institute Management System (CIMS)` is a Python and MySQL-based application developed to manage course enrollments in a computer training institute efficiently. 
For Python-MySQL connectivity, following data have been used:-
host ='localhost', user='root', passwd='manager', database='cims'
It is a menu driven program. After execution main menu will be dispalyed as follows:
```
1. Enrolling For A Course
2. Edit Enrollments (as admin)
3. Display Details
4. Exit
```
For each menu there is a sub-menu

•	If we select the option for Enrolling for a Course then it will ask for entering the details of the candidate like admission number, candidate name. Then the course details will be displayed along with the course fees. When the course name and the amount will be entered that will be verified by matching  the original course name and amount. For exact verification of the fee manual checking is also needed, once everything is finalised then confirmation will go to the student.

•	We can also modify the enrollments of the student, like deleting a candidate’s enrollment , modifying the name of the candidate or updating a students course by selecting Edit Enrollments which needs credentials to login (username: abc, password: 123).

•	We can display all the candidate details or a specific candidate details using admission number by selecting the third option Display Details

•	And finally we can exit the program by selecting the option Exit.

The system uses SQL commands such as CREATE, INSERT, UPDATE, DELETE, and SELECT to manage the data in the MySQL database. Every modification is saved permanently using the commit() method.
Overall, this project demonstrates how Python and MySQL can be integrated to build a simple yet effective data management system. It is a practical example of using programming logic, database connectivity, and user interaction to simulate a real-world institutional management application
