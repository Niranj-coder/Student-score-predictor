# student_predictor.py
from sklearn.linear_model import LinearRegression

# Hours studied vs marks scored
X = [[1], [2], [3], [4], [5]]
y = [35, 50, 65, 75, 85]

# Train the model
model = LinearRegression()
model.fit(X, y)

# Predict score for 6 hours of study
prediction = model.predict([[6]])
print(f"Predicted score: {prediction[0]:.2f}")