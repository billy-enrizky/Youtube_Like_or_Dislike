import pandas as pd
import random

# Create a list of random names
random.seed(42)  # Set a seed for reproducibility
num_samples = 100  # Number of random names to generate

def generate_random_name():
    first_names = ["John", "Jane", "Robert", "Emily", "Michael", "Olivia", "William", "Ava", "David", "Sophia"]
    last_names = ["Smith", "Johnson", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson", "Thomas"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

names = [generate_random_name() for _ in range(num_samples)]

# Create a categorical column 'like' or 'dislike'
likes = ['like', 'dislike']
like_dislike = [random.choice(likes) for _ in range(num_samples)]

# Create a DataFrame
df = pd.DataFrame({'Name': names, 'Like/Dislike': like_dislike})

# Save the DataFrame to a CSV file
df.to_csv('random_names_likes.csv', index=False)

# Get the 'Like/Dislike' column as a list
like_dislike_list = df['Like/Dislike'].tolist()

# Print the first 10 elements of the 'Like/Dislike' list
print(like_dislike_list[:10])
