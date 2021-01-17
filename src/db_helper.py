import mysql.connector as sql
class DbHelper:
    def __init__(self,cursor):
        self.cursor=cursor
    def get_maximum_salary(self):
        query= "SELECT salary FROM salary ORDER BY salary DESC  LIMIT 1"
        self.cursor.execute(query)
        result=self.cursor.fetchone()
        print("result ",result)
        return result

    def get_minimum_salary(self):
       query= "SELECT salary FROM salary ORDER BY salary LIMIT 1"
       self.cursor.execute(query)
       result=self.cursor.fetchone()
       return result

if __name__ == "__main__":
    connection=sql.connect(
    host="localhost",
    user="root",
    password="1234",
    database="employee")
    print(connection)
    # cursor.execute("CREATE DATABASE employee")
    # cursor.execute("CREATE TABLE salary( name VARCHAR(255), salary INTEGER(10))")
    # sql="INSERT INTO salary(name,salary) VALUES (%s,%s)"
    # values=[ ("Khushbu",1000),("Khushbu",900),("Aman",200),("Naman",800),("Manan",300),("Raman",700),("Khushi",600)]
    # cursor.executemany(sql, values)
    # print("row inserted",cursor.lastrowid)
    # connection.commit()
    cursor = connection.cursor()
    db_helper = DbHelper(cursor)
    min_salary = db_helper.get_minimum_salary()
    max_salary = db_helper.get_maximum_salary()
    print(max_salary)
    print(min_salary)
