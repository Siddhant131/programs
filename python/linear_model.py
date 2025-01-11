import numpy as np
import matplotlib.pyplot as plt
x_train=np.array([1.0,2.0])
y_train=np.array([300.0,500.0])
print(f"x_train = {x_train}")
print(f"y_train = {y_train}")
m=x_train.shape[0]
print(f"number of training examples are {m}")
w=200
b=100
def compute_model_output(x, w, b):
    m = x.shape[0]
    f_wb = np.zeros(m)
    for i in range(m):
        f_wb[i] = w * x[i] + b
        
    return f_wb
tmp_f_wb = compute_model_output(x_train, w, b,)

# Plot our model prediction
plt.plot(x_train, tmp_f_wb, c='b',label='Our Prediction')

# Plot the data points
plt.scatter(x_train, y_train, marker='x', c='r',label='Actual Values')

# Set the title
plt.title("Housing Prices")
# Set the y-axis label
plt.ylabel('Price (in 1000s of dollars)')
# Set the x-axis label
plt.xlabel('Size (1000 sqft)')
plt.legend()
plt.show()