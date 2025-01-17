import pandas as pd

# Load the dataset (replace 'your_file.csv' with your actual file name)
file_path = 'my_file.csv'
data = pd.read_csv(file_path)

# Function to safely extract first and last names
def extract_name_safe(email):
    username = email.split('@')[0]  # Extract the part before @
    parts = username.split('.')  # Split by '.'
    first_name = parts[0].capitalize() if len(parts) > 0 else ''
    last_name = parts[1].capitalize() if len(parts) > 1 else ''
    return first_name, last_name

# Apply the function to extract names
data[['firstname', 'lastname']] = data['emails'].apply(lambda x: pd.Series(extract_name_safe(x)))

# Save the updated dataset to a new CSV file
updated_file_path = 'updated_emails_with_names.csv'
data.to_csv(updated_file_path, index=False)

print(f"Updated file saved as {updated_file_path}")
