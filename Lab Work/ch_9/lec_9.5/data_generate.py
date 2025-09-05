import pandas as pd
import numpy as np
import random
from datetime import datetime

file_name = "customer_satisfaction_data.csv"

try:
    np.random.seed(42)
    random.seed(42)

    n_rows = 550

    survey_ids = [f"SURV{str(i).zfill(4)}" for i in range(1, n_rows + 1)]
    customer_ids = [f"CUST{str(random.randint(1, 350)).zfill(4)}" for _ in range(n_rows)]
    store_locations = ["New York", "Los Angeles", "Chicago", "Houston", "Miami", "San Francisco", "Seattle", "Boston", "Atlanta", "Dallas"]
    months = [3, 4, 5, 6, 7, 8]
    visit_dates = []
    for _ in range(n_rows):
        month = random.choice(months)
        day = random.randint(1, 28)
        visit_dates.append(datetime(2024, month, day))

    purchase_amounts = np.round(np.random.uniform(10, 500, n_rows), 2)
    wait_times = np.random.randint(1, 46, n_rows)
    staff_ratings = np.random.randint(1, 11, n_rows)
    product_ratings = np.random.randint(1, 11, n_rows)
    cleanliness_ratings = np.random.randint(1, 11, n_rows)
    recommend = np.random.choice(["Yes", "No"], n_rows, p=[0.7, 0.3])
    total_ratings = np.round((staff_ratings + product_ratings + cleanliness_ratings) / 3, 1)

    df = pd.DataFrame({
        "Survey_ID": survey_ids,
        "Customer_ID": customer_ids,
        "Store_Location": [random.choice(store_locations) for _ in range(n_rows)],
        "Visit_Date": visit_dates,
        "Purchase_Amount": purchase_amounts,
        "Wait_Time_Min": wait_times,
        "Staff_Rating": staff_ratings,
        "Product_Rating": product_ratings,
        "Cleanliness_Rating": cleanliness_ratings,
        "Recommend": recommend,
        "Total_Rating": total_ratings
    })

    duplicate_indices = random.sample(range(n_rows), 15)
    duplicates = df.iloc[duplicate_indices].copy()
    df = pd.concat([df, duplicates], ignore_index=True)

    numeric_columns = ["Purchase_Amount", "Wait_Time_Min", "Staff_Rating", "Product_Rating", "Cleanliness_Rating", "Total_Rating"]
    empty_indices = random.sample(range(len(df)), 25)
    for idx in empty_indices:
        col = random.choice(numeric_columns)
        df.at[idx, col] = np.nan

    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    
except BaseException as e:
    print(f"An error occurred: {e}")
else:
    df.to_csv(file_name, index=False)
    print(f"Dataset '{file_name}' generated successfully.")