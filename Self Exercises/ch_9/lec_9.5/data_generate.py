import pandas as pd
import numpy as np
import random
from datetime import datetime

np.random.seed(45)
random.seed(45)

n_rows = 560

reading_ids = [f"READ{str(i).zfill(4)}" for i in range(1, n_rows + 1)]
household_ids = [f"HH{str(random.randint(1, 300)).zfill(4)}" for _ in range(n_rows)]
regions = ["North", "South", "East", "West", "Central", "Coastal", "Urban", "Rural"]

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
reading_dates = []
for _ in range(n_rows):
    month = random.choice(months)
    day = random.randint(1, 28)
    reading_dates.append(datetime(2024, month, day))

electricity_kwh = np.round(np.random.uniform(50, 800, n_rows), 2)
gas_consumption_m3 = np.round(np.random.uniform(10, 300, n_rows), 2)
water_liters = np.round(np.random.uniform(200, 2000, n_rows), 2)
temperature_c = np.round(np.random.uniform(-5, 35, n_rows), 1)
total_energy_units = np.round(electricity_kwh * 0.8 + gas_consumption_m3 * 10.5 + water_liters * 0.001, 2)

df = pd.DataFrame({
    "Reading_ID": reading_ids,
    "Household_ID": household_ids,
    "Region": [random.choice(regions) for _ in range(n_rows)],
    "Reading_Date": reading_dates,
    "Electricity_kWh": electricity_kwh,
    "Gas_Consumption_m3": gas_consumption_m3,
    "Water_Liters": water_liters,
    "Temperature_C": temperature_c,
    "Total_Energy_Units": total_energy_units
})

duplicate_indices = random.sample(range(n_rows), 18)
duplicates = df.iloc[duplicate_indices].copy()
df = pd.concat([df, duplicates], ignore_index=True)

numeric_columns = ["Electricity_kWh", "Gas_Consumption_m3", "Water_Liters", "Temperature_C", "Total_Energy_Units"]
empty_indices = random.sample(range(len(df)), 25)
for idx in empty_indices:
    col = random.choice(numeric_columns)
    df.at[idx, col] = np.nan

df = df.sample(frac=1, random_state=45).reset_index(drop=True)
df.to_csv("household_energy_usage.csv", index=False)