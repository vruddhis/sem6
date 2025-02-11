
import matplotlib.pyplot as plt
import math

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
    b1 = (n * sum_y_x - sum_x * sum_y) / (n * sum_x_squared - sum_x * sum_x)
    ans = b0 + b1 * question_x
    print("b0 and b1 in statistical are", b0, b1)
    return ans, b0, b1  # Return b0 and b1

def is_linear_relationship(dataset):
    sum_y = 0
    sum_x = 0
    n = 0
    for (x, y) in dataset:
        x = float(x)
        y = float(y)
        sum_x += x
        sum_y += y
        n += 1
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
    print("Pearson Correlation Coefficient:", pearson)
    if abs(pearson) >= 0.75:
        return True
    return False


dataset = [(1,1), (2,2), (3,3), (4,4), (5,7), (6, 4)]
print("Is linear relationship?", is_linear_relationship(dataset))
prediction, b0, b1 = linear_regression_statistical(dataset, 5) # Get b0 and b1
print("Statistical method prediction:", prediction)


x_values = [x for x, y in dataset]
y_values = [y for x, y in dataset]

plt.scatter(x_values, y_values, label="Data Points")

x_line = [min(x_values), max(x_values)] 
y_line = [b0 + b1 * x for x in x_line]

plt.plot(x_line, y_line, color='red', label="Regression Line")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear Regression")
plt.legend()
plt.grid(True)
plt.show()