import pandas as pd
from collections import Counter


# Path to your CSV file
file_path = 'Data/articles_PhilippHennig.csv'

# Read the CSV into a DataFrame
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame



#get oredered dict of coauthors by number of occurances
all_authors = list(df['authors'])
all_authors_flattened = flattened_list = [name.strip() for item in all_authors for name in item.split(',')]

name_counts = Counter(all_authors_flattened)

# Sort the dictionary by value in descending order
sorted_name_counts = sorted(name_counts.items(), key=lambda item: item[1], reverse=True)

# Convert sorted tuples back to dictionary
sorted_name_counts_dict = dict(sorted_name_counts)



paper_titles = list(df['title'])

print(paper_titles)