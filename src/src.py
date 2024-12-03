# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
file_path = "election_results_2024.csv"  # Update with your actual file path
data = pd.read_csv(file_path)

# Display basic information about the dataset
print("Dataset Overview:")
print(data.info())
print("\nFirst 5 rows of the dataset:")
print(data.head())

# Basic data cleaning
# Check for missing values
print("\nMissing Values in Dataset:")
print(data.isnull().sum())

# Fill missing values (if any) with placeholders or drop rows
data = data.dropna()

# Analyze election results by party
party_counts = data['Leading Party'].value_counts()
print("\nNumber of Seats Won by Each Party:")
print(party_counts)

# Analyze margins of victory
average_margin = data['Margin'].astype(int).mean()
print(f"\nAverage Margin of Victory: {average_margin:.2f}")

# Predicting results (simple rule-based model)
# Assume the leading party from this dataset continues to lead
data['Predicted Winner'] = data['Leading Party']

# Calculate prediction accuracy (comparing with actual results if available)
correct_predictions = np.sum(data['Leading Party'] == data['Predicted Winner'])
total_constituencies = len(data)
accuracy = (correct_predictions / total_constituencies) * 100
print(f"\nPrediction Accuracy: {accuracy:.2f}%")

# Visualization: Bar chart of seats won by each party
plt.figure(figsize=(10, 6))
plt.bar(party_counts.index, party_counts.values, color='skyblue')
plt.xlabel('Political Party')
plt.ylabel('Number of Constituencies Won')
plt.title('Seats Won by Each Party')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('seats_won_by_party.png')
plt.show()

# Visualization: Margins of victory distribution
plt.figure(figsize=(10, 6))
plt.hist(data['Margin'].astype(int), bins=20, color='lightgreen', edgecolor='black')
plt.xlabel('Margin of Victory')
plt.ylabel('Frequency')
plt.title('Distribution of Victory Margins')
plt.tight_layout()
plt.savefig('victory_margins_distribution.png')
plt.show()
