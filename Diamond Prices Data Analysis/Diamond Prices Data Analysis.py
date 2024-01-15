import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

diamonds = pd.read_csv('diamonds.csv')

print(diamonds.head())
print(diamonds.info())
print(diamonds.describe())

diamonds = diamonds.dropna()

sns.scatterplot(x='carat', y='price', data=diamonds)
plt.title('Carat vs Price')
plt.show()

# Select only numeric columns for correlation analysis
numeric_columns = diamonds.select_dtypes(include=['number']).columns
correlation_matrix = diamonds[numeric_columns].corr()

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

X = diamonds[['carat', 'depth', 'table', 'x', 'y', 'z']]  # Exclude non-numeric columns
y = diamonds['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')
