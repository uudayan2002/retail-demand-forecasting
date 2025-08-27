# Retail Demand Forecasting using PySpark & Prophet

## Project Overview
This project demonstrates **retail demand forecasting** using a large-scale sales dataset.  
We leverage **PySpark** for big data preprocessing and **Facebook Prophet** for time series forecasting.  

The goal is to:
  - Analyze sales trends.  
  - Identify seasonality and demand cycles.  
  - Forecast future demand for product sub-categories such as **Chairs, Tables, Binders, Phones**, etc.  

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
  - **PySpark** → Distributed big data processing.  
  - **Prophet** → Time series forecasting.  
  - **Matplotlib / Seaborn** → Data visualization.  
  - **Pandas** → Lightweight manipulation after Spark aggregations.  

---

## Workflow

### 🔹 Step 1: Data Loading & Cleaning (PySpark)
    - Imported dataset into Spark DataFrame.  
    - Converted date columns into timestamp format.  
    - Selected relevant columns (**Order Date, Sales, Sub-Category**).  
    - Handled missing values and inconsistencies.  

### 🔹 Step 2: Exploratory Data Analysis (EDA)
    - Identified top-selling sub-categories.  
    - Analyzed sales distribution across years.  
    - Visualized growth trends over time.  

### 🔹 Step 3: Time Series Preparation
  - Focused on one sub-category (e.g., **Chairs**) for initial forecast.  
  - Grouped data by **Order Date**, aggregated Sales.  
  - Renamed columns to Prophet format:  
    - `ds` = Date  
    - `y` = Sales  

### 🔹 Step 4: Forecasting with Prophet
  - Initialized model: `Prophet(daily_seasonality=True)`.  
  - Fitted on historical data.  
  - Generated forecasts for the next **180 days**.  

### 🔹 Step 5: Visualization of Forecast
  - **Forecast Plot**: Actual vs Predicted sales with confidence intervals.  
  - **Component Plots**: Trend, Seasonality, Residuals.  

### 🔹 Step 6: Scaling to Multiple Sub-Categories
  - Repeated process for other sub-categories (**Tables, Phones, Binders**).  
  - Compared forecasts across product lines.  
  - Insights supported inventory planning & demand management.  

---

## Results & Insights
### 🔸 Example: Chairs
  - Historical sales show consistent growth.  
  - Seasonal spikes detected (quarterly corporate purchases).  
  - Prophet predicts **steady demand rise** with periodic fluctuations.  

### 🔸 General Observations
  - **Office Supplies** → Frequent smaller orders.  
  - **Technology (Phones, Accessories)** → Sharp spikes (promotions/new launches).  
  - **Furniture** → Long-term growth (useful for warehouse planning).  

---

## Future Work
  - Extend to **multivariate forecasting** (include promotions, holidays, regional data).
  - Automate forecasting pipeline (weekly updates).  
  - Deploy results with **Power BI** dashboards for real-time use.  

---

## Forecast Plot for chairs

