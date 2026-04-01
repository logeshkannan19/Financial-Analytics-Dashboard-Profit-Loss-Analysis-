import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def run_analysis():
    # Load the generated dataset
    data_path = '../data/financial_data.csv'
    if not os.path.exists(data_path):
        print(f"Error: Could not find {data_path}. Please run generate_data.py first.")
        return
        
    df = pd.read_csv(data_path)
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Ensure reports directory exists
    os.makedirs('../reports', exist_ok=True)
    
    # 1. Monthly Revenue and Profit Trend (Line Chart)
    plt.figure(figsize=(12, 6))
    monthly_trend = df.groupby(['Year', 'Month'])[['Revenue', 'Profit']].sum().reset_index()
    monthly_trend['YearMonth'] = monthly_trend['Year'].astype(str) + '-' + monthly_trend['Month'].astype(str).str.zfill(2)
    
    sns.lineplot(data=monthly_trend, x='YearMonth', y='Revenue', marker='o', label='Revenue')
    sns.lineplot(data=monthly_trend, x='YearMonth', y='Profit', marker='s', label='Profit')
    plt.xticks(rotation=45)
    plt.title('Monthly Revenue and Profit Trend')
    plt.ylabel('Amount ($)')
    plt.xlabel('Month')
    plt.tight_layout()
    plt.savefig('../reports/monthly_trend.png')
    plt.close()

    # 2. Profit by Business Unit (Bar Chart)
    plt.figure(figsize=(10, 6))
    bu_profit = df.groupby('Business_Unit')['Profit'].sum().sort_values(ascending=False).reset_index()
    sns.barplot(data=bu_profit, x='Profit', y='Business_Unit', palette='viridis')
    plt.title('Total Profit by Business Unit')
    plt.xlabel('Total Profit ($)')
    plt.ylabel('Business Unit')
    plt.tight_layout()
    plt.savefig('../reports/bu_profit.png')
    plt.close()

    # 3. Cost Distribution by Category (Pie Chart)
    plt.figure(figsize=(8, 8))
    cost_dist = df.groupby('Cost_Category')['Expense'].sum()
    plt.pie(cost_dist, labels=cost_dist.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
    plt.title('Cost Distribution by Category')
    plt.tight_layout()
    plt.savefig('../reports/cost_distribution.png')
    plt.close()

    # Generate Insights Report Document
    insights_path = '../reports/business_insights.txt'
    with open(insights_path, 'w') as f:
        f.write("=========================================\n")
        f.write("FINANCIAL ANALYTICS - BUSINESS INSIGHTS\n")
        f.write("=========================================\n\n")
        
        # High Profit BU
        top_bu = bu_profit.iloc[0]['Business_Unit']
        bottom_bu = bu_profit.iloc[-1]['Business_Unit']
        f.write("1. High-Profit and Loss-Making Units:\n")
        f.write(f"   - The highest performing Business Unit is '{top_bu}'.\n")
        f.write(f"   - The lowest performing Business Unit is '{bottom_bu}'. Strategic review is recommended for optimizing operational costs in this unit.\n\n")
        
        # Cost Heavy Category
        top_cost_cat = cost_dist.sort_values(ascending=False).index[0]
        f.write("2. Cost-Heavy Categories:\n")
        f.write(f"   - '{top_cost_cat}' is the most significant cost driver.\n")
        f.write("   - Recommendation: Audit expenses within this category to identify potential negotiation leverage with vendors or efficiency optimizations.\n\n")
        
        # Total metrics
        total_rev = df['Revenue'].sum()
        total_profit = df['Profit'].sum()
        margin = (total_profit / total_rev) * 100
        f.write("3. Overall Performance:\n")
        f.write(f"   - Total Revenue: ${total_rev:,.2f}\n")
        f.write(f"   - Total Profit:  ${total_profit:,.2f}\n")
        f.write(f"   - Overall Profit Margin: {margin:.2f}%\n")

    print("Data analysis complete. Visualizations and insights saved in the 'reports' folder.")

if __name__ == "__main__":
    print("Running Python financial analysis...")
    run_analysis()
