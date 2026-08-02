import pandas as pd

# Load the hospital dataset
hospital_data = pd.read_csv("/home/rguktongole/Downloads/hospital_raw_data.csv")

# Display first 5 rows
print(hospital_data.head())

# Display dataset information
print(hospital_data.info())

# Display shape
print("Dataset Shape:", hospital_data.shape)

# Save a backup copy
hospital_data.to_csv("data/hospital_raw_backup.csv", index=False)

print("Hospital dataset collected successfully.")
