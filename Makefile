# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: issad <issad@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/05 15:48:00 by tissad            #+#    #+#              #
#    Updated: 2026/02/05 22:46:31 by issad            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #



all: install


load_data:
	@echo "Loading data..."
	@python3 src/data_loader.py

run:
	@echo "Running the linear regression project..."
	@python3 src/main.py

install:
	@echo "Installing dependencies..."
	@pip install -r requirements.txt

clean:
	@echo "Cleaning up..."
	@find . -type f -name "*.pyc" -delete
	@find . -type d -name "__pycache__" -delete	
