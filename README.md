# House Price Prediction using Web Scraping and Machine Learning

## Overview
This project focuses on predicting house prices in Baku using a dataset obtained through web scraping. The process involves four key steps: web scraping, exploratory data analysis (EDA), feature engineering, and model building. The extracted data is cleaned, processed, and used to train a predictive model.


## Web Scraping
The `scrapy.py` script automates the extraction of house listing details from `bina.az`. The script uses Selenium to navigate multiple pages and BeautifulSoup to parse the HTML content. The extracted data includes:
- **Price** of the house
- **Location** of the property
- **Room and floor details**

After extracting the data, it is saved into `House.csv` for further processing.

## Exploratory Data Analysis (EDA)
In `houseprice_prediction.ipynb`, the dataset is explored and cleaned:
- **Handling missing values**
- **Checking the distribution of numerical features**
- **Visualizing correlations between variables using heatmaps**
- **Correlation analysis**: Identifying the strongest predictors of price
- **Skewness analysis**: Transforming features to improve model stability
- **Boxplots**: Identifying and handling outliers
- **Log transformation** applied to reduce skewness in price and area

## Feature Engineering
To improve the predictive power of the model, the following new features are created:
- **`price_per_sqm`**: Price per square meter
- **`room_area_ratio`**: Ratio of room count to total area
- **`floor_ratio`**: Current floor divided by maximum floor
- **Encoding categorical features** (e.g., location) using `LabelEncoder`

## Model Building
A `RandomForestRegressor` is trained to predict house prices. The pipeline includes:
1. **Splitting the data** into training and test sets
2. **Scaling numerical features** using `StandardScaler`
3. **Hyperparameter tuning** using `RandomizedSearchCV`
4. **Model evaluation** using metrics such as `r2_score` and `mean_squared_error`

## Results
Linear Regression:
- Mean Absolute Error: 9.905989942241036e-16
- Mean Squared Error: 1.6672681834671116e-30
- R-squared: 1.0

Random Forest Regressor:
- Mean Absolute Error: 0.0018570826934125246
- Mean Squared Error: 0.00016093607081635268
- R-squared: 0.9986651059714101



