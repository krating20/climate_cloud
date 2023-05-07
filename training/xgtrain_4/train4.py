import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score

# Load the CSV files for years 2015-2019 and 2022

df_2010 = pd.read_csv('2010.csv')
df_2011 = pd.read_csv('2011.csv')
df_2012 = pd.read_csv('2012.csv')
df_2013 = pd.read_csv('2013.csv')
df_2014 = pd.read_csv('2014.csv')
df_2015 = pd.read_csv('2015.csv')
df_2016 = pd.read_csv('2016.csv')
df_2017 = pd.read_csv('2017.csv')
df_2018 = pd.read_csv('2018.csv')
df_2019 = pd.read_csv('2019.csv')
df_2022 = pd.read_csv('2022.csv')

# Concatenate the dataframes for training data
df_train = pd.concat([df_2010,df_2011,df_2012,df_2013,df_2014,df_2015, df_2016, df_2017, df_2018, df_2019])

# Extract features and target variable for training data
X_train = df_train[['lat', 'lon', 'apcp','air']].values
y_train = df_train['drought_catagory'].values

# Extract features for testing data
X_test = df_2022[['lat', 'lon', 'apcp','air']].values

# Convert time column to datetime and extract year, month, and day
df_train['time'] = pd.to_datetime(df_train['time'])
df_train['year'] = df_train['time'].dt.year
df_train['month'] = df_train['time'].dt.month
df_train['day'] = df_train['time'].dt.day

# Convert time column to datetime for testing data
df_2022['time'] = pd.to_datetime(df_2022['time'])

# Extract year, month, and day for testing data
df_2022['year'] = df_2022['time'].dt.year
df_2022['month'] = df_2022['time'].dt.month
df_2022['day'] = df_2022['time'].dt.day

# Train an XGBoost model
model = xgb.XGBClassifier(random_state=42)
model.fit(X_train, y_train)

# Make predictions on validation data
y_val_pred = model.predict(X_test)

# Add predictions to testing dataframe
df_2022['drought_catagory_pred'] = y_val_pred

# Save the testing dataframe with predictions to a CSV file
df_2022.to_csv('2022_predictions.csv', index=False)

# Calculate accuracy and F1 score on training data
y_train_pred = model.predict(X_train)
accuracy_train = accuracy_score(y_train, y_train_pred)
f1_train = f1_score(y_train, y_train_pred, average='weighted')
print(f'Training Accuracy: {accuracy_train:.2f}')
print(f'Training F1 Score: {f1_train:.2f}')


#Training Accuracy: 0.85
#Training F1 Score: 0.79