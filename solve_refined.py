import pandas as pd
import sqlite3

def solve_refined():
    path = 'final_food_delivery_dataset.csv'
    df = pd.read_csv(path)
    df['order_date_dt'] = pd.to_datetime(df['order_date'], format='%d-%m-%Y', errors='coerce')
    conn = sqlite3.connect(':memory:')
    df.to_sql('data', conn, index=False)

    def run(q):
        return pd.read_sql(q, conn)

    print("Q1 Highest revenue from Gold members (City):")
    print(run("SELECT city, SUM(total_amount) FROM data WHERE membership = 'Gold' GROUP BY city ORDER BY SUM(total_amount) DESC"))

    print("\nQ2 Highest avg order value (Cuisine):")
    print(run("SELECT cuisine, AVG(total_amount) FROM data GROUP BY cuisine ORDER BY AVG(total_amount) DESC"))

    print("\nQ4 Revenue by rating range:")
    q4 = """
    SELECT 
        CASE 
            WHEN rating >= 3.0 AND rating <= 3.5 THEN '3.0 - 3.5'
            WHEN rating > 3.5 AND rating <= 4.0 THEN '3.6 - 4.0'
            WHEN rating > 4.0 AND rating <= 4.5 THEN '4.1 - 4.5'
            WHEN rating > 4.5 AND rating <= 5.0 THEN '4.6 - 5.0'
        END as rating_range,
        SUM(total_amount) as revenue
    FROM data
    GROUP BY rating_range
    ORDER BY revenue DESC
    """
    print(run(q4))

    print("\nQ12 Total revenue in Hyderabad:")
    print(run("SELECT SUM(total_amount) FROM data WHERE city = 'Hyderabad'"))

if __name__ == "__main__":
    solve_refined()
