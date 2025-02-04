#dataset is list with elements of form (x, y)
""" y = b0 + b1x1 y is estimated or predicted value
b0 = ( sum(y) * sum(x**2) - sum(x)sum(xy))/(n*sum(x**2) - sum(x)**2)
b1 = (n*sum(xy) - sum(x)sum(y))/(n*sum(x**2) - sum(x)**2)"""

def linear_regression_statistical(dataset, question_x):
    sum_y = 0
    sum_x_squared = 0
    sum_x = 0
    sum_y_x = 0
    n = 0
    for (x,y) in dataset:
        sum_x += x
        sum_y += y
        sum_x_squared += x * x
        sum_y_x += x * y
        n += 1
    b0 = (sum_y * sum_x_squared - sum_x * sum_y_x) / (n * sum_x_squared - sum_x * sum_x)
    b1 = (n * sum_y_x - sum_x * sum_y)/(n * sum_x_squared - sum_x * sum_x)
    ans = b0 + b1 * question_x
    print("b0 and b1 in statistical are", b0, b1)
    return ans

"""COV(X,Y)=E([X-E(X)][Y-E(Y)])=E(XY)-E(X)E(Y)
pearson coeff = covariance/ standard_dev(x) standard_dev(y)
find deviation from mean, square, avg. sqrt it to get standard deviation
"""
import math

def is_linear_relationship(dataset):
    sum_y = 0
    
    sum_x = 0
    
    n = 0
    for (x,y) in dataset:
        x = float(x)
        y = float(y)
        sum_x += x
        sum_y += y
        n += (1)
    mean_x = sum_x / n
    mean_y = sum_y / n
    numerator = 0
    sum_dev_x_squared = 0
    sum_dev_y_squared = 0
    for (x, y) in dataset:
        x = float(x)
        y = float(y)
        numerator += (x - mean_x) * (y - mean_y)
        sum_dev_x_squared += (x ** 2 - mean_x**2)
        sum_dev_y_squared += (y**2 - mean_y**2)
    pearson = numerator / math.sqrt(sum_dev_x_squared * sum_dev_y_squared)
    print(pearson)
    if abs(pearson) >= 0.75:
        return True
    return False


    
    
""" for learning way: update rule: w_j = w_j - alpha * [1/N * sum(y_hat - y_i) * x_i]
do train test split too"""   

def linear_regression_learning(dataset, question_x):
    n = len(dataset)
    test = dataset[:n//10 + 1]
    train = dataset[n//10 + 1:]
    N = len(train)
    
    b0 = 1
    b1 = 1
    alpha = 0.1
    def error(b0, b1, train):
        summation = 0
        N = 0
        y_deviation_x = 0
        for (x, y) in train:
            N += 1
            predicted_y = b0 + b1 * x
            summation += (predicted_y - y) ** 2
            y_deviation_x += (predicted_y - y) * x
        return (y_deviation_x, summation / (2 * N))
    y_deviation_x, E = error(b0, b1, train)
    epoch = 1
    print("error after assumption and b0, b1", E, b0, b1)
    while E > 0.1:
        
        b0 = b0 - alpha * ((1/N) * y_deviation_x)
        b1 = b1 - alpha * ((1/N) * y_deviation_x)
        y_deviation_x, E = error(b0, b1, train)
        print("After epoch ", epoch, " error was ", E, " and b0 and b1 were ", b0, b1)
        epoch += 1
        
    def accuracy(test, b0, b1):
        correct = 0
        total = 0
        n = 0
        for (x, y) in dataset:
            n += 1
            predicted_y = b0 + b1 * x
            if y == predicted_y:
                correct += 1
            total += 1
       
        return (correct) / total
    
    a = accuracy(test, b0, b1)
    print("Accuracy is ", a)
    ans = b0 + b1 * question_x
    return ans

#dataset = [(43, 99), (21, 65), (25, 79), (42, 75), (57, 87), (59, 81)]
dataset = [(1,1), (2,2), (3,3), (4,4), (5,7), (6, 4)]
print("Is linear relationship?", is_linear_relationship(dataset))
print("Statistical method", linear_regression_statistical(dataset, 55))
print("Learning method:\n"(linear_regression_learning(dataset, 55)))
