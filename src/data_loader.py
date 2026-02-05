# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    data_loader.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tissad <tissad@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/05 15:34:29 by tissad            #+#    #+#              #
#    Updated: 2026/02/05 17:24:50 by tissad           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


"""
This module provides a function to load data from a CSV file into a 
pandas DataFrame. It includes error handling to manage cases where 
the file is not found or other exceptions occur during loading.
"""
import pandas as pd

def load_data(filepath):
    """
    Function to load data from a CSV file into a pandas DataFrame.
    Args:
        filepath (str): The path to the CSV file to be loaded.
        
    Returns:
        pd.DataFrame: A DataFrame containing the loaded data, 
        or None if an error occurs.
    """
    try:
        data = pd.read_csv(filepath)
        print(f"✓Length of data: {len(data)}")
        return data
    except FileNotFoundError:
        print(f"✗ Error: File '{filepath}' not found.")
        return None
    except Exception as e:
        print(f"✗ Error loading data: {e}")
        return None
    


#mormalize the data
def normalize_data(data):
    """
    Function to normalize the data using  z-score normalization.
    Args:
        data (pd.DataFrame): The DataFrame containing the data to be normalized.
        
    Returns:
        Tuple: (normalized_data, stats) where normalized_data is a DataFrame with normalized values,
        and stats is a dictionary containing the mean and standard deviation for each column.        
    """
    
    km_mean = data['km'].mean()
    km_std = data['km'].std()
    price_mean = data['price'].mean()
    price_std = data['price'].std()
    
    normalized_data = data.copy()
    normalized_data['km'] = (data['km'] - km_mean) / km_std
    normalized_data['price'] = (data['price'] - price_mean) / price_std
    
    stats = {
        'km_mean': km_mean,
        'km_std': km_std,
        'price_mean': price_mean,
        'price_std': price_std
    }
    
    print(f"✓Data normalization complete.")
    print(f"  - KM: μ={km_mean:.0f}, σ={km_std:.0f}")
    print(f"  - Prix: μ={price_mean:.0f}, σ={price_std:.0f}")
    
    return normalized_data, stats

    