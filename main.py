from random import choice

from functions import add_employee,get_employee,update_employee_salary,delete_employee,list_employees
def menu():
    print("Employement Management System")
    print("1.Add Employee")
    print("2.Update Employee Salary")
    print("3.Delete Employee")
    print("4.List all Employees")

    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_employee()

            if choice == 2:
                salary=int(input("Enter the Salary of employee: "))
                id = int(input("Enter the ID of Employee: "))
                update_employee_salary(salary,id)

            if choice==3:
                id = int(input("Enter the ID of Employee: "))
                delete_employee(id)

            if choice==4:
                list_employees()
                for emp in list_employees():
                    print(emp)

            if choice==0:
                break
        except ValueError:
            print("Choice must be a number")

menu()