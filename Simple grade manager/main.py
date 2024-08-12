import mysql.connector
from mysql.connector import Error

# Function to create a connection to the MySQL database
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="pass",
            database="Organisation"
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

# Function to execute a query (INSERT, UPDATE, DELETE)
def execute_query(connection, query, values=None):
    cursor = connection.cursor()
    try:
        cursor.execute(query, values)
        connection.commit()
    except Error as e:
        print(f"The error '{e}' occurred")

# Function to fetch data (SELECT)
def fetch_query(connection, query, values=None):
    cursor = connection.cursor()
    try:
        cursor.execute(query, values)
        return cursor.fetchall()
    except Error as e:
        print(f"The error '{e}' occurred")
        return None

# Function to calculate total marks, percentage, and grade
def calculate_results(sub1, sub2, sub3, sub4, sub5):
    total_marks = sub1 + sub2 + sub3 + sub4 + sub5
    percentage = (total_marks / 500) * 100
    
    # Grading criteria
    if percentage >= 90:
        grade = 'A'
    elif percentage >= 80:
        grade = 'B'
    elif percentage >= 70:
        grade = 'C'
    elif percentage >= 50:
        grade = 'D'
    else:
        grade = 'F'
    
    return total_marks, percentage, grade

# Function to add a new student
def add_student(connection, roll_no, name, gender, sub1, sub2, sub3, sub4, sub5):
    total_marks, percentage, grade = calculate_results(sub1, sub2, sub3, sub4, sub5)
    
    query = """
    INSERT INTO STUDENTS (Roll_No, Name, Gender, Sub1, Sub2, Sub3, Sub4, Sub5, Total_Marks, Percentage, Grade)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (roll_no, name, gender, sub1, sub2, sub3, sub4, sub5, total_marks, percentage, grade)
    execute_query(connection, query, values)
    print(f"Student {name} added successfully with Roll No: {roll_no}.")

# Function to modify a student's data
def modify_student(connection, roll_no, sub1, sub2, sub3, sub4, sub5):
    total_marks, percentage, grade = calculate_results(sub1, sub2, sub3, sub4, sub5)
    
    query = """
    UPDATE STUDENTS 
    SET Sub1 = %s, Sub2 = %s, Sub3 = %s, Sub4 = %s, Sub5 = %s, Total_Marks = %s, Percentage = %s, Grade = %s
    WHERE Roll_No = %s
    """
    values = (sub1, sub2, sub3, sub4, sub5, total_marks, percentage, grade, roll_no)
    execute_query(connection, query, values)
    print(f"Student with Roll No: {roll_no} has been updated successfully.")

# Function to delete a student record
def delete_student(connection, roll_no):
    query = "DELETE FROM STUDENTS WHERE Roll_No = %s"
    values = (roll_no,)
    execute_query(connection, query, values)
    print(f"Student with Roll No: {roll_no} has been deleted successfully.")

# Function to show all students
def show_students(connection):
    query = "SELECT * FROM STUDENTS"
    results = fetch_query(connection, query)
    
    if results:
        print("\nAll Student Records:")
        for record in results:
            print(record)
    else:
        print("No records found.")

# Function to search for a student by roll number
def search_student(connection, roll_no):
    query = "SELECT * FROM STUDENTS WHERE Roll_No = %s"
    values = (roll_no,)
    result = fetch_query(connection, query, values)
    
    if result:
        print(f"\nDetails for Roll No: {roll_no}")
        print(result[0])
    else:
        print(f"No record found for Roll No: {roll_no}.")

# Main script
def main():
    print("\n" + "="*40)
    print(" "*8 + "SIMPLE GRADE MANAGER")
    print("="*40 + "\n")

    connection = create_connection()
    
    while True:
        print("\nOptions:")
        print("1. Add a new student")
        print("2. Modify student data")
        print("3. Delete a student")
        print("4. Show all students")
        print("5. Search for a student by Roll No")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            roll_no = int(input("Enter Roll No: "))
            name = input("Enter Name: ")
            gender = input("Enter Gender (M/F): ").upper()
            sub1 = float(input("Enter marks for Subject 1: "))
            sub2 = float(input("Enter marks for Subject 2: "))
            sub3 = float(input("Enter marks for Subject 3: "))
            sub4 = float(input("Enter marks for Subject 4: "))
            sub5 = float(input("Enter marks for Subject 5: "))
            
            add_student(connection, roll_no, name, gender, sub1, sub2, sub3, sub4, sub5)
        
        elif choice == '2':
            roll_no = int(input("Enter Roll No: "))
            sub1 = float(input("Enter new marks for Subject 1: "))
            sub2 = float(input("Enter new marks for Subject 2: "))
            sub3 = float(input("Enter new marks for Subject 3: "))
            sub4 = float(input("Enter new marks for Subject 4: "))
            sub5 = float(input("Enter new marks for Subject 5: "))
            
            modify_student(connection, roll_no, sub1, sub2, sub3, sub4, sub5)
        
        elif choice == '3':
            roll_no = int(input("Enter Roll No to delete: "))
            delete_student(connection, roll_no)
        
        elif choice == '4':
            show_students(connection)
        
        elif choice == '5':
            roll_no = int(input("Enter Roll No to search: "))
            search_student(connection, roll_no)
        
        elif choice == '6':
            print("\n" + "="*60)
            print(" "*8 + " THANKS FOR USING SIMPLE GRADE MANAGER")
            print("="*60 + "\n")
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
