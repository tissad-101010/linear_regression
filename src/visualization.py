# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    visualization.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tissad <tissad@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/05 16:24:11 by tissad            #+#    #+#              #
#    Updated: 2026/02/05 17:11:10 by tissad           ###   ########.fr        #
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