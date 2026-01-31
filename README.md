# 🍔 Food Delivery Data Analysis Hackathon

A comprehensive data engineering and analysis project that integrates transactional, user, and restaurant data from multiple formats (CSV, JSON, SQL) into a single source of truth for business intelligence.

## 🚀 Project Overview

In this project, we process data from three disparate real-world systems:
1.  **Transactional Data (`orders.csv`):** Contains order IDs, user links, restaurant IDs, and transaction amounts.
2.  **User Master Data (`users.json`):** Contains user demographics and membership tiers (Gold vs Regular).
3.  **Restaurant Master Data (`restaurants.sql`):** SQL insert statements containing restaurant details, cuisine types, and satisfaction ratings.

### Goals:
*   Merge multi-format datasets using Python/Pandas.
*   Perform automated Data Cleaning and ETL.
*   Execute SQL-based analysis to derive business insights on revenue, user behavior, and cuisine performance.

---

## 📂 Repository Structure

```text
GenAI_Hackathon/
│
├── final_check.py
├── final_food_delivery_dataset.csv
├── merge_data.py
├── orders.csv
├── README.md
├── requirements.txt
├── restaurants.sql
├── solve_questions.py
├── solve_refined.py
└── users.json
```


## 🛠️ Setup and Installation

1.  **Clone the repository:**
    ```bash
    https://github.com/Priyadharshini-cbe/final_food_delivery_dataset.git
    cd final-food-delivery-dataset
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the ETL pipeline:**
    ```bash
    python merge_data.py
    ```

---

## 📊 Business Insights (Hackathon Results)

Based on the consolidated dataset, the following insights were derived:

### Key Performance Indicators
- **Top Revenue City (Gold Members):** Chennai
- **Most Profitable Cuisine:** Mexican (Highest Average Order Value)
- **Membership Impact:** Gold members contribute ~50% of total order volume.
- **Top Seasonality:** Q3 (July–September) generated the highest revenue.

### Analysis Summary Table
| Metric | Result |
| :--- | :--- |
| **Total Orders Processed** | 10,000 |
| **Distinct Users** | 2,883 |
| **Avg Order Value (Gold)** | ₹797.15 |
| **Top Rated Restaurant Performance** | 3,374 orders for restaurants rated ≥ 4.5 |

---

## 🔍 Data Architecture

The integration follows a **Left Join** strategy to ensure no transactional data from `orders.csv` is lost.
*   **Key 1:** `orders.user_id` ➔ `users.user_id`
*   **Key 2:** `orders.restaurant_id` ➔ `restaurants.restaurant_id`

---

## 📝 Technologies Used
- **Language:** Python 3
- **Libraries:** Pandas, SQLite, Regex
- **Database Engine:** SQLite (In-Memory for Analysis)
- **Version Control:** Git

Developed as part of the GenAI Hackathon.
