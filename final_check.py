import pandas as pd
import sqlite3

def final_check():
    df = pd.read_csv('final_food_delivery_dataset.csv')
    conn = sqlite3.connect(':memory:')
    df.to_sql('data', conn, index=False)

    print("="*50)
    print("      FINAL VALIDATION CHECKS")
    print("="*50)

    # Q8 check
    print("\n[Check Q8] Highest AOV but < 20 orders:")
    q8 = """
    SELECT restaurant_name, AVG(total_amount), COUNT(*)
    FROM data
    WHERE restaurant_name IN ('Grand Cafe Punjabi', 'Grand Restaurant South Indian', 'Ruchi Mess Multicuisine', 'Ruchi Foods Chinese')
    GROUP BY restaurant_name
    """
    print(pd.read_sql(q8, conn))

    # Q15 check
    print("\n[Check Q15] Rating >= 4.5 Count:")
    print(pd.read_sql("SELECT COUNT(*) FROM data WHERE rating >= 4.5", conn))

if __name__ == "__main__":
    final_check()
