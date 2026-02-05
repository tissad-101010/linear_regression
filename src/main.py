# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tissad <issad@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/05 16:27:33 by tissad            #+#    #+#              #
#    Updated: 2026/02/05 23:59:19 by tissad            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""
Docstring pour main
"""

from data_loader import load_data, normalize_data, get_statistics
from visualization import plot_data, save_plot,display_statistics,plot_regression
from linear_regression import LinearRegression

import pandas as pd

def main():
    # Load the data
    print("✓Loading data...")
    data = load_data('./data/data.csv')
    if data is None:
        print("✗ Failed to load data. Exiting.")
        return 1
    
    print("✓Data loaded successfully.")
    # statistics analysis
    print("\n✓Performing statistical analysis...")
    print("-" * 60)
    stats_desc = get_statistics(data)
    display_statistics(stats_desc)
    # Data visualization
    print("\nData Visualization")
    print("-" * 60)
    plt1 = plot_data(data)
    save_plot(plt1, './plot/original_data_plot.png')
    plt1.close()
    # Normalize the data
    print("\n✓Normalizing data...")
    normalized_data, norm_stat = normalize_data(data)
    print("✓Data normalized successfully.")
    plt2 = plot_data(normalized_data)
    save_plot(plt2, './plot/normalized_data_plot.png')
    plt2.close()
    # Fit the linear regression model
    print("\n✓Fitting linear regression model...")
    print("-" * 60)
    model = LinearRegression(learning_rate=0.05, tolerance=1e-6, n_iterations=1000)
    X = normalized_data['km'].values
    y = normalized_data['price'].values
    model.fit(X, y, data=data, norm_stat=norm_stat)
    print("✓Model fitted successfully.")
    # Visualize the regression line
    save_final_plot = input("\nDo you want to visualize the final regression fit? (y/n): ").strip().lower() == 'y'
    if save_final_plot:
        plt3 = plot_regression(data, model, norm_stat)
        save_plot(plt3, './plot/regression_fit_plot.png')
        plt3.close()
    
if __name__ == "__main__":
    main()
    