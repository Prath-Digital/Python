def employee_details(**kwargs):
    required = {'name', 'department'}
    if not all(field in kwargs for field in required):
        missing = required - set(kwargs.keys())
        print(f"Missing required fields: {missing}")
    else:
        print(f"Employee: {kwargs['name']}, Department: {kwargs['department']}")
        if 'salary' in kwargs:
            print(f"Salary: ${kwargs['salary']}")

# Test the function
employee_details(name="Alice", department="HR", salary=50000)
employee_details(name="Bob", salary=60000)  # Missing department