import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Parameters for data generation
NUM_RECORDS = 5000
START_DATE = datetime(2023, 1, 1)
END_DATE = datetime(2024, 12, 31)

# Categorical data
business_units = ['Retail', 'Enterprise Software', 'Consulting Services', 'Hardware', 'Cloud Infrastructure']
regions = ['North America', 'Europe', 'Asia Pacific', 'Latin America']
cost_categories = ['Marketing', 'Operations', 'Salaries', 'R&D', 'Software Licenses', 'Logistics', 'Real Estate']

# Helper to generate random dates
def random_date(start, end):
    delta = end - start
    random_days = random.randrange(delta.days)
    return start + timedelta(days=random_days)

def generate_financial_data(num_records):
    data = []
    for i in range(num_records):
        txn_id = f"TXN-{100000 + i}"
        txn_date = random_date(START_DATE, END_DATE)
        bu = random.choice(business_units)
        region = random.choice(regions)
        category = random.choice(cost_categories)
        
        # Add basic logic to make numbers somewhat realistic per BU
        base_rev_multiplier = {
            'Retail': 1.0,
            'Enterprise Software': 3.5,
            'Consulting Services': 2.0,
            'Hardware': 2.5,
            'Cloud Infrastructure': 4.0
        }
        
        # Generate revenue (some variance based on bu)
        revenue = round(random.uniform(5000, 50000) * base_rev_multiplier[bu], 2)
        
        # Generate expense (ensuring mostly profitable, with some loss-making records)
        margin_percent = random.uniform(-0.15, 0.45) # Margins from -15% to 45%
        expense = round(revenue * (1 - margin_percent), 2)
        
        # Ensure 'Salaries' and 'R&D' have higher costs sometimes
        if category in ['Salaries', 'R&D']:
            expense = round(expense * random.uniform(1.1, 1.3), 2)
            
        profit = round(revenue - expense, 2)
        
        # Product / Service assignment
        product_service = f"{bu} - Product {random.randint(1, 5)}"
        
        data.append({
            'Transaction_ID': txn_id,
            'Date': txn_date.strftime('%Y-%m-%d'),
            'Business_Unit': bu,
            'Region': region,
            'Cost_Category': category,
            'Product_Service': product_service,
            'Revenue': revenue,
            'Expense': expense,
            'Profit': profit
        })
    
    df = pd.DataFrame(data)
    
    # Sort by date
    df = df.sort_values(by='Date').reset_index(drop=True)
    
    # Calculate extra columns as requested
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.month
    df['Quarter'] = df['Date'].dt.quarter
    df['Year'] = df['Date'].dt.year
    df['Profit_Margin'] = (df['Profit'] / df['Revenue']).round(4)
    
    return df

if __name__ == "__main__":
    print("Generating synthetic financial data...")
    df = generate_financial_data(NUM_RECORDS)
    
    # Ensure data directory exists
    os.makedirs('../data', exist_ok=True)
    
    output_path = '../data/financial_data.csv'
    df.to_csv(output_path, index=False)
    print(f"Successfully generated {NUM_RECORDS} records and saved to {output_path}")
    print(df.head())
