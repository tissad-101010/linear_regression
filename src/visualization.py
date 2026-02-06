# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    visualization.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tissad <tissad@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/05 16:24:11 by tissad            #+#    #+#              #
#    Updated: 2026/02/06 13:30:27 by tissad           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""
This module provides functions for visualizing data and model predictions using
matplotlib. It includes functions to plot the original data points and the
"""
import matplotlib.pyplot as plt
import numpy as np

def plot_data(data, title="data visualization (km vs price)"):
    """
    Function to visualize the data using a scatter plot.
    
    Args:
        data (pd.DataFrame): The DataFrame containing the data to be visualized.
        title (str): The title of the plot.
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(data['km'], data['price'], alpha=0.6, color='blue', edgecolors='black')
    plt.xlabel('Mileage (km)', fontsize=12)
    plt.ylabel('Price', fontsize=12)
    plt.title(title, fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    return plt



def save_plot(plt, filename):
    """
    Function to save the plot to a file.
    Args:
        plt: The matplotlib plot object to be saved.
        filename (str): The name of the file where the plot will be saved.
    returns:
        None
    """
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"✓ Plot saved as '{filename}'")


def plot_regression(data, model, stats, title="Linear Regression Fit (km vs price)"):
    """
    Function to visualize the data along with the fitted linear regression line.
    
    Args:
        data (pd.DataFrame): The DataFrame containing the data to be visualized.
        model: The fitted linear regression model with a predict method.
        stats (dict): Normalization statistics
        title (str): Title of the plot
    """
    plt.figure(figsize=(12, 7))
    
    #   Scatter plot of the original data points
    plt.scatter(data['km'], data['price'], alpha=0.6, color='blue', 
                label='original data', edgecolors='black', s=50)
    
    # Regression line
    km_range = np.linspace(data['km'].min(), data['km'].max(), 100)
    km_normalized = (km_range - stats['km_mean']) / stats['km_std']
    price_normalized = model.predict(km_normalized)
    price_range = price_normalized * stats['price_std'] + stats['price_mean']
    
    plt.plot(km_range, price_range, color='red', linewidth=2, 
             label='Regression line')
    
    plt.xlabel('Mileage (km)', fontsize=12)
    plt.ylabel('Price', fontsize=12)
    plt.title(title, fontsize=14, fontweight='bold')
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    return plt


def plot_cost_history(cost_history, title="Cost History During Training"):
    """
    Function to visualize the cost history during training.
    The cost illustrates how the model's error decreases over iterations,
    which can help in understanding the convergence 
    of the gradient descent algorithm.
    
    Args:
        cost_history (list): A list of cost function values recorded 
        at each iteration of training.
        title (str): Title of the plot
    """
    plt.figure(figsize=(10, 6))
    plt.plot(cost_history, color='green', linewidth=2)
    plt.xlabel('Iteration', fontsize=12)
    plt.ylabel('Cost (MSE)', fontsize=12)
    plt.title(title, fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    return plt


def display_statistics(stats):
    """
    Function to display the calculated statistics in a formatted manner.
    
    Args:
        stats (dict): A dictionary containing the calculated statistics 
        for the 'km' and 'price' columns.
    """
    print("\n" + "="*60)
    print("📊 STATISTICAL ANALYSIS".center(60))
    print("="*60)
    
    print("\n🚗 MILEAGE (KM):")
    print(f"  - Minimum:  {stats['km']['min']:>10.0f} km")
    print(f"  - Maximum:  {stats['km']['max']:>10.0f} km")
    print(f"  - Mean:  {stats['km']['mean']:>10.0f} km")
    print(f"  - median:  {stats['km']['median']:>10.0f} km")
    print(f"  - Standard Deviation: {stats['km']['std']:>8.0f} km")
    
    print("\n💰 PRICE:")
    print(f"  - Minimum:  {stats['price']['min']:>10.0f}")
    print(f"  - Maximum:  {stats['price']['max']:>10.0f}")
    print(f"  - Mean:  {stats['price']['mean']:>10.0f}")
    print(f"  - median:  {stats['price']['median']:>10.0f}")
    print(f"  - Standard Deviation: {stats['price']['std']:>8.0f}")
    print("="*60)