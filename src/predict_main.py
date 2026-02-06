# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    predict_main.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tissad <tissad@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/06 14:01:31 by tissad            #+#    #+#              #
#    Updated: 2026/02/06 14:29:05 by tissad           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


"""
This module serves as the entry point for making predictions using a saved linear regression model.
It loads the model parameters and normalization statistics from a JSON file,
normalizes the input data, and uses the model to make predictions.
"""
import pandas as pd
from model_saver import load_model, predict_price

def main(args):
    """Main function to load the model and make predictions."""
    
    # Load the model parameters
    print("\nLoading model parameters...")
    if args.model_file:
        params = load_model(args.model_file)
    else:
        params = load_model('./models/model_params.json')
    if params is None:
        print("✗ Failed to load model parameters. Exiting.")
        return 1
    print("\n✓ Model parameters loaded successfully.")
    print(f"  - θ₀: {params['theta0']:.6f}")
    print(f"  - θ₁: {params['theta1']:.6f}")

    # Interactive prediction loop
    print("\n" + "-"*60)
    print("Enter mileage (km) to predict price (or 'exit' to quit):")
    print("-"*60)
    while True:
        try:
            user_input = input("Mileage (km): ")
            if user_input.lower() in ['q', 'quit', 'exit']:
                print("Exiting prediction mode. Goodbye!")
                break

            km = float(user_input)
            
            if km < 0:
                print("Mileage cannot be negative. Please enter a valid value.")
                continue
            predicted_price = predict_price(km, params)
            if predicted_price < 0:
                print("Predicted price is negative, which is not realistic. " \
                "Please check the model parameters or input value.")
                continue
            print("\n" + "="*60)
            print(f"Predicted price: {predicted_price:.2f} €")
            print("="*60)
        except ValueError:
            print("Invalid input. Please enter a numeric value for mileage or 'exit' to quit.")
        except KeyboardInterrupt:
            print("\nExiting prediction mode. Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again or type 'exit' to quit.")   
        
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Predict car prices using a saved linear regression model.")
    parser.add_argument('--model_file', type=str, help='Path to the JSON file containing the model parameters and normalization statistics.')
    
    args = parser.parse_args()
    main(args)