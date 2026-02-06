# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    precision_main.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tissad <tissad@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/06 14:46:27 by tissad            #+#    #+#              #
#    Updated: 2026/02/06 15:31:14 by tissad           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""
This module serves as the entry point for evaluating the precision of the linear regression model.
It loads the model parameters and normalization statistics from a JSON file,
"""

import pandas as pd
import numpy as np
from model_saver import load_model
from data_loader import load_data, normalize_data, get_statistics


def score(model, X, y):
    """
    Compute the R² score of the model on the given data.
    
    Args:
        X (np.array): Features
        y (np.array): true target values
        
    Returns:
        float: R² score
    """
    y_pred = model['theta0'] + model['theta1'] * X
    ss_res = np.sum((y - y_pred) ** 2) # Residual sum of squares
    ss_tot = np.sum((y - np.mean(y)) ** 2) # Total sum of squares
    r2 = 1 - (ss_res / ss_tot) # R² score calculation
    return r2

def main(args):
    """Main function to load the model and evaluate its precision."""
    
    # Load the model parameters
    print("\nLoading model parameters...")
    
    params = load_model(args.model_file) if args.model_file else load_model('./models/model_params.json')   
    if params is None:
        print("✗ Failed to load model parameters. Exiting.")
        return 1
    print("\n✓ Model parameters loaded successfully.")
    print(f"  - θ₀: {params['theta0']:.6e}")
    print(f"  - θ₁: {params['theta1']:.6e}")
    # Load the dataset
    print("\nLoading dataset...")
    data_file = args.data_file if args.data_file else './data/data.csv'
    data = load_data(data_file)
    if data is None:
        print("✗ Failed to load dataset. Exiting.")
        return 1
    print("✓ Dataset loaded successfully.")
    # Normalize the dataset
    print("\nNormalizing dataset...")
    normalized_data, norm_stat = normalize_data(data)
    print("✓ Dataset normalized successfully.")
    X = normalized_data['km'].values    
    y = normalized_data['price'].values
    # Evaluate the model's precision
    r2_score = score(params, X, y)
    print(f"\nModel R² score: {r2_score:.6f}")
    if r2_score > 0.8:
        print("  → Good Job! Excellent fit! 🎉")
    elif r2_score > 0.6:
        print("  → Not bad! Decent fit! 👍")
    else:
        print("  → Needs improvement! Poor fit! 😕")
    return 0

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Evaluate the precision of the linear regression model.")
    parser.add_argument('--model_file', type=str, help='Path to the model parameters JSON file')
    parser.add_argument('--data_file', type=str, help='Path to the CSV file containing the dataset')
    args = parser.parse_args()
    main(args)
    