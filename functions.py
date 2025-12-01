from connect import connection
def add_employee():
    with connection() as con:
        cur = con.cursor()
        name = input("enter the name: ")
        salary = int(input("enter the salary: "))
        country = input("enter the country: ")
        cur.execute("insert into employees (name,salary,country) values (:name, :salary, :country)",{'name':name,'salary':salary,'country':country})
        con.commit()


def get_employee():
    with connection() as con:
        cur = con.cursor()
        id = int(input("enter the employee ID: "))
        cur.execute( "select name,salary,country from employees where eid=:id",{'id':id})
        ro = cur.fetchone()
        print(ro)

def update_employee_salary(salary,id):
    with connection() as con:
        cur = con.cursor()
        cur.execute("Update employees set salary=:salary where eid=:id",{'salary':salary,'id':id})
        con.commit()
        print('Row updated')

def delete_employee(eid):
    with connection() as con:
        cur=con.cursor()
        cur.execute("delete from employees where eid=:id",{'id':eid})
        con.commit()
        print('Row Deleted')

def list_employees():
    with connection() as con:
        cur = con.cursor()
        cur.execute("select * from employees")
        rows = cur.fetchall()
        return rows

