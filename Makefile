# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tissad <tissad@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/05 15:48:00 by tissad            #+#    #+#              #
#    Updated: 2026/02/06 15:31:54 by tissad           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #



all: install


load_data:
	@echo "Loading data..."
	@python3 src/data_loader.py

fit:
	@echo "Running the linear regression project..."
	@python3 src/linear_regression_main.py
predict:
	@echo "Running the prediction script..."
	@python3 src/predict_main.py --model_file ./models/model_params.json 
precision:
	@echo "Running the precision evaluation script..."
	@python3 src/precision_main.py --model_file ./models/model_params.json --data_file ./data/test_data.csv
install:
	@echo "Installing dependencies..."
	@pip install -r requirements.txt

clean:
	@echo "Cleaning up..."
	@find . -type f -name "*.pyc" -delete
	@find . -type d -name "__pycache__" -delete	
