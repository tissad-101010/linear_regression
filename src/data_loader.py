# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    data_loader.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tissad <tissad@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/05 15:34:29 by tissad            #+#    #+#              #
#    Updated: 2026/02/05 15:43:32 by tissad           ###   ########.fr        #
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
    
# Example usage:
data = load_data('./data/data.csv')
#print the first few rows of the data if it was loaded successfully
if data is not None:
    print(data.head())