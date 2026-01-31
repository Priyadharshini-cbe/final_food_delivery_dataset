import pandas as pd
import sqlite3
import os

def run_analysis():
    # Load the integrated dataset
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(script_dir)
    file_path = os.path.join(base_dir, 'final_food_delivery_dataset.csv')
    
    if not os.path.exists(file_path):
        print(f"[!] Error: {file_path} not found. Run merge_data.py first.")
        return

    df = pd.read_csv(file_path)
    df['order_date'] = pd.to_datetime(df['order_date'], format='%d-%m-%Y')
    
    # Setup SQL connection for complex analysis
    conn = sqlite3.connect(':memory:')
    df.to_sql('orders', conn, index=False)
    
    def q(sql):
        return pd.read_sql(sql, conn)

    print("="*50)
    print("      FOOD DELIVERY DATA ANALYSIS REPORT")
    print("="*50)

    # 1. Top Revenue City for Gold
    top_city_gold = q("""
        SELECT city, SUM(total_amount) as revenue 
        FROM orders WHERE membership = 'Gold' 
        GROUP BY city ORDER BY revenue DESC LIMIT 1
    """)
    print(f"1. Top Revenue City (Gold): {top_city_gold.iloc[0]['city']} (₹{top_city_gold.iloc[0]['revenue']:,.2f})")

    # 2. Top AOV Cuisine
    top_cuisine_aov = q("SELECT cuisine, AVG(total_amount) as aov FROM orders GROUP BY cuisine ORDER BY aov DESC LIMIT 1")
    print(f"2. Cuisine with Highest Avg Order Value: {top_cuisine_aov.iloc[0]['cuisine']} (₹{top_cuisine_aov.iloc[0]['aov']:.2f})")

    # 3. Users with > 1000 Total
    high_value_users = q("SELECT COUNT(*) as count FROM (SELECT user_id FROM orders GROUP BY user_id HAVING SUM(total_amount) > 1000)")
    print(f"3. Distinct Users with total spend > ₹1000: {high_value_users.iloc[0]['count']}")

    # 4. Rating Range
    rating_rev = q("""
        SELECT 
            CASE 
                WHEN rating BETWEEN 3.0 AND 3.5 THEN '3.0 - 3.5'
                WHEN rating > 3.5 AND rating <= 4.0 THEN '3.6 - 4.0'
                WHEN rating > 4.0 AND rating <= 4.5 THEN '4.1 - 4.5'
                WHEN rating > 4.5 AND rating <= 5.0 THEN '4.6 - 5.0'
            END as range,
            SUM(total_amount) as revenue
        FROM orders GROUP BY range ORDER BY revenue DESC LIMIT 1
    """)
    print(f"4. Top Revenue Rating Range: {rating_rev.iloc[0]['range']}")

    # 5. Top Seasonality
    quarterly = q("""
        SELECT (CAST(strftime('%m', order_date) AS INT) - 1) / 3 + 1 as quarter, SUM(total_amount) as revenue
        FROM orders GROUP BY quarter ORDER BY revenue DESC LIMIT 1
    """)
    print(f"5. Highest Revenue Quarter: Q{int(quarterly.iloc[0]['quarter'])}")

    # 6. Gold Member Stats
    gold_stats = q("SELECT COUNT(*) as c, AVG(total_amount) as aov FROM orders WHERE membership = 'Gold'")
    print(f"6. Gold Stats: {gold_stats.iloc[0]['c']} orders, Avg ₹{gold_stats.iloc[0]['aov']:.2f}")

    print("="*50)
    print("✓ Analysis Engine Execution Successful")

if __name__ == "__main__":
    run_analysis()
