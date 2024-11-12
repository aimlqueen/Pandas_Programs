import pandas as pd
import numpy as np

# Set the future option to avoid downcasting warnings
pd.set_option('future.no_silent_downcasting', True)

# Sample data
data = [
    [1, "Rajiv", "Reddy", "n.a", "9848022337", "Hyderabad"],
    [2, "siddarth", "Battacharya", 22, "9848022338", "Kolkata"],
    [3, "Rajesh", "Khanna", "n.a", "9848022339", "n.a"],
    [4, "Preethi", "Agarwal", 21, "9848022330", "Pune"],
    [5, "Trupthi", "Mohanthy", 23, "9848022336", "Bhuwaneshwar"],
    [6, "Archana", "Mishra", 23, "9848022335", "chennai"],
    [7, "Komal", "Nayak", 24, "9848022334", "trivendram"],
    [8, "Bharathi", "Nambiayar", 124, "9848822333", "chennai"]
]

# Create a DataFrame
columns = ['ID', 'First Name', 'Last Name', 'Age', 'Phone', 'City']
df = pd.DataFrame(data, columns=columns)

# Replace "n.a" with NaN
df = df.replace("n.a", np.nan)

# Assign specific values for the NaN entries in 'Age'
age_replacements = {0: 25, 2: 30}  # Assign 25 to the first 'n.a' and 30 to the second

# Update 'Age' column using the dictionary
for index, value in age_replacements.items():
    df.at[index, 'Age'] = value

# Convert 'Age' to float for consistency if necessary
df['Age'] = df['Age'].astype(float)


# Fill NaN values in 'City' with "Unknown" (or you can leave it as is)
df['City'] = df['City'].fillna("Unknown")  # Optional: Replace NaNs in 'City'

# Display the modified DataFrame
print(df)
