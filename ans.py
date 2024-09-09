
employees = {}

def add_employee():
    emp_id = input("Enter Employee ID: ")
    if emp_id in employees:
        print(f"Employee with ID {emp_id} already exists.")
        return
    
    name = input("Enter Employee Name: ")
    department = input("Enter Employee Department: ")
    salary = float(input("Enter Employee Salary: "))
    
    employees[emp_id] = {
        "name": name,
        "department": department,
        "salary": salary
    }
    print(f"Employee {name} added successfully.")


def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    if emp_id not in employees:
        print(f"Employee with ID {emp_id} not found.")
        return
    
    print("Leave blank if you do not want to update a field.")
    name = input("Enter new name (or press Enter to skip): ")
    department = input("Enter new department (or press Enter to skip): ")
    salary_input = input("Enter new salary (or press Enter to skip): ")
    salary = float(salary_input) if salary_input else None

    if name:
        employees[emp_id]['name'] = name
    if department:
        employees[emp_id]['department'] = department
    if salary is not None:
        employees[emp_id]['salary'] = salary
    
    print(f"Employee {emp_id} updated successfully.")

def search_employee_by_id():
    emp_id = input("Enter Employee ID to search: ")
    if emp_id in employees:
        details = employees[emp_id]
        print(f"\nEmployee ID: {emp_id}")
        print(f"Name: {details['name']}")
        print(f"Department: {details['department']}")
        print(f"Salary: {details['salary']}")
    else:
        print(f"Employee with ID {emp_id} not found.")


def generate_department_wise_report():
    report = {}

 
    for emp_id, details in employees.items():
        dept = details['department']
        if dept not in report:
            report[dept] = []
        report[dept].append({
            "ID": emp_id,
            "Name": details['name'],
            "Salary": details['salary']
        })

    
    for dept, emp_list in report.items():
        print(f"\nDepartment: {dept}")
        print(f"{'ID':<5} {'Name':<10} {'Salary':<10}")
        print("-" * 30)
        for emp in emp_list:
            print(f"{emp['ID']:<5} {emp['Name']:<10} {emp['Salary']:<10}")
    print("\nReport Generated Successfully!")


def main_menu():
    while True:
        print("1. Add Employee")
        print("2. Update Employee")
        print("3. Search Employee by ID")
        print("4. Generate Department-wise Report")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_employee()
        elif choice == '2':
            update_employee()
        elif choice == '3':
            search_employee_by_id()
        elif choice == '4':
            generate_department_wise_report()
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")

main_menu()

