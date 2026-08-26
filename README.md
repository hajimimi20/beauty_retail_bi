# 💄 Beauty Retail BI

### North American Beauty Retail Analytics

An end-to-end **Business Intelligence project** analyzing the beauty retail market across the **United States and Canada**.

Built with **Python, SQL, MariaDB, and Power BI**, this project demonstrates how raw public data can be transformed into business-ready insights through a complete **ETL → Data Modeling → BI** workflow.

---

## 📊 Project at a Glance

| Area                     | Technology   |
| ------------------------ | ------------ |
| 🐍 Data Collection & ETL | Python       |
| 🧹 Data Transformation   | Pandas       |
| 🗄️ Database             | MariaDB      |
| 🔎 Data Analysis         | SQL          |
| 📐 Data Modeling         | Star Schema  |
| 📈 Visualization         | Power BI     |
| 🔢 BI Calculations       | DAX          |
| 🛠️ Development          | VS Code      |
| 📦 Package Management    | uv           |
| 🌿 Version Control       | Git / GitHub |

---

## 🎯 Business Objective

The beauty retail industry is highly competitive, with major retailers operating across multiple markets, categories, brands, and geographic regions.

This project aims to answer:

> **What can public retail data tell us about the North American beauty market?**

Key business questions include:

* 📈 How is beauty retail sales changing over time?
* 🇺🇸 How does the U.S. market compare with Canada?
* 🗺️ Which states and provinces show the strongest performance?
* 💄 Which beauty categories contribute the most revenue?
* 🏷️ Which brands and products perform best?
* 💰 How do price and discount levels relate to sales?
* 📊 Which regions and categories show the strongest growth?

---

# 🌎 Data Sources

The project prioritizes **official public data sources** from North America.

### 🇺🇸 United States

**U.S. Census Bureau**

Retail trade data will be collected through the Census Bureau's public data services.

A key industry classification used in this project is:

```text
NAICS 446120
Cosmetics, Beauty Supplies, and Perfume Retailers
```

Potential metrics include:

* Retail sales
* Monthly sales trends
* Industry activity
* E-commerce sales
* Geographic information

