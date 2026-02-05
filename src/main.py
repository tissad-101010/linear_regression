# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tissad <tissad@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/05 16:27:33 by tissad            #+#    #+#              #
#    Updated: 2026/02/05 17:20:12 by tissad           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""
Docstring pour main
"""

from data_loader import load_data, normalize_data
from visualization import plot_data, save_plot


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

        # Visualize the original data
        plot = plot_data(data)
        # plot.show()
        save_plot(plot, './plot/original_data_plot.png')
        
if __name__ == "__main__":
    main()
    