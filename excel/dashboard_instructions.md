# Excel Dashboard - Step-by-Step Instructions

This document provides structured instructions on how to build the interactive Financial Analytics Excel Dashboard using the generated `financial_data.csv`.

## Step 1: Import Data
1. Open a new Excel Workbook and name it `dashboard.xlsx`.
2. Go to **Data > Get Data > From Text/CSV** and select `data/financial_data.csv`.
3. Click **Load** (or **Transform Data** in Power Query if you wish to do additional formatting, e.g., formatting currency columns).
4. Name the loaded sheet `Raw Data`.

## Step 2: Create Pivot Tables (Calculation Engine)
Create a new sheet called `Calculation Engine` where all Pivot Tables will reside.

**Pivot Table 1: High-Level KPIs**
* Total Revenue, Total Expense, Total Profit.
* Add a calculated field for **Profit Margin %** = `= 'Profit' / 'Revenue'`.

**Pivot Table 2: P&L Trend (Monthly)**
*   **Rows:** `Year`, `Month` (or Group `Date` by Months and Years).
*   **Values:** Sum of `Revenue`, Sum of `Expense`, Sum of `Profit`.

**Pivot Table 3: Profit by Business Unit**
*   **Rows:** `Business_Unit`
*   **Values:** Sum of `Profit` (Sorted Largest to Smallest)

**Pivot Table 4: Cost Distribution**
*   **Rows:** `Cost_Category`
*   **Values:** Sum of `Expense` (Format as % of Grand Total or Currency)

**Pivot Table 5: Region-wise Performance**
*   **Rows:** `Region`
*   **Values:** Sum of `Profit`

## Step 3: Build the Dashboard UI
Create a new sheet called `Dashboard`. 
1. **Remove Gridlines:** Go to **View** and uncheck **Gridlines**.
2. **Title:** Insert a Text Box at the top for "Financial Analytics Dashboard".
3. **KPI Cards:** Insert Shapes (e.g., Rounded Rectangles) at the top. Link the text in these shapes to the KPI values in the `Calculation Engine` sheet.
    *   *To link: Select the shape, click the formula bar, type `=` and click the cell in the Calculation Engine.*

## Step 4: Add Visualizations
From your `Calculation Engine` Pivot Tables, insert the following **PivotCharts**, and cut/paste them into the `Dashboard` sheet.

1. **Profit & Loss Trend:** Line Chart (from Pivot Table 2).
2. **Profit by Business Unit:** Clustered Column Chart or Bar Chart (from Pivot Table 3).
3. **Cost Breakdown:** Donut or Pie Chart (from Pivot Table 4). Disable the legend and use Data Labels for better visibility.
4. **Region-wise Performance:** Map Chart (if available/supported) or a simple Bar Chart (from Pivot Table 5).

## Step 5: Add Interactivity (Slicers)
1. Click on any PivotChart in the `Dashboard`.
2. Go to **PivotChart Analyze > Insert Slicer**.
3. Select `Year`, `Region`, and `Business_Unit`.
4. Position the Slicers on the left or top of the dashboard.
5. **IMPORTANT:** Right-click each Slicer, select **Report Connections**, and check ALL Pivot Tables you created on the `Calculation Engine` sheet. This ensures that filtering one Slicer updates all charts and KPIs simultaneously.

## Step 6: Formatting and Polish
*   Ensure all charts share a consistent color palette (e.g., Corporate Blues and strategic uses of Green/Red for Profit/Loss).
*   Format numbers as Currency where applicable.
*   Hide the `Raw Data` and `Calculation Engine` sheets to keep the file clean.
