# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    data_loader.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: issad <issad@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/05 15:34:29 by tissad            #+#    #+#              #
#    Updated: 2026/02/06 00:42:52 by issad            ###   ########.fr        #
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
    


#normalize the data
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

def get_statistics(data):
    """
    Function to calculate basic statistics (min, max, mean, median, std)
      for the 'km' and 'price' columns.
    
    Args:
        data (pd.DataFrame): The DataFrame containing the data for which 
        statistics are to be calculated.
        
    Returns:
        dict: Calculated statistics
    """
    stats = {
        'km': {
            'min': data['km'].min(),
            'max': data['km'].max(),
            'mean': data['km'].mean(),
            'median': data['km'].median(),
            'std': data['km'].std()
        },
        'price': {
            'min': data['price'].min(),
            'max': data['price'].max(),
            'mean': data['price'].mean(),
            'median': data['price'].median(),
            'std': data['price'].std()
        }
    }
    
    return stats
