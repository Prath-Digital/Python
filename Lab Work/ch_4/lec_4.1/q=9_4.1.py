def describe_person(**kwargs):
    description = "Person details: "
    if "name" in kwargs:
        description += f"Name: {kwargs['name']}"
    if "age" in kwargs:
        description += f", Age: {kwargs['age']}"
    if "city" in kwargs:
        description += f", City: {kwargs['city']}"
    print(description)

# Test the function
describe_person(name="Alice", age=25, city="New York")
describe_person(name="Bob", city="London")