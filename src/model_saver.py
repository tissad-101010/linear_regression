# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    model_saver.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tissad <tissad@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/06 13:42:35 by tissad            #+#    #+#              #
#    Updated: 2026/02/06 14:03:21 by tissad           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #



"""
This module provides functions to save and load the parameters of a linear 
regression model.
It uses JSON format for saving the model parameters and normalization 
statistics,
"""

import json

def save_model(model, stats, filename='model_params.json'):
    """
    save the model parameters and normalization statistics to a JSON file
    
    Args:
        model: The linear regression model object containing the parameters to be saved.
        stats (dict): A dictionary containing the normalization statistics (mean and std for km and price).
        filename (str): The name of the file where the model parameters will be saved.
    """
    params = {
        'theta0': model.theta0,
        'theta1': model.theta1,
        'km_mean': stats['km_mean'],
        'km_std': stats['km_std'],
        'price_mean': stats['price_mean'],
        'price_std': stats['price_std']
    }
    
    with open(filename, 'w') as f:
        json.dump(params, f, indent=4)
    
    print(f"✓ Model saved: {filename}")


def load_model(filename='model_params.json'):
    """
    Load the model parameters
    
    Args:
        filename (str): The name of the file from which the model parameters will be loaded.
        
    Returns:
        dict: The model parameters and normalization statistics, or None if the file is not found.
    """
    try:
        with open(filename, 'r') as f:
            params = json.load(f)
        print(f"✓ Model loaded: {filename}")
        return params
    except FileNotFoundError:
        print(f"✗ File '{filename}' not found")
        return None
    

def predict_price(km, params):
    """
    Prédit le prix pour un kilométrage donné
    
    Args:
        km (float): Kilométrage
        params (dict): Paramètres du modèle
        
    Returns:
        float: Prix prédit
    """
    # Normalisation
    km_norm = (km - params['km_mean']) / params['km_std']
    
    # Prédiction normalisée
    price_norm = params['theta0'] + params['theta1'] * km_norm
    
    # Dénormalisation
    price = price_norm * params['price_std'] + params['price_mean']
    
    return price
