class Employee:
    company_name = "Tech Solutions"
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def __str__(self):
        return f"Employee Name: {self.name}, Salary: {self.salary}"


employees=[
    Employee("Ahmed", 70000),
    Employee("Bob", 80000),
]

for employee in employees:
    print(employee)

def search_employee(name):
    for employee in employees:
        if employee.name.lower() == name.lower():
            return employee

    return None

result = search_employee("Ahmed")

if result:
    print("Found:", result)
else:
    print("Employee not found")