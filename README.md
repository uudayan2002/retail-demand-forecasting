# Retail Demand Forecasting using PySpark & Prophet

## Project Overview
This project demonstrates how to combine big data processing with **PySpark** and time series forecasting with **Prophet**.

We first perform **Exploratory Data Analysis (EDA)** on a large dataset using **PySpark** for scalability, and then apply **Prophet (by Facebook)** to forecast future values.

The project highlights:
  - How **PySpark** helps in cleaning, transforming, and summarizing large datasets.
  - How **Prophet** uses those prepared time series features to generate accurate forecasts.  
  - How **EDA** and forecasting are connected in a real-world data science pipeline.

---

## Dataset Description
The dataset contains retail sales transactions with the following relevant columns:

  - **Row ID** – Unique identifier for each record.  
  - **Order ID** – Unique order identifier.  
  - **Order Date** – Date when the order was placed.  
  - **Ship Date** – Date when the order was shipped.  
  - **Ship Mode** – Delivery method (e.g., First Class, Second Class).  
  - **Customer ID / Customer Name** – Customer information.  
  - **Segment** – Market segment (Consumer, Corporate, Home Office).  
  - **Country / City / State / Region** – Geographical data.  
  - **Product ID / Category / Sub-Category / Product Name** – Product details.  
  - **Sales** – Sales revenue.  

---

## Tools & Libraries Used
  - **Python 3**
  - **PySpark** → Distributed big data processing.  
  - **Prophet** → Time series forecasting.  
  - **Matplotlib / Seaborn** → Data visualization.  
  - **Pandas** → Lightweight manipulation after Spark aggregations.
  - **Jupyter Notebook** 

---

## Workflow

- ### 1. Exploratory Data Analysis (EDA) with PySpark
    - Why PySpark?
      
      PySpark is used because it can handle large datasets efficiently compared to pandas.
      In this project, the dataset is big enough that using Spark avoids memory issues.
      
    - Steps implemented:
      - Loading the dataset into a Spark DataFrame.
      - Performing summary statistics (mean, median, min, max).
      - Cleaning and handling missing/null values.
      - Converting date columns into proper formats.
      - Aggregating values over time (e.g., daily/weekly totals).
    - Connection to Forecasting:
      This stage ensures the dataset is structured into a time series format (with ds = date/time and y = target variable), which Prophet requires.

- ### 2. Forecasting with Prophet
    - **Why Prophet?**
      
      Prophet is designed for business time series (with trends, seasonality, holidays). It is easy to use, robust, and interpretable.
      
    - **Steps implemented:**
      - Installing and importing Prophet.
      - Preparing the dataset from PySpark output:
        - Rename columns to Prophet format:
          - ds → Date column
          - y → Value to forecast
      - Creating a Prophet model and fitting it to the cleaned time series data.
      - Generating a future dataframe (e.g., next 365 days).
      - Forecasting future values.
      - Visualizing results with Prophet’s built-in plotting functions.
        
    - **Connection to EDA**
      
      Prophet cannot work directly on raw messy data. The EDA step ensured the dataset was cleaned, time-indexed, and aggregated, making it directly usable by Prophet.

---

## Results & Insights
- **Trends Identified**: The model highlights underlying trends, seasonality, and growth patterns in the dataset.
- **Forecasting**: Future values are predicted with confidence intervals, visualized using Prophet’s plotting tools.  
- **Scalability**: Using PySpark ensures this approach works for datasets much larger than what pandas can handle.

---

## Future Work
  - Extend to **multivariate forecasting** (include promotions, holidays, regional data).
  - Automate forecasting pipeline (weekly updates).  
  - Deploy results with **Power BI** dashboards for real-time use.  

---

## Forecast Plot for chairs

![Forecast Plot](outputs/forecast(chairs).png)
![Forecast Plot](outputs/trends(chairs).png)

