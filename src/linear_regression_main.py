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
from visualization import plot_data, save_plot,display_statistics,\
    plot_regression, plot_cost_history
from linear_regression import LinearRegression
from model_saver import save_model

import pandas as pd
import argparse

def main(args):
    # Load the data
    data_file = args.data_file if args.data_file else './data/data.csv'
    print("✓Loading data...")
    data = load_data(data_file)
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
    model = LinearRegression(learning_rate=0.03, tolerance=1e-6, n_iterations=1000)
    X = normalized_data['km'].values
    y = normalized_data['price'].values
    model.fit(X, y, data=data, norm_stat=norm_stat)
    print("✓Model fitted successfully.")


    # Visualize the regression line
    save_final_plot = input("\nDo you want to save the visualization of the final regression fit? (y/n): ").strip().lower() == 'y'
    if save_final_plot:
        plot_name = input("Enter the filename to save the regression plot (e.g., 'final_regression_fit.png'): ").strip()
        plot_name = 'final_regression_fit.png' if not plot_name else plot_name
        plt3 = plot_regression(data, model, norm_stat)
        save_plot(plt3, f'./plot/{plot_name}')
        plt3.close()
    
    # Visualize the cost history
    save_cost_plot = input("\nDo you want to save the visualization of the cost history? (y/n): ").strip().lower() == 'y'
    if save_cost_plot:
        save_cost_filename = input("Enter the filename to save the cost history plot (e.g., 'cost_history.png'): ").strip()
        save_cost_filename = 'cost_history.png' if not save_cost_filename else save_cost_filename
        plt4 = plot_cost_history(model.cost_history)
        save_plot(plt4, f'./plot/{save_cost_filename}')
        plt4.close()

    # Save the model parameters
    save_model_choice = input("\nDo you want to save the model parameters? (y/n): ").strip().lower() == 'y'
    if save_model_choice:
        model_filename = input("Enter the filename to save the model parameters (e.g., 'model_params.json'): ").strip()
        model_filename = 'model_params.json' if not model_filename else model_filename
        save_model(model, norm_stat, filename=f'./models/{model_filename}')

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Train a linear regression model on the car dataset.")
    parser.add_argument('--data_file', type=str, help='Path to the CSV file containing the dataset')
    args = parser.parse_args()
    main(args)
    