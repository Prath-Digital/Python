def calculate_total_cost(**kwargs):
    total = 0
    for name, price, quantity in zip(kwargs.get('name', []), kwargs.get('price', []), kwargs.get('quantity', [])):
        total += price * quantity
    return f"Total cost: ${total:.2f}"

# Test the function
products = {
    'name': ['Apple', 'Banana'],
    'price': [0.5, 0.3],
    'quantity': [10, 5]
}
print(calculate_total_cost(**products))