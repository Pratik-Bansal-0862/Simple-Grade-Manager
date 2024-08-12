import mysql.connector

# Establishing the connection
mydb = mysql.connector.connect(
    host="localhost",
    user="Pratik",
    passwd="Pratik10123#"
)

# Creating a cursor object
mycursor = mydb.cursor()

# Creating the Organisation database
mycursor.execute("CREATE DATABASE IF NOT EXISTS Organisation")

# Using the Organisation database
mycursor.execute("USE Organisation")

# Creating the STUDENTS table with appropriate data types
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS STUDENTS (
        Roll_No INT PRIMARY KEY,
        Name VARCHAR(50) NOT NULL,
        Gender CHAR(1) NOT NULL,
        Sub1 DECIMAL(5,2),
        Sub2 DECIMAL(5,2),
        Sub3 DECIMAL(5,2),
        Sub4 DECIMAL(5,2),
        Sub5 DECIMAL(5,2),
        Total_Marks DECIMAL(6,2),
        Percentage DECIMAL(5,2),
        Grade CHAR(1)
    )
""")

# Closing the cursor and connection
mycursor.close()
mydb.close()

print("Database and table created successfully.")