🔗 [U.S. Census Bureau — Retail Trade](https://www.census.gov/retail/)

🔗 [U.S. Census API](https://api.census.gov/data/timeseries/eits/mrts.html)

---

### 🇨🇦 Canada

**Statistics Canada**

Canadian retail information will be collected from Statistics Canada and Canada's open data platform.

Potential data includes:

* Monthly retail sales
* Sales by store type
* Sales by province and territory
* Industry-level retail statistics
* Time-series data

🔗 [Statistics Canada](https://www.statcan.gc.ca/)

🔗 [Government of Canada Open Data](https://open.canada.ca/)

---

### 💄 Beauty Product Data

Additional public beauty-related datasets may be incorporated to provide product-level dimensions such as:

* Brand
* Product
* Category
* Subcategory
* Price
* Rating
* Retailer
* Country

> **Data Principle:** Publicly available data will be used, with the original source documented for each dataset.

---

# 🏗️ Data Architecture

```text
                🌎 Public Data Sources
                         │
          ┌──────────────┼──────────────┐
          │              │              │
       🇺🇸 Census     🇨🇦 StatCan    💄 Product Data
          │              │              │
          └──────────────┼──────────────┘
                         ↓
                  🐍 Python ETL
                         │
              ┌──────────┴──────────┐
              │                     │
           Extract               Transform
              │                     │
              └──────────┬──────────┘
                         ↓
                    Load to DB
                         ↓
                    🗄️ MariaDB
                         ↓
                     🔎 SQL
                         ↓
                 📐 Data Modeling
                         ↓
                    📊 Power BI
                         ↓
              💡 Business Insights
```

---

# 🔄 ETL Pipeline

The project follows a traditional **Extract → Transform → Load** architecture.

### 1️⃣ Extract

Python collects data from public APIs and datasets.

```text
API / Dataset
      ↓
Python
      ↓
Raw Data
```

Tools:

* `requests`
* `BeautifulSoup`
* Public APIs
* CSV / JSON datasets

---

### 2️⃣ Transform

Raw data is cleaned and standardized using Pandas.

Typical transformations include:

```text
✔ Remove duplicates
✔ Handle missing values
✔ Standardize column names
✔ Convert data types
✔ Standardize dates
✔ Normalize geographic names
✔ Standardize product categories
✔ Create calculated fields
✔ Validate data quality
```

---

### 3️⃣ Load

Cleaned data is loaded into MariaDB.

```text
Raw Data
   ↓
Staging Tables
   ↓
Transformation
   ↓
Fact & Dimension Tables
```

---

# 🗄️ Database Design

The database will follow a **dimensional modeling approach** designed for Power BI.

### Fact Tables

| Table                | Purpose                              |
| -------------------- | ------------------------------------ |
| `fact_sales`         | Product-level sales information      |
| `fact_retail_market` | Industry-level retail market metrics |

### Dimension Tables

| Table          | Purpose                            |
| -------------- | ---------------------------------- |
| `dim_date`     | Date and time analysis             |
| `dim_product`  | Product information                |
| `dim_brand`    | Brand information                  |
| `dim_category` | Product category hierarchy         |
| `dim_store`    | Retailer / store information       |
| `dim_location` | Country, state, province, and city |

---

# ⭐ Star Schema

```text
                         dim_date
                            │
                            │
                      ┌─────┴─────┐
                      │           │
                dim_product   dim_store
                      │           │
                      └─────┬─────┘
                            │
                       fact_sales
                            │
                     ┌──────┴──────┐
                     │             │
              dim_category    dim_location
                     │
                  dim_brand
```

The model is designed to provide efficient filtering, aggregation, and reporting in Power BI.

---

# 🔎 SQL Analytics

SQL will be used to transform database tables into business-ready analytical datasets.

Example:

```sql
SELECT
    category,
    SUM(revenue) AS total_revenue
FROM fact_sales
GROUP BY category
ORDER BY total_revenue DESC;
```

### SQL techniques

```text
SELECT / WHERE
JOIN
GROUP BY
CASE WHEN
CTE
Window Functions
Aggregations
Views
Date Analysis
```

---

# 📈 Power BI Dashboard

The final dashboard will focus on **business decision-making rather than simply displaying charts**.

## 01 — Executive Overview

Key KPIs:

* 💰 Total Revenue
* 📦 Units Sold
* 💵 Average Selling Price
* 📈 Revenue Growth
* 🏆 Top Brand
* 💄 Top Category

Visuals:

```text
Revenue Trend
Revenue by Country
Revenue by Category
Top Brands
Monthly Growth
```

---

## 02 — Product & Brand Performance

Explore:

* Top products
* Top brands
* Category performance
* Product mix
* Average product price
* Revenue contribution

Example analysis:

```text
Which brands generate the highest revenue?

Which categories are growing fastest?

Which products contribute the most to sales?
```

---

## 03 — Geographic Performance

Analyze:

```text
🇺🇸 United States
        ↓
State
        ↓
City
```

and

```text
🇨🇦 Canada
        ↓
Province
        ↓
City
```

Potential visuals:

* Sales by State
* Sales by Province
* Regional Revenue
* Market Comparison
* Geographic Growth

---

## 04 — Pricing & Promotion

Analyze the relationship between:

```text
Price
   ↓
Discount
   ↓
Units Sold
   ↓
Revenue
```

Key question:

> **Do discounts appear to increase sales volume?**

---

# 📌 Key Performance Indicators

| KPI                       | Description                      |
| ------------------------- | -------------------------------- |
| **Total Revenue**         | Total sales revenue              |
| **Units Sold**            | Total quantity sold              |
| **Average Selling Price** | Average product selling price    |
| **Revenue Growth**        | Change in revenue over time      |
| **Category Share**        | Revenue contribution by category |
| **Brand Share**           | Revenue contribution by brand    |
| **Regional Revenue**      | Sales by geographic region       |

---

# 🧠 Business Insights

The final stage of the project will translate analytical results into business recommendations.

Examples:

### Product Strategy

Identify high-performing categories and products.

### Regional Strategy

Identify regions with strong sales growth and potential expansion opportunities.

### Pricing Strategy

Analyze whether pricing and discount levels are associated with changes in sales volume.

### Brand Strategy

Identify brands that contribute significantly to overall revenue.

---

# 🛠️ Technology Stack

### Programming

```text
Python
Pandas
Requests
BeautifulSoup
PyMySQL
python-dotenv
```

### Database

```text
MariaDB
HeidiSQL
```

### Business Intelligence

```text
Power BI Desktop
DAX
```

### Development

```text
VS Code
uv
Git
GitHub
```

---

# 📁 Project Structure

```text
beauty-retail-bi/
│
├── 📂 data/
│   ├── raw/
│   └── processed/
│
├── 📂 src/
│   ├── extract/
│   ├── transform/
│   ├── load/
│   └── utils/
│
├── 📂 sql/
│   ├── staging/
│   ├── analytics/
│   └── views/
│
├── 📂 powerbi/
│
├── 📂 notebooks/
│
├── 📂 docs/
│
├── 📂 tests/
│
├── 📄 .env.example
├── 📄 .gitignore
├── 📄 README.md
├── 📄 pyproject.toml
└── 📄 uv.lock
```

---

# 🌿 Git Branch Strategy

The project follows a feature-based Git workflow.

```text
main
 │
 └── develop
       │
       ├── feature/data-collection
       │
       ├── feature/etl-pipeline
       │
       ├── feature/database
       │
       ├── feature/sql-analysis
       │
       ├── feature/data-model
       │
       └── feature/powerbi-dashboard
```

### Branch Responsibilities

| Branch                      | Purpose                   |
| --------------------------- | ------------------------- |
| `main`                      | Stable production version |
| `develop`                   | Integrated development    |
| `feature/data-collection`   | API and data extraction   |
| `feature/etl-pipeline`      | Python ETL                |
| `feature/database`          | MariaDB schema            |
| `feature/sql-analysis`      | SQL analytics             |
| `feature/data-model`        | Dimensional modeling      |
| `feature/powerbi-dashboard` | Power BI and DAX          |

---

# 🔐 Environment Variables

Database credentials are stored locally in `.env`.

```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=beauty_retail
```

Sensitive credentials are excluded from Git using `.gitignore`.

A `.env.example` file is provided for project setup.

---

# 🚀 Development Roadmap

* [x] Define project scope
* [x] Identify North American data sources
* [ ] Create GitHub repository
* [ ] Set up Python environment
* [ ] Build data collection pipeline
* [ ] Collect U.S. retail data
* [ ] Collect Canadian retail data
* [ ] Collect beauty product data
* [ ] Build ETL pipeline
* [ ] Create MariaDB database
* [ ] Build staging tables
* [ ] Build fact & dimension tables
* [ ] Create SQL analytical views
* [ ] Build star schema
* [ ] Connect Power BI
* [ ] Create DAX measures
* [ ] Build dashboard
* [ ] Analyze business insights
* [ ] Document the final project

---

# 📊 Final Deliverables

The completed project will include:

```text
🐍 Python ETL Pipeline
🗄️ MariaDB Database
🔎 SQL Analytics
📐 Star Schema
📊 Power BI Dashboard
💡 Business Insights
📚 Technical Documentation
🌿 GitHub Version Control
```

---

# 🎓 Skills Demonstrated

This project demonstrates practical experience with:

**Data Analytics**

* Data Cleaning
* Exploratory Data Analysis
* Business Analysis
* KPI Development

**Data Engineering**

* API Data Collection
* ETL Pipelines
* Data Transformation
* Database Loading

**Database**

* MariaDB
* SQL
* Relational Modeling
* Dimensional Modeling
* Star Schema

**Business Intelligence**

* Power BI
* DAX
* Data Visualization
* Dashboard Design
* Business Insights

**Development**

* Python
* Git
* GitHub
* Environment Management
* Project Documentation

---

# 👤 Author

### Hajimi

**Data Analyst / Data Engineer**

Focused on:

> **Beauty Industry × Business Analytics × Data**

**Technical Skills**

`Python` · `SQL` · `Power BI` · `ETL` · `Data Modeling` · `Business Intelligence`

---

⭐ If you find this project useful, feel free to explore the repository and the data pipeline.
