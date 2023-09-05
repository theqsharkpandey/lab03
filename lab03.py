class Employee:
    def _init_(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def display_info(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary (PM): {self.salary}")
        print()

def search_by_age(employees, condition, age):
    filtered_employees = []
    if condition == ">":
        filtered_employees = [emp for emp in employees if emp.age > age]
    elif condition == "<":
        filtered_employees = [emp for emp in employees if emp.age < age]
    elif condition == ">=":
        filtered_employees = [emp for emp in employees if emp.age >= age]
    elif condition == "<=":
        filtered_employees = [emp for emp in employees if emp.age <= age]
    return filtered_employees

def search_by_salary(employees, condition, salary):
    filtered_employees = []
    if condition == ">":
        filtered_employees = [emp for emp in employees if emp.salary > salary]
    elif condition == "<":
        filtered_employees = [emp for emp in employees if emp.salary < salary]
    elif condition == ">=":
        filtered_employees = [emp for emp in employees if emp.salary >= salary]
    elif condition == "<=":
        filtered_employees = [emp for emp in employees if emp.salary <= salary]
    return filtered_employees

def search_by_employee_id(employees, emp_id):
    return [emp for emp in employees if emp.emp_id == emp_id]

def main():
    employees = [
        Employee("161E90", "Raman", 41, 56000),
        Employee("161F91", "Himadri", 38, 67500),
        Employee("161F99", "Jaya", 51, 82100),
        Employee("171E20", "Tejas", 30, 55000),
        Employee("171G30", "Ajay", 45, 44000),
    ]

    while True:
        print("Options:")
        print("1: Search by Age")
        print("2: Search by Salary")
        print("3: Search by Employee ID")
        print("4: Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            condition = input("Enter condition (> < >= <=): ")
            age = int(input("Enter age: "))
            result = search_by_age(employees, condition, age)
        elif choice == "2":
            condition = input("Enter condition (> < >= <=): ")
            salary = float(input("Enter salary: "))
            result = search_by_salary(employees, condition, salary)
        elif choice == "3":
            emp_id = input("Enter Employee ID: ")
            result = search_by_employee_id(employees, emp_id)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
            continue

        if result:
            for emp in result:
                emp.display_info()
        else:
            print("No matching records found.")

if __name__ == "_main_":
    main()