#Dot product   
#The dot product is the operation that performs
#(weights × inputs) + bias in one mathematically correct step.
import numpy as np      
inputs = [1, 2, 3, 2.5]
weights =[ [0.2, 0.8, -0.5, 1.0],
[0.5, -0.91, 0.26, -0.5],[0.5, -0.91, 0.26, -0.5]]
bias = [2,3,0.5]

output=np.dot(weights,inputs)+bias
print(output)
                      
