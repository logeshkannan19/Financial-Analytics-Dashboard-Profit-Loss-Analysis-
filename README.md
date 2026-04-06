<p align="center">
  <img src="https://readme-jitsu.vercel.app/api/vis/svg?username=Financial-Analytics-Dashboard-Profit-Loss-Analysis-&title=Financial+Analytics+Dashboard&description=Profit+%26+Loss+Analysis+Platform&theme=vue-dark&align=center&title-align=center&description-align=center" width="100%" />
</p>

<h1 align="center">Financial Analytics Dashboard</h1>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"></a>
  <a href="https://www.postgresql.org/"><img src="https://img.shields.io/badge/Database-PostgreSQL_/_MySQL-4479A1?style=for-the-badge&logo=postgresql&logoColor=white" alt="Database"></a>
  <a href="https://products.office.com/en-us/excel"><img src="https://img.shields.io/badge/Visualization-Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white" alt="Excel"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License"></a>
</p>

<p align="center">
  <b>An end-to-end financial analytics platform for profit and loss analysis, enabling KPI tracking, revenue insights, and strategic decision-making through data visualization.</b>
</p>

---

<div align="center">

| [Features](#features) | [Architecture](#architecture) | [Tech Stack](#tech-stack) | [Getting Started](#getting-started) | [Project Structure](#project-structure) | [Data Model](#data-model) |
|:---:|:---:|:---:|:---:|:---:|:---:|

</div>

---

## 🚀 Features

| Feature | Description |
|:---|:---|
| **Synthetic Data Generation** | Generate 5,000+ realistic financial records with configurable parameters |
| **SQL Analytics Engine** | Comprehensive query suite for margin analysis, business unit performance, and regional insights |
| **Advanced Python Analytics** | Programmatic analysis using Pandas, NumPy, Matplotlib, and Seaborn |
| **Interactive Excel Dashboard** | Dynamic Pivot Tables, Charts, and Slicers for filtered data exploration |
| **Automated Reporting** | Export high-definition visualizations and business insights automatically |

---

## 🏗️ Architecture

### System Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              SYSTEM ARCHITECTURE                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌──────────┐ │
│  │   Source    │     │  Storage    │     │  Analysis   │     │  Output  │ │
│  │   Layer     │────▶│   Layer     │────▶│   Layer     │────▶│   Layer  │ │
│  └─────────────┘     └─────────────┘     └─────────────┘     └──────────┘ │
│                                                                             │
│  ┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌──────────┐ │
│  │  generate  │     │   CSV File   │     │   SQL/      │     │  Excel   │ │
│  │  _data.py  │     │  (5K+ rows)  │     │   Python    │     │ Dashboard│ │
│  └─────────────┘     └─────────────┘     └─────────────┘     └──────────┘ │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Data Pipeline

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                               DATA FLOW PIPELINE                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Stage 1: Generation          Stage 2: Storage          Stage3: Analysis│
│  ┌──────────────────┐       ┌──────────────────┐       ┌────────────────┐   │
│  │  scripts/        │       │  data/           │       │  sql/          │   │
│  │  generate_data   │──────▶│  financial_data  │──────▶│  queries.sql   │   │
│  │      .py         │       │      .csv        │       │                │   │
│  └──────────────────┘       └──────────────────┘       └────────────────┘   │
│                                    │                        │                │
│                                    │                        ▼                │
│                                    │              ┌────────────────────────┐│
│                                    │              │   scripts/              ││
│                                    │              │   financial_analysis.py ││
│                                    │              └────────────────────────┘│
│                                    │                        │                │
│                                    ▼                        ▼                │
│                          ┌──────────────────┐       ┌────────────────┐   │
│                          │  excel/           │       │  reports/      │   │
│                          │  dashboard.xlsx   │       │  *.png, *.txt  │   │
│                          └──────────────────┘       └────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Component Architecture

#### 1. Data Generation Layer (`scripts/generate_data.py`)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        DATA GENERATION ENGINE                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌──────────────────┐      ┌──────────────────┐      ┌─────────────────┐ │
│  │ Configuration   │─────▶│ Generation Core  │─────▶│ CSV Exporter    │ │
│  │ Parameters      │      │ (5,000+ records) │      │                 │ │
│  └──────────────────┘      └──────────────────┘      └─────────────────┘ │
│                                                                             │
│  Output Fields:                                                             │
│  ├── transaction_id    (UUID)     ├── cost_of_goods_sold (DECIMAL)          │
│  ├── date              (DATE)     ├── operating_expenses  (DECIMAL)        │
│  ├── business_unit     (VARCHAR)  ├── profit             (DECIMAL)         │
│  ├── region            (VARCHAR)  └── margin_percentage  (DECIMAL)        │
│  └── revenue           (DECIMAL)                                             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### 2. SQL Analytics Layer (`sql/queries.sql`)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           SQL ANALYTICS SUITE                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Query Categories:                                                          │
│  ├── Revenue Analysis     │ Cost Analysis                                   │
│  │  By Business Unit     │  By Category                                    │
│  │  By Region            │  By Business Unit                               │
│  │  By Time Period       │  Trend Analysis                                 │
│  ├───────────────────────┼──────────────────────────                        │
│  │ Profit & Margin       │ Advanced Analytics                              │
│  │  Margin Trends       │  YoY/QoQ Growth                                  │
│  │  Unit Performance    │  Running Totals                                  │
│  │  Regional Comparison │  Ranking & Percentiles                         │
│  └───────────────────────┴──────────────────────────                        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### 3. Analytics Engine (`scripts/financial_analysis.py`)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         ANALYTICS ENGINE                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌──────────────┐     ┌──────────────┐     ┌──────────────┐                 │
│  │ Data Loader │────▶│  Processing  │────▶│  Visualization│                │
│  │  (Pandas)   │     │  (Transform) │     │  (Charts)    │                │
│  └──────────────┘     └──────────────┘     └──────────────┘                 │
│                                                                             │
│  Outputs:                                                                   │
│  ├── bu_profit.png         - Profit by Business Unit                       │
│  ├── cost_distribution.png - Cost breakdown analysis                       │
│  ├── monthly_trend.png    - P&L trend over time                           │
│  └── business_insights.txt - Automated insights                            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### 4. Dashboard Framework (`excel/dashboard.xlsx`)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       INTERACTIVE DASHBOARD                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  KPI Cards  │  KPI Cards  │  KPI Cards  │  KPI Cards              │   │
│  ├─────────────────────────────────────────────────────────────────────┤   │
│  │                                                                     │   │
│  │          Revenue vs Expenses (Line)    │  Business Unit (Bar)    │   │
│  │                                                                     │   │
│  ├─────────────────────────────────────────────────────────────────────┤   │
│  │                                                                     │   │
│  │          Cost Distribution (Pie)        │  Regional (Bar)        │   │
│  │                                                                     │   │
│  ├─────────────────────────────────────────────────────────────────────┤   │
│  │  [Business Unit ▼] [Region ▼] [Year ▼] [Quarter ▼]               │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|:---|:---|:---|
| **Language** | Python 3.9+ | Core programming |
| **Data Processing** | Pandas, NumPy | Data manipulation & computation |
| **Visualization** | Matplotlib, Seaborn | Static chart generation |
| **Database** | PostgreSQL / MySQL | Data storage (optional) |
| **Dashboard** | Microsoft Excel 2016+ | Interactive visualization |
| **Query Language** | ANSI SQL | Data analytics |

### Dependencies

```txt
pandas>=1.5.0
numpy>=1.21.0
matplotlib>=3.5.0
seaborn>=0.11.0
```

---

## 🏁 Getting Started

### Prerequisites

| Requirement | Version |
|:---|:---|
| Python | 3.9+ |
| PostgreSQL / MySQL | 13+ (optional) |
| Microsoft Excel | 2016+ |

### Installation

```bash
# Clone the repository
git clone https://github.com/logeshkannan19/Financial-Analytics-Dashboard-Profit-Loss-Analysis-.git
cd financial_analytics_dashboard

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # Linux / macOS
# or
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
```

### Usage

#### Step 1: Generate Synthetic Data

```bash
cd scripts
python generate_data.py
```

#### Step 2: Run Analytics Engine

```bash
python financial_analysis.py
```

#### Step 3: Execute SQL Queries

```bash
# PostgreSQL
psql -d financial_db -f sql/queries.sql

# MySQL
mysql financial_db < sql/queries.sql
```

#### Step 4: Build Excel Dashboard

1. Open `excel/dashboard.xlsx`
2. Follow `excel/dashboard_instructions.md`
3. Connect data source to `data/financial_data.csv`

---

## 📂 Project Structure

```
financial_analytics_dashboard/
│
├── 📁 data/                                    # Data storage
│   ├── financial_data.csv                       # Generated dataset
│   └── README.md                                # Data dictionary
│
├── 📁 excel/                                   # Dashboard layer
│   ├── dashboard.xlsx                          # Interactive workbook
│   └── dashboard_instructions.md               # Setup guide
│
├── 📁 reports/                                 # Output artifacts
│   ├── business_insights.txt                  # Generated insights
│   ├── bu_profit.png                          # Profit visualization
│   ├── cost_distribution.png                  # Cost breakdown
│   └── monthly_trend.png                      # Trend analysis
│
├── 📁 scripts/                                 # Processing scripts
│   ├── generate_data.py                        # Data generator
│   └── financial_analysis.py                  # Analytics engine
│
├── 📁 sql/                                     # Query definitions
│   └── queries.sql                             # SQL analytics
│
└── 📄 README.md                                # Documentation
```

---

## 🗃️ Data Model

### Entity Relationship

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              ENTITY RELATIONSHIP                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ┌──────────────────┐                                                    │
│   │  financial_data  │                                                    │
│   ├──────────────────┤                                                    │
│   │ PK transaction_id│                                                    │
│   ├──────────────────┤                                                    │
│   │    date          │                                                    │
│   │    business_unit │                                                    │
│   │    region        │                                                    │
│   │    revenue       │                                                    │
│   │    cogs          │──┐                                                 │
│   │    opex          │  │── Profit (computed)                             │
│   │    profit        │◀─┘                                                 │
│   │    margin_pct    │◀──── Margin % (computed)                           │
│   └──────────────────┘                                                    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Schema Definition

```sql
CREATE TABLE financial_data (
    transaction_id       UUID PRIMARY KEY,
    date                DATE NOT NULL,
    business_unit       VARCHAR(50) NOT NULL,
    region              VARCHAR(20) NOT NULL,
    revenue             DECIMAL(12, 2) NOT NULL,
    cost_of_goods_sold  DECIMAL(12, 2) NOT NULL,
    operating_expenses  DECIMAL(12, 2) NOT NULL,
    profit              DECIMAL(12, 2) GENERATED ALWAYS AS 
                       (revenue - cost_of_goods_sold - operating_expenses) STORED,
    margin_percentage   DECIMAL(5, 2) GENERATED ALWAYS AS 
                       ((revenue - cost_of_goods_sold - operating_expenses) / NULLIF(revenue, 0) * 100) STORED
);
```

### Field Reference

| Field | Type | Description |
|:---|:---|:---|
| `transaction_id` | UUID | Unique transaction identifier |
| `date` | DATE | Transaction date (YYYY-MM-DD) |
| `business_unit` | VARCHAR | Business unit (Cloud, Retail, Healthcare, etc.) |
| `region` | VARCHAR | Geographic region (North, South, East, West) |
| `revenue` | DECIMAL(12,2) | Total revenue |
| `cost_of_goods_sold` | DECIMAL(12,2) | Direct production costs |
| `operating_expenses` | DECIMAL(12,2) | Indirect costs |
| `profit` | DECIMAL(12,2) | Computed: revenue - COGS - opex |
| `margin_percentage` | DECIMAL(5,2) | Computed: (profit/revenue) * 100 |

---

## ⚙️ Configuration

### Data Generator Settings

```python
# scripts/generate_data.py

CONFIG = {
    'record_count': 5000,
    'business_units': [
        'Cloud Infrastructure',
        'Retail',
        'Healthcare',
        'Manufacturing',
        'Finance'
    ],
    'regions': ['North', 'South', 'East', 'West'],
    'date_range': {
        'start': '2023-01-01',
        'end': '2024-12-31'
    },
    'revenue_range': (1000, 50000),
    'cogs_percentage': (0.3, 0.6),
    'opex_percentage': (0.2, 0.4)
}
```

---

## 📊 Output Artifacts

| File | Type | Description |
|:---|:---|:---|
| `data/financial_data.csv` | CSV | Generated dataset (5,000+ records) |
| `reports/business_insights.txt` | TXT | Automated insights |
| `reports/bu_profit.png` | PNG | Business unit profit chart |
| `reports/cost_distribution.png` | PNG | Cost breakdown chart |
| `reports/monthly_trend.png` | PNG | P&L trend visualization |

---

## 📈 Business Insights

| Category | Insight | Recommendation |
|:---|:---|:---|
| **Profitability** | Cloud Infrastructure leads in profit margins | Maintain investment focus |
| **Cost Optimization** | Salaries and R&D are top cost drivers | Conduct efficiency audit |
| **Underperforming** | Retail shows negative margins | Optimize operations |
| **Trends** | Steady YoY profit margin growth | Monitor quarterly metrics |

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  <b>Built with</b> <a href="https://www.python.org/">Python</a> • <a href="https://www.postgresql.org/">SQL</a> • <a href="https://products.office.com/en-us/excel">Excel</a>
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=Financial-Analytics-Dashboard-Profit-Loss-Analysis-&label=Views&color=0e75b6&style=flat" alt="Profile views" />
</p>