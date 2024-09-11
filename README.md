# 🚖 NY Taxi Tip Prediction Project 🚖

### 🎯 Objective
The objective of this project is to build a regression model to predict the tip amount for taxi rides in New York City using a dataset from the seaborn library. The project involves data cleaning, visualization, and applying a Random Forest model to achieve high accuracy in predictions.

### 🛠️ Functionality
This project performs the following steps:

- 📥 **Import Data**: Load the NY taxi dataset from seaborn.
- 📊 **Descriptive Statistics**: Generate statistical summaries to understand the data.
- 🧹 **Data Cleaning**: Fill missing values with the mode for categorical columns, check for duplicates, and select relevant columns for analysis.
- 📈 **Data Visualization**: Use seaborn and matplotlib to create visualizations that explore relationships between features.
- 🌲 **Model Training**: Apply a Random Forest classifier to predict the tip amount.
- 📉 **Evaluation**: Assess the model’s performance and present the results.
- 📝 **Manual Testing**: Test the model with manually inputted data.
- 🌐 **Streamlit App**: A Streamlit app has been created to allow users to test the model interactively.

### 🛠️ Tools Used
- 🐍 **Python**: Programming language used for data analysis and model building.
- 📊 **pandas**: Library for data manipulation and analysis.
- 📈 **seaborn**: Library for data visualization.
- 📉 **matplotlib**: Library for creating static, animated, and interactive visualizations.
- 🤖 **scikit-learn**: Library for machine learning, used to implement the Random Forest classifier.
- 📓 **Jupyter Notebooks**: An interactive computing environment that allows you to create and share documents containing live code, equations, visualizations, and narrative text.
- 🌐 **Streamlit**: Framework used to create the web app for testing the model.

### 🛠️ Development Process
- 📥 **Data Import**: The NY taxi dataset is imported from the seaborn library.
- 📊 **Descriptive Statistics**: Descriptive statistics are generated to understand the distribution and central tendencies of the features.
- 🧹 **Data Cleaning**: Missing values are handled by filling them with the mode for categorical columns. Duplicates are checked and removed, and relevant columns are selected for further analysis.
- 📈 **Data Visualization**: Various visualizations are created using seaborn and matplotlib to explore the data. This includes:
  - 📉 **Distribution of the Tip**: This plot shows the distribution of tip amounts.
  - 📊 **Tip vs. Distance**: This plot illustrates the relationship between tip amount and distance traveled.
  - 📈 **Tip vs. Total Fare**: This plot shows the relationship between tip amount and total fare.
  - 💳 **Tip by Payment Method**: This plot displays the distribution of tips based on different payment methods.
  - ⏱️ **Tip vs. Trip Duration**: This plot shows the relationship between tip amount and trip duration.
  - 👥 **Tip by Number of Passengers**: This plot illustrates the distribution of tips based on the number of passengers.
- 🌲 **Model Training**: A Random Forest classifier is applied to predict the tip amount. The process involves:
  - Splitting the data into training and testing sets.
  - Training the model on the training data.
  - Evaluating the model on the test data.
- 🌐 **Streamlit App**: A Streamlit app is created to allow users to interactively test the model with their own inputs.

### 📉 Results
The performance of the RandomForest model has been evaluated using various error metrics and the coefficient of determination. The results obtained are as follows:

- **Mean Absolute Error (MAE)**: Provides an average measure of the absolute errors between the predictions and the actual values.
- **Mean Squared Error (MSE)**: Calculates the average of the squared errors, which penalizes larger errors more.
- **Root Mean Squared Error (RMSE)**: Is the square root of the MSE, providing a measure in the same units as the original data.
- **Coefficient of Determination (R²)**: Indicates the proportion of the variance in the dependent data that is predictable from the independent variables.

Additionally, several charts were created to evaluate the results:

- **Scatter Plot of Predictions vs. Actual Values**: This chart shows how the model’s predictions compare with the actual values. The red line represents the ideal case where the predictions are exactly equal to the actual values.
- **Residuals Plot**: This chart shows the distribution of residuals (prediction errors). A good model should have residuals approximately normally distributed around zero.
- **Feature Importance**: This chart shows the relative importance of each feature in the Random Forest model. Features with higher importance have a greater impact on the model’s predictions.

### 📝 Manual Testing
The model is tested with manually inputted data to verify its predictions.

### 🏆 Results
The Random Forest classifier achieved excellent results in predicting the tip amounts for NY taxi rides. The model’s accuracy was high, and the visualizations provided clear insights into the relationships between features and tip amounts.

### 🌐 Streamlit App
A Streamlit app has been created to allow users to test the model interactively. Users can input their own data to see the predicted tip amounts and explore the model's performance.

### 📧 Contact
For any questions or further information, please contact me at: jotaduranbon@gmail.com
