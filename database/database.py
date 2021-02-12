import mysql.connector


# mydb = mysql.connector.connect(host="localhost", user="root", passwd="qwerty1234")
# cursor =  mydb.cursor()
# cursor.execute("CREATE DATABASE SALARIES")

salariesdb = mysql.connector.connect(host="localhost", user="root", passwd="qwerty1234", database="SALARIES")
cursor = salariesdb.cursor()

# cursor.execute("CREATE TABLE employees ( id VARCHAR(255), salaries VARCHAR(255))")

# cursor.execute("ALTER TABLE employees ADD PRIMARY KEY (id)")

# cursor.execute("SHOW TABLES")

# for i in cursor:
#     print(i)

# cursor.execute("INSERT INTO employees (id, salaries) VALUES (5, 10000)")
# salariesdb.commit()

cursor.execute("SELECT * FROM employees")

allemployees = cursor.fetchall()

print(type(allemployees[0]))

maxval = (0, 0)

for employee in allemployees:
    if(int(maxval[1]) < int(employee[1])):
        maxval = employee

print(maxval)
