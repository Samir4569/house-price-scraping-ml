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
- **Encoding categorical features** (e.g., location) using `LabelEncoder`

## Feature Engineering
To improve the predictive power of the model, the following new features are created:
- **`price_per_sqm`**: Price per square meter
- **`room_area_ratio`**: Ratio of room count to total area
- **`floor_ratio`**: Current floor divided by maximum floor
- **Log transformation** applied to reduce skewness in price and area

## Model Building
A `RandomForestRegressor` is trained to predict house prices. The pipeline includes:
1. **Splitting the data** into training and test sets
2. **Scaling numerical features** using `StandardScaler`
3. **Hyperparameter tuning** using `RandomizedSearchCV`
4. **Model evaluation** using metrics such as `r2_score` and `mean_squared_error`

## Results
The model is evaluated based on:
- **Correlation analysis**: Identifying the strongest predictors of price
- **Skewness analysis**: Transforming features to improve model stability
- **Boxplots**: Identifying and handling outliers

## Future Improvements
- Expanding the dataset with more listings
- Experimenting with other regression models (e.g., XGBoost, LightGBM)
- Incorporating additional features such as neighborhood crime rates and infrastructure quality


## Usage
1. Run `scrapy.py` to scrape house listings.
2. Process and analyze the dataset in `houseprice_prediction.ipynb`.
3. Train the model and evaluate its performance.


