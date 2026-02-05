# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tissad <tissad@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/05 16:27:33 by tissad            #+#    #+#              #
#    Updated: 2026/02/05 17:01:39 by tissad           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""
Docstring pour main
"""

from data_loader import load_data, normalize_data
from visualization import plot_data


def main():
    # Load the data
    print("✓Loading data...")
    data = load_data('./data/data.csv')
    if data is None:
        print("✗ Failed to load data. Exiting.")
        return
    
    print("✓Data loaded successfully.")
    
    if data is not None:
        # Normalize the data
        print("-" * 60)
        normalized_data, norm_stats = normalize_data(data)
        print("✓Data normalized successfully.")
        print(f"✓Normalization stats: {norm_stats}")
        print("-" * 60)
        print("✓First 5 rows of normalized data:")
        print(normalized_data.head())        
        # Visualize the original data
        plot = plot_data(data)
        plot.show()
        
if __name__ == "__main__":
    main()
    