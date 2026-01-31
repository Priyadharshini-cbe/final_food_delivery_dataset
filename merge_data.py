import pandas as pd
import json
import re

def process_data():
    # Step 1: Load CSV Data
    print("Loading orders.csv...")
    orders_df = pd.read_csv('orders.csv')
    
    # Step 2: Load JSON Data
    print("Loading users.json...")
    with open('users.json', 'r') as f:
        users_data = json.load(f)
    users_df = pd.DataFrame(users_data)
    
    # Step 3: Load SQL Data
    print("Parsing restaurants.sql...")
    restaurants = []
    with open('restaurants.sql', 'r') as f:
        for line in f:
            if line.startswith('INSERT INTO restaurants VALUES'):
                match = re.search(r'\((.*)\);', line)
                if match:
                    values_str = match.group(1)
                    parts = values_str.split(',')
                    r_id = int(parts[0].strip())
                    r_name = parts[1].strip().strip("'")
                    cuisine = parts[2].strip().strip("'")
                    rating = float(parts[3].strip())
                    restaurants.append({
                        'restaurant_id': r_id,
                        'restaurant_name_master': r_name,
                        'cuisine': cuisine,
                        'rating': rating
                    })
    restaurants_df = pd.DataFrame(restaurants)
    
    # Step 4: Merge the Data
    print("Merging datasets...")
    merged_df = orders_df.merge(users_df, on='user_id', how='left')
    final_df = merged_df.merge(restaurants_df, on='restaurant_id', how='left')
    
    # Step 5: Create Final Dataset
    output_path = 'final_food_delivery_dataset.csv'
    print(f"Saving final dataset to {output_path}...")
    final_df.to_csv(output_path, index=False)
    
    print("Successfully created final_food_delivery_dataset.csv")

if __name__ == "__main__":
    process_data()
