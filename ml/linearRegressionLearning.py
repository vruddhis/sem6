

import csv
import os
import math
import random

def load_dataset(filename):
    if not os.path.isfile(filename):
        print(f"Error: File '{filename}' not found.") 
        return []

    dataset = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)

        for row in reader:
            try:
                x = [float(row[0])]
                y = float(row[1])
                dataset.append((x, y))
            except ValueError:
                print(f"Warning: Skipping row with invalid data: {row}")  
                continue  
            except IndexError: 
                print(f"Warning: Skipping row with missing data: {row}")
                continue

    if not dataset:  
        print(f"Warning: No valid data found in '{filename}'.")  

    return dataset

def is_linear_relationship(dataset):
    n = len(dataset)
    print(n)
    num_features = len(dataset[0][0])
    correlation_coefficients = []

    for j in range(num_features):  
        sum_x = 0
        sum_y = 0
        sum_xy = 0
        sum_x_squared = 0
        sum_y_squared = 0

        for x, y in dataset:
            sum_x += x[j]
            sum_y += y
            sum_xy += x[j] * y
            sum_x_squared += x[j] ** 2
            sum_y_squared += y ** 2

        numerator = n * sum_xy - sum_x * sum_y
        denominator = math.sqrt((n * sum_x_squared - sum_x**2) * (n * sum_y_squared - sum_y**2))

        if denominator == 0: 
            correlation = 0  
        else:
            correlation = numerator / denominator
        correlation_coefficients.append(correlation)

    print("Pearson correlation coefficients:", correlation_coefficients)
    return all(abs(p) >= 0.75 for p in correlation_coefficients)


def linear_regression_learning(dataset, question_x):
    n = len(dataset)
    num_features = len(dataset[0][0])
    test = dataset[:n // 10]
    train = dataset[n // 10:]
    mean_x = [0] * num_features
    std_x = [0] * num_features
    for i in range(num_features):
        feature_values = [x[i] for x, _ in train]
        mean_x[i] = sum(feature_values) / len(feature_values)
        std_x[i] = math.sqrt(sum((val - mean_x[i])**2 for val in feature_values) / len(feature_values))
    
    def scale_data(data, mean, std):
      scaled_data = []
      for x, y in data:
        scaled_x = [(x[i] - mean[i]) / std[i] if std[i] != 0 else 0 for i in range(num_features)]
        scaled_data.append((scaled_x, y))
      return scaled_data

    train_scaled = scale_data(train, mean_x, std_x)
    test_scaled = scale_data(test, mean_x, std_x)
    question_x_scaled = [(question_x[i] - mean_x[i]) / std_x[i] if std_x[i] != 0 else 0 for i in range(num_features)]

    b = [random.random() for _ in range(num_features)]
    b0 = random.random()
    alpha = 0.01
    epochs = 1000
    tolerance = 0.001

    def error(b0, b, data):
        error_sum = 0
        for x, y in data:
            y_pred = b0 + sum(b[i] * x[i] for i in range(num_features))
            error_sum += (y_pred - y)**2
        return error_sum / len(data)

    prev_error = float('inf')
    for epoch in range(epochs):
        db = [0] * num_features
        db0 = 0
        for x, y in train_scaled:
            y_pred = b0 + sum(b[i] * x[i] for i in range(num_features))
            diff = y - y_pred
            for i in range(num_features):
                db[i] -= 2 * diff * x[i] / len(train_scaled)
            db0 -= 2 * diff / len(train_scaled)

        for i in range(num_features):
            b[i] -= alpha * db[i]
        b0 -= alpha * db0
        current_error = error(b0, b, train_scaled)

        if abs(prev_error - current_error) < tolerance:
            print("Converged!")
            break
        prev_error = current_error
        print(f"Epoch {epoch+1}, error: {current_error}")

    test_error = error(b0, b, test_scaled)
    print("Test error:", test_error)

    ans = b0 + sum(b[i] * question_x_scaled[i] for i in range(num_features))
    return ans

dataset = load_dataset('Salary_Data.csv')
print("Is linear relationship?", is_linear_relationship(dataset))
years_experience = 4
predicted_salary = linear_regression_learning(dataset, [years_experience]) 

print(f"Predicted salary for {years_experience} years of experience: {predicted_salary}")