import numpy as np
import pandas as pd

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def log_likelihood(y_true, y_pred):
    return np.sum(y_true * np.log(y_predicted) + (1 - y_true) * np.log(1 - y_predicted))

def update_rule(w, alpha, y_true, x):
    y_pred = sigmoid(np.dot(x, weights))
    gradient = np.dot(x.T, (y_true - y_predicted)) #need transpose
    w += alpha * gradient
    return weights
    
def classify(x, w):
    if sigmoid(np.dot(x, w)) >= 0.5:
        return 1
    else:
        return 0

def learning(x, y_true):
    alpha = 0.1
    epochs = 1000
    w = np.zeros(x.shape[1])
    for _ in range(epochs):
        w = update_rule(w, alpha, y_true, x)
    return w

data = pd.read_csv('diabetes.csv')
X = data[[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]]
y = data['Outcome']
X = X.values
y = y.values

def train_test_splitl(X, y):
    indices = np.arange(X.shape[0])
    np.random.shuffle(indices)
    test_set_size = int(len(X) * test_size)
    test_indices = indices[:test_set_size]
    train_indices = indices[test_set_size:]
    return X[train_indices], X[test_indices], y[train_indices], y[test_indices]

X_train, X_test, y_train, y_test = train_test_split(X, y)

w = learning(X_train, y_train)
print(w)

def accuracy(X, y, weights):
    predictions = np.array([classify(x, weights) for x in X])
    return np.mean(predictions == y)

test_accuracy = accuracy(X_test, y_test, weights)
print(test_accuracy)

