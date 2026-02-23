GRADIENT DESCENT FROM SCRATCH

1. WHAT IS GRADIENT DESCENT?
  --> It is a first-order iterative algorithm for minimizing a differentiable multivariate function.
  --> In layman terms it is nothing but an algorithm that takes any mathematical function as input given it is differentiable at 0 and then returns it's global minima(Note: Given the function is convex). 
  --> The idea is to take repeated steps in the opposite direction of the gradient (or approximate gradient) of the function at the current point, because this is the direction of steepest descent. Conversely, stepping in the direction of the gradient will lead to a trajectory that maximizes that function; the procedure is then known as gradient ascent. 
  --> It is particularly useful in machine learning and artificial intelligence for minimizing the cost or loss function.

2. GRADIENT DESCENT TO OPTIMIZE LINEAR REGRESSION PARAMETERS
  --> The objective is to find the optimal model parameters that minimize prediction error.
   
  --> CASE 1 (SLR) : In SLR the model is defined as y = mx + b, where 'm' is coefficient and 'b' is intercept. So The goal is to find the optimal values of m and b that minimizes the Loss function (MSE/SSE)
  --> CASE 2 (MLR) : In MLR the model extends to multiple features and is defined as y = b + m1x1 + m2x2 + m3x3 + m4x4 + ....... + mnxn and the goal remains the same that is to find all of these coefficients and intercept values that will minimize the overall Loss function

3. ASSUMPTIONS AND DEMERITS OF LOSS FUNCTION
  --> Gradient Descent requires the loss function to be continous and differentiable
  --> Proper learning rate selection
  --> For guaranteed convergence to a global minima, the loss function should be 'Convex'. In case of Concave loss functions gradient descent may converge to a local minima or saddle points.
  --> Can get computationally expensive
  --> Gradient descent is very sensitive to Learning rate selected.
  --> Gradient descent assumes features are scaled properly.

4. THE GOAL OF THIS 'Gradient Descent' FOLDER IN THIS REPOSITORY IS:
   --> How Gradient Descent works internally
   --> How coefficients are updated mathematically
   --> How optimization behaves in both Simple and Multiple Linear Regression

5. ADDITIONAL LEARNING RESOURCES
   --> PDF containing detailed handwritten notes on Gradient Descent.
   --> difference between Convex v/s Concave function
   --> Gifs showing how Gradient Descent will take steps
    
