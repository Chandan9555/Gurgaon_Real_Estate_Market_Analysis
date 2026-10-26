# Gurgaon Real Estate Market Analysis 🏠

## 📌 Project Overview

**Gurgaon Real Estate Market Analysis** is a Python-based data analytics project that explores residential property prices and market trends in Gurgaon.

The project uses Python libraries such as Pandas, Matplotlib, and Seaborn to clean real estate data, analyze property pricing, compare localities, evaluate builder pricing, and explore the relationship between property size and price per square foot.

The main objective is to extract meaningful insights from real estate data and understand the factors that influence property prices.

## 🎯 Project Objectives

- Clean and preprocess real estate data using Python.
- Identify the costliest residential property.
- Find localities with the highest average property prices.
- Analyze average property prices across different localities.
- Compare ready-to-move and under-construction properties.
- Examine pricing differences between RERA-approved and non-approved properties.
- Identify expensive BHK configurations and property types.
- Compare builders based on their average price per square foot.
- Explore the relationship between property area and price per square foot.
- Generate useful insights to support real estate market analysis.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Data analysis and processing |
| Pandas | Data cleaning, transformation, and aggregation |
| Matplotlib | Data visualization |
| Seaborn | Statistical data visualization |
| CSV | Dataset storage and input |

## 📂 Project Structure

```text
Gurgaon-Real-Estate-Market-Analysis/
│
├── data.csv
├── main.py
└── README.md
```

**File descriptions:**

- `data.csv` — Contains the real estate dataset used for analysis.
- `main.py` — Python script for data cleaning, analysis, and visualization.
- `README.md` — Documentation describing the project, technologies, and implementation.

## 📊 Dataset Description

The project uses a CSV file named `data.csv`.

The dataset contains real estate attributes used in the analysis, including:

| Column | Description |
|---|---|
| `price` | Property price |
| `area` | Property area in square feet |
| `rate_per_sqft` | Property price per square foot |
| `locality` | Location of the property |
| `bhk_count` | Number of bedrooms |
| `flat_type` | Type or configuration of the flat |
| `status` | Property status, such as ready to move or under construction |
| `rera_approval` | RERA approval status |
| `builder_name` | Builder name used in the costliest-property analysis |
| `company_name` | Company name used in the builder pricing analysis |


## 🧹 Data Cleaning and Preprocessing

The project performs the following data-cleaning operations:

1. **Load the dataset:** Read the CSV file using Pandas.
2. **Standardize column names:** Remove extra spaces, convert column names to lowercase, and replace spaces with underscores.
3. **Clean numeric values:** Remove commas from the `price`, `area`, and `rate_per_sqft` columns and convert them into numeric data types.
4. **Normalize categorical values:** Remove unnecessary spaces and convert property status, flat type, and RERA approval text to lowercase.
5. **Convert RERA approval values:** Map approval descriptions to Boolean values (`True` and `False`).
6. **Remove duplicate records:** Use Pandas to remove duplicate rows.

These operations prepare the dataset for further analysis.

## 🔍 Key Business Questions

The project addresses the following 10 analytical questions:

### 1. Which is the costliest flat?
Identifies the property with the maximum price and displays its BHK configuration, property type, locality, area, price per square foot, status, builder, and RERA approval status.

### 2. Which locality has the highest average property price?
Groups properties by locality and identifies the locality with the highest average price.

### 3. Which locality has the highest average rate per square foot?
Compares the average price per square foot across localities to identify the most expensive locality by this measure.

### 4. Do ready-to-move properties cost more than under-construction properties?
Calculates and compares the average prices of properties in these two construction-status categories.

### 5. Do RERA-approved properties command a price premium?
Compares the average prices of RERA-approved and non-approved properties to investigate pricing differences.

### 6. How does area impact property price?
Explores the relationship between property area and price using a scatter plot. The corresponding plotting code is currently commented out.

### 7. Which BHK configuration has the highest average price per square foot?
Groups properties by BHK count and identifies the configuration with the highest average rate per square foot.

### 8. Which property type has the highest average price?
Compares average property prices across flat types.

### 9. Do certain builders price properties higher?
Ranks companies by their average price per square foot and displays the top five companies.

### 10. Are larger homes more expensive per square foot?
Creates a scatter plot to explore the relationship between property area and price per square foot.

## 📈 Analysis and Visualization

The project combines data analysis and visualization techniques to explore real estate pricing patterns.

**Analytical techniques used:**
- Maximum and average calculations
- Grouping and aggregation
- Category-based comparisons
- Sorting and ranking
- Duplicate removal
- Data type conversion
- Scatter plot visualization

**Visualizations:**
- Property area vs. price per square foot

Additional visualizations can be developed to explore locality-level prices, property status, BHK configurations, and builder pricing.

## 💡 Key Learnings

Through this project, I practiced:

- Data cleaning and preprocessing with Pandas.
- Handling numeric values stored as text.
- Standardizing categorical data.
- Removing duplicate records.
- Applying filtering, grouping, aggregation, and sorting.
- Comparing real estate prices across categories.
- Identifying high-priced properties and localities.
- Creating scatter plots using Seaborn and Matplotlib.
- Translating business questions into Python-based analytical solutions.

## 🚀 Future Improvements

The project can be extended with the following features:

- Add more visualizations for property prices and localities.
- Investigate missing values and inconsistent records.
- Analyze relationships between BHK count, area, and price.
- Compare builder-level pricing patterns.
- Calculate additional real estate KPIs.
- Build an interactive dashboard using Power BI.
- Develop a simple interface for exploring property data.
