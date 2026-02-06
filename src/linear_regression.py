# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    linear_regression.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tissad <tissad@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/05 18:04:09 by tissad            #+#    #+#              #
#    Updated: 2026/02/06 15:00:46 by tissad           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""
This module implements a simple linear regression model using gradient descent.
It includes functions to compute the cost function, perform gradient descent, and
make predictions based on the learned parameters. 
The model is designed to work with normalized data.
"""
import numpy as np
import matplotlib.pyplot as plt
from visualization import plot_regression

class LinearRegression:
    """
    A simple linear regression model that uses gradient descent to learn the parameters.
    
    Arguments:
    learning_rate (float): The step size for updating the parameters during gradient descent.
    tolerance (float): The threshold for convergence. If the change in cost function is less than this value, the algorithm will stop.
    n_iterations (int): The maximum number of iterations for gradient descent.

    Attributes:
    learning_rate (float): The step size for updating the parameters during gradient descent.
    tolerance (float): The threshold for convergence. If the change in cost function is less than this value, the algorithm will stop.
    n_iterations (int): The maximum number of iterations for gradient descent.
    theta0 (float): The intercept term of the linear model.
    theta1 (float): The slope term of the linear model.
    cost_history (list): A list to store the cost function values at each iteration for analysis.
    """
    def __init__(self, learning_rate=0.01, tolerance=1e-6, n_iterations=1000):
        self.learning_rate = learning_rate
        self.tolerance = tolerance # tolerance for convergence
        self.n_iterations = n_iterations
        self.theta0 = 0.0  # Intercept
        self.theta1 = 0.0  # Slope
        self.cost_history = []  # To store cost function values during training
    def compute_cost(self, errors, m):
        """
        Compute the cost function for linear regression.
        
        Arguments:
        X (numpy array): The input feature values (normalized).
        y (numpy array): The target values (normalized).
        
        Returns:
        float: The computed cost value.
        """
        # Compute the cost using the mean squared error formula
        return (1/(m)) * np.sum(errors ** 2)
        
    
        
    
    def gradient_descent(self, X, y, plot_interval=10, plot_fit=False, data=None, norm_stat=None):
        """
        Perform gradient descent to learn the parameters theta0 and theta1.
        
        Arguments:
        X (numpy array): The input feature values (normalized).
        y (numpy array): The target values (normalized).
        """
        m = len(y)
        for iteration in range(self.n_iterations):
            # Calculate the predicted values based on current parameters
            predictions = self.theta0 + self.theta1 * X
            # Calculate the errors between predictions and actual target values
            errors = predictions - y
            
            # Compute the gradients for theta0 and theta1
            d_theta0 = (1/m) * np.sum(errors)
            d_theta1 = (1/m) * np.sum(errors * X)
            
            # Update the parameters using the computed gradients and learning rate
            self.theta0 -= self.learning_rate * d_theta0
            self.theta1 -= self.learning_rate * d_theta1
            
            # Compute the cost function value after updating parameters
            cost = self.compute_cost(errors, m)
            self.cost_history.append(cost) # Store cost for analysis
            
            if iteration % plot_interval == 0 or iteration == self.n_iterations - 1:
                print(f"Iteration {iteration}: Cost = {cost:.6f}, theta0 = {self.theta0:.4e}, theta1 = {self.theta1:.4f}")
                # Optionally, plot the fit at certain iterations to visualize convergence
                if data is not None and norm_stat is not None and plot_fit:
                    plt = plot_regression(data, self, norm_stat, title=f"Iteration {iteration} Fit")
                    plt.show(block=False)  # Non-blocking show to allow the loop to continue
                    plt.pause(3)           # Pause to display the plot for a short time
                    plt.close()            # Close the plot to avoid too many open windows during training
            
            # Check for convergence by comparing the change in cost function value
            if iteration > 0 and abs(self.cost_history[-2] - cost) < self.tolerance:
                print(f"✓ Convergence reached at iteration {iteration}.")
                break

    def fit(self, X, y, data=None, norm_stat=None):
        """
        Fit the linear regression model to the training data.
        
        Arguments:
        X (numpy array): The input feature values (normalized).
        y (numpy array): The target values (normalized).
        """
        plot_fit = input("Do you want to visualize the fit during training? (y/n): ").strip().lower() == 'y'
        print("✓Starting gradient descent...")
        self.gradient_descent(X, y, plot_fit=plot_fit, data=data, norm_stat=norm_stat)
        print(f"First cost: {self.cost_history[0]:.6f}  ")
        print(f"Final cost: {self.cost_history[-1]:.6f}")
        print(f"✓Learned parameters: theta0 = {self.theta0:.4e}, theta1 = {self.theta1:.4f}")  
        
    def predict(self, X):
        """
        Make predictions using the learned linear regression model.
        
        Arguments:
        X (numpy array): The input feature values (normalized) for which to make predictions.
        
        Returns:
        numpy array: The predicted target values based on the input features.
        """
        return self.theta0 + self.theta1 * X
    
