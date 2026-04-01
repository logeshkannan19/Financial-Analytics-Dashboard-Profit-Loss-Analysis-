-- ===============================================================================
-- FINANCIAL ANALYTICS DASHBOARD - SQL QUERIES
-- Database setup: PostgreSQL / MySQL
-- Table: financial_data
-- Note: It is assumed that the data has been loaded into a table named 'financial_data'
-- ===============================================================================

-- -------------------------------------------------------------------------------
-- 1. Total Revenue, Total Expense, Total Profit
-- -------------------------------------------------------------------------------
SELECT 
    SUM(Revenue) AS Total_Revenue,
    SUM(Expense) AS Total_Expense,
    SUM(Profit) AS Total_Profit,
    ROUND(SUM(Profit) / SUM(Revenue) * 100, 2) AS Overall_Profit_Margin_Pct
FROM 
    financial_data;

-- -------------------------------------------------------------------------------
-- 2. Monthly Profit & Loss Trend
-- -------------------------------------------------------------------------------
SELECT 
    Year, 
    Month, 
    SUM(Revenue) AS Monthly_Revenue, 
    SUM(Expense) AS Monthly_Expense, 
    SUM(Profit) AS Monthly_Profit
FROM 
    financial_data
GROUP BY 
    Year, Month
ORDER BY 
    Year ASC, Month ASC;

-- -------------------------------------------------------------------------------
-- 3. Profit by Business Unit
-- -------------------------------------------------------------------------------
SELECT 
    Business_Unit, 
    SUM(Revenue) AS Total_Revenue, 
    SUM(Profit) AS Total_Profit,
    ROUND(SUM(Profit) / SUM(Revenue) * 100, 2) AS Margin_Pct
FROM 
    financial_data
GROUP BY 
    Business_Unit
ORDER BY 
    Total_Profit DESC;

-- -------------------------------------------------------------------------------
-- 4. Top Performing Units (By Profit Margin)
-- -------------------------------------------------------------------------------
SELECT 
    Business_Unit, 
    SUM(Profit) AS Total_Profit,
    ROUND(SUM(Profit) / SUM(Revenue) * 100, 2) AS Margin_Pct
FROM 
    financial_data
GROUP BY 
    Business_Unit
HAVING 
    SUM(Revenue) > 0
ORDER BY 
    Margin_Pct DESC
LIMIT 5;

-- -------------------------------------------------------------------------------
-- 5. Cost Distribution by Category
-- -------------------------------------------------------------------------------
SELECT 
    Cost_Category, 
    SUM(Expense) AS Total_Cost,
    ROUND(SUM(Expense) / (SELECT SUM(Expense) FROM financial_data) * 100, 2) AS Pct_Of_Total_Cost
FROM 
    financial_data
GROUP BY 
    Cost_Category
ORDER BY 
    Total_Cost DESC;

-- -------------------------------------------------------------------------------
-- 6. Region-wise Financial Performance
-- -------------------------------------------------------------------------------
SELECT 
    Region, 
    SUM(Revenue) AS Regional_Revenue, 
    SUM(Profit) AS Regional_Profit,
    ROUND(SUM(Profit) / SUM(Revenue) * 100, 2) AS Margin_Pct
FROM 
    financial_data
GROUP BY 
    Region
ORDER BY 
    Regional_Profit DESC;

-- -------------------------------------------------------------------------------
-- 7. Profit Margin Analysis by Product/Service
-- -------------------------------------------------------------------------------
SELECT 
    Product_Service, 
    SUM(Revenue) AS Revenue,
    SUM(Profit) AS Profit,
    ROUND(SUM(Profit) / SUM(Revenue) * 100, 2) AS Margin_Pct
FROM 
    financial_data
GROUP BY 
    Product_Service
ORDER BY 
    Margin_Pct DESC, Revenue DESC
LIMIT 10;
