import pandas as pd
import numpy as np
import random

try:
    np.random.seed(42)
    random.seed(42)

    num_records = 505
    genders = ['Male', 'Female']
    regions = ['North', 'South', 'East', 'West', 'Central']
    categories = {
        'Electronics': (400, 1200),
        'Clothing': (20, 100),
        'Home & Kitchen': (50, 300),
        'Books': (8, 30),
        'Health & Beauty': (15, 80),
        'Sports & Outdoors': (25, 200)
    }

    customer_ids = ['CUST' + str(i+1).zfill(3) for i in range(100)]
    repeated_customer_ids = random.choices(customer_ids, k=405)
    all_customer_ids = customer_ids + repeated_customer_ids
    random.shuffle(all_customer_ids)

    data = {
        'Customer_ID': all_customer_ids[:500],
        'Gender': [random.choice(genders) for _ in range(500)],
        'Age': [random.randint(18, 70) for _ in range(500)],
        'Region': [random.choice(regions) for _ in range(500)],
        'Product_Category': [random.choice(list(categories.keys())) for _ in range(500)],
        'Units_Purchased': [random.randint(1, 6) for _ in range(500)],
    }

    def generate_price(category):
        low, high = categories[category]
        return round(random.uniform(low, high), 2)

    data['Price_Per_Unit'] = [generate_price(cat) for cat in data['Product_Category']]

    data['Purchase_Date'] = []
    for _ in range(500):
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        date_str = f"2024-{month:02d}-{day:02d}"
        data['Purchase_Date'].append(date_str)

    data['Total_Amount'] = [round(units * price, 2) for units, price in zip(data['Units_Purchased'], data['Price_Per_Unit'])]

    df = pd.DataFrame(data)

    null_count = random.randint(15, 25)
    null_indices = random.sample(range(len(df)), null_count)
    df.loc[null_indices, 'Price_Per_Unit'] = np.nan
    df.loc[null_indices, 'Total_Amount'] = np.nan

    duplicate_count = random.randint(5, 10)
    rows_to_duplicate = df.sample(n=duplicate_count, random_state=42)
    df = pd.concat([df, rows_to_duplicate], ignore_index=True)

    customer_id_counts = df['Customer_ID'].value_counts()
    repeated_customers = customer_id_counts[customer_id_counts > 1].index.tolist()
except BaseException as e:
    print("Error occurred:", e)
else:
    df.to_csv('customer_sales_data.csv', index=False)
    print("Data generation completed successfully.")
