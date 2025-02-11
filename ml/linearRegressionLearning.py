
import csv
import os

def load_dataset(filename):
    if not os.path.isfile(filename):
        print(f"File {filename} does not exist.")
        return []
    dataset = []
    with open(filename, newline='') as csvfile:
        
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            
            x = [float(value) for value in row[:-1]]  
            y = float(row[-1]) 
            dataset.append((x, y))
    return dataset

dataset = load_dataset('tvmarketing.csv')

import math
import random


def is_linear_relationship(dataset):
    n = len(dataset)
    num_features = len(dataset[0][0])
    sums_x = [0] * num_features
    sums_y = 0
    for x, y in dataset:
        for i in range(num_features):
            sums_x[i] += x[i]
        sums_y += y

    mean_x = [sums_x[i] / n for i in range(num_features)]
    mean_y = sums_y / n
    numerator = [0] * num_features
    sum_dev_x_squared = [0] * num_features
    sum_dev_y_squared = 0
    for x, y in dataset:
        for i in range(num_features):
            numerator[i] += (x[i] - mean_x[i]) * (y - mean_y)
            sum_dev_x_squared[i] += (x[i] - mean_x[i]) ** 2
        sum_dev_y_squared += (y - mean_y) ** 2

    pearson = [numerator[i] / math.sqrt(sum_dev_x_squared[i] * sum_dev_y_squared) for i in range(num_features)]
    print("Pearson correlation coefficients:", pearson)
    return all(abs(p) >= 0.75 for p in pearson)

def linear_regression_learning(dataset, question_x):
    n = len(dataset)
    num_features = len(dataset[0][0])
    test = dataset[:n//10]
    train = dataset[n//10:]
    N = len(train)
    b = [random.random() for _ in range(num_features)]
    b0 = random.random()
    
    alpha = 0.001
    def error(b0, b, train):
        y_deviation = [0] * num_features
        summation = 0 #for error
        only_y_deviation = 0
        for x, y in train:
            predicted_y = b0 + sum(b[i] * x[i] for i in range(num_features))
            summation += (predicted_y - y) ** 2
            only_y_deviation += (predicted_y - y)
            for i in range(num_features):
                y_deviation[i] += (predicted_y - y) * x[i]
        return (only_y_deviation, y_deviation, summation / (2 * N))

    only_y_deviation, y_deviation, E = error(b0, b, train)
    epoch = 1
    print("error after assumption and b0, b", E, b0, b)

    while E > 1:
        b0 = b0 - alpha * only_y_deviation / N
        for i in range(num_features):
            b[i] = b[i] - alpha * y_deviation[i] / N
        only_y_deviation, y_deviation, E = error(b0, b, train)
        print(f"After epoch {epoch}, error was {E} and b0, b were {b0}, {b}")
        epoch += 1

    def accuracy(test, b0, b):
        correct = 0
        total = 0
        if len(test) == 0:
            return 1.0
        for x, y in test:
            predicted_y = b0 + sum(b[i] * x[i] for i in range(num_features))
            if round(y) == round(predicted_y):
                correct += 1
            total += 1
        return correct / total

    a = accuracy(test, b0, b)
    print("Accuracy is", a)
    ans = b0 + sum(b[i] * question_x[i] for i in range(num_features))
    return ans

#dataset = [([1, 1], 1), ([2, 2], 2), ([3, 3], 3), ([4, 4], 4), ([5, 5], 5), ([7, 7], 7)]
print("Is linear relationship?", is_linear_relationship(dataset))
print("Learning method:\n", linear_regression_learning(dataset, [1]))
