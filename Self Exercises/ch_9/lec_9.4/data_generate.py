import pandas as pd
import numpy as np
import random
from datetime import datetime

try:
    np.random.seed(42)
    random.seed(42)

    num_records = 500

    order_ids = ["ORD" + str(i + 1).zfill(5) for i in range(num_records)]
    customer_ids = [
        "CUST" + str(random.randint(1, 150)).zfill(4) for _ in range(num_records)
    ]

    products = [
        "Laptop Pro",
        "Wireless Headphones",
        "Smart Watch",
        "Bluetooth Speaker",
        "Gaming Mouse",
        "Mechanical Keyboard",
        "USB-C Hub",
        "Wireless Charger",
        "External SSD",
        "Noise Cancelling Earbuds",
        "Tablet",
        "Smart Home Hub",
        "Fitness Tracker",
        "Portable Monitor",
        "Webcam HD",
    ]

    categories = [
        "Electronics",
        "Electronics",
        "Electronics",
        "Audio",
        "Computer",
        "Computer",
        "Accessories",
        "Accessories",
        "Storage",
        "Audio",
        "Electronics",
        "Smart Home",
        "Wearables",
        "Computer",
        "Accessories",
    ]

    product_category_map = dict(zip(products, categories))

    return_statuses = [
        "Not Returned",
        "Returned",
        "Not Returned",
        "Not Returned",
        "Not Returned",
    ]
    shipping_methods = [
        "Standard",
        "Express",
        "Next Day",
        "Free Shipping",
        "International",
    ]

    data = {
        "Order_ID": order_ids,
        "Customer_ID": customer_ids,
        "Product": [random.choice(products) for _ in range(num_records)],
        "Category": [],
        "Order_Quantity": [random.randint(1, 5) for _ in range(num_records)],
        "Price": [],
        "Return_Status": [random.choice(return_statuses) for _ in range(num_records)],
        "Shipping_Method": [
            random.choice(shipping_methods) for _ in range(num_records)
        ],
        "Order_date": [],
    }

    price_ranges = {
        "Laptop Pro": (800, 2000),
        "Wireless Headphones": (50, 300),
        "Smart Watch": (150, 500),
        "Bluetooth Speaker": (30, 150),
        "Gaming Mouse": (40, 120),
        "Mechanical Keyboard": (60, 200),
        "USB-C Hub": (20, 80),
        "Wireless Charger": (25, 100),
        "External SSD": (80, 400),
        "Noise Cancelling Earbuds": (100, 350),
        "Tablet": (300, 900),
        "Smart Home Hub": (80, 250),
        "Fitness Tracker": (50, 200),
        "Portable Monitor": (150, 450),
        "Webcam HD": (30, 120),
    }

    for product in data["Product"]:
        data["Category"].append(product_category_map[product])
        low, high = price_ranges[product]
        data["Price"].append(round(random.uniform(low, high), 2))

    for _ in range(num_records):
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        date_str = f"2024-{month:02d}-{day:02d}"
        data["Order_date"].append(date_str)

    data["Total_Price"] = [
        round(qty * price, 2)
        for qty, price in zip(data["Order_Quantity"], data["Price"])
    ]

    df = pd.DataFrame(data)

    null_count = random.randint(10, 20)
    null_indices = random.sample(range(len(df)), null_count)
    df.loc[null_indices, "Price"] = np.nan
    df.loc[null_indices, "Total_Price"] = np.nan

    duplicate_count = random.randint(5, 8)
    rows_to_duplicate = df.sample(n=duplicate_count, random_state=42)
    df = pd.concat([df, rows_to_duplicate], ignore_index=True)
except BaseException as e:
    print("Error occurred while generating data:", e)
else:
    df.to_csv("order_shipping_data.csv", index=False)
    print("Data generation completed successfully.")
