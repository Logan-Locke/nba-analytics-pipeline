# NBA Analytics Pipeline: Data Exploration and Predictive Modeling

This repository presents a comprehensive data science workflow applied to NBA per-game statistics.
It showcases practical techniques (data cleaning, visualization, statistical inference,
and predictive modeling) that reveal insights into player performance and age dynamics.
The notebooks serve as a hands-on guide for transforming raw sports data into informative results.

## Exploratory Data Analysis (`exploration.ipynb`)
* **Data Loading & Overview**: Connects to an SQLite database (`nba_stats.db`) and summarizes a table containing over **30,000 records across 32 attributes**.
* **Data Cleaning & Transformation**: Optimizes data types and resolves encoding issues in player names using regular expressions.
* **Granularity & Temporality Analysis**: Investigates cases such as players with multiple team entries per season (mid-season team changes) and addresses missing data (more statistics being recorded as the NBA developed).
* **Aggregation & Visualization**: Applies deduplication techniques to extract full-season statistics and generates visualizations to identify trends and insights.
    * Highlights seasonal trends in scoring (a peak around 1970 and gradual changes over decades).
    * Examines the rarity of players playing for multiple teams in one season.
    * Explores relationships among various statistical measures to uncover potential insights for further analysis.

## Inference Analysis (`inference.ipynb`)
* **Objective**: Investigates whether a player’s performance metrics can help infer their age using statistical hypothesis testing.
* **Hypothesis Testing**: Compares performance between extreme age groups using bootstrapping and t-tests.
* **Regression Analysis**: Develops a simple linear regression model to quantify how well points per game predict age, with model evaluation metrics ($R^2$) highlighting its limitations.
* **Key Insights**: Finds that while significant differences exist between age extremes, a single performance metric (PTS) offers limited predictive power.

## Prediction Workflow (`prediction.ipynb`)
* **Data Splitting**: Divides the dataset into training and test sets, where the target variable is age.
* **Model Exploration**: Assesses multiple modeling approaches including Linear Regression, Lasso Regression, Random Forest, and XGBoost to forecast player age from various performance metrics.
* **Model Tuning & Evaluation**: Uses hyperparameter tuning (via GridSearchCV and RandomizedSearchCV) and evaluates models using metrics such as MSE, MAE, and R-squared.
* **Interpretability**: Leverages feature importance, partial dependence plots, and SHAP analyses to identify which predictors most influence age predictions.
    * The predictors with the most influence were minutes played, free-throw percentage, the NBA season/year.
* **Key Observations**: Concludes that even the best models explain only about 20% of the variance in age, suggesting that additional features may be necessary to enhance predictive performance.

## Conclusion

This project illustrates the power of a structured data science workflow in uncovering insights from raw sports data.
The exploratory phase addressed data quality and aggregation challenges,
while the inference and predictive analyses revealed that individual game statistics have limited predictive power for player age.
Future enhancements may include integrating advanced performance metrics and additional contextual variables to further refine predictions and deepen our understanding of NBA player dynamics.

## Data Source

Basketball Reference: https://www.basketball-reference.com/
