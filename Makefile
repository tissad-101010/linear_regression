# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tissad <tissad@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/05 15:48:00 by tissad            #+#    #+#              #
#    Updated: 2026/02/05 15:53:14 by tissad           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #



all: install


load_data:
	@echo "Loading data..."
	@python src/data_loader.py

run:
	@echo "Running the linear regression project..."
	@python src/main.py

install:
	@echo "Installing dependencies..."
	@pip install -r requirements.txt