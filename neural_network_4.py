#The more the data(batch) given to the neural network the easier it is for it to reach the output layer
#More batches = Better Prediction
# So we will be increasing the batch this time
#Increasing inputs does not affect the lawyer composition cause lawyers only consists of weights and biases
import numpy as np      
inputs = [[1, 2, 3, 2.5],
        [2,5,-1,2],
        [-1.5,2.7,3.3,-0.8] ]
weights =[ [0.2, 0.8, -0.5, 1.0],
[0.5, -0.91, 0.26, -0.5],[0.5, -0.91, 0.26, -0.5]]
bias = [2,3,0.5]

output=np.dot(weights,inputs)+bias
print(output)
