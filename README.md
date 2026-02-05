# Linear_regression

## Overview

**ft_linear_regression** is an introductory machine learning project focused on implementing **linear regression from scratch**. The goal is to understand the fundamental concepts behind machine learning by building a simple model that predicts the price of a car based on its mileage.

This project does not rely on high-level machine learning libraries. Instead, it emphasizes mathematical intuition, algorithmic thinking, and full ownership of the learning process.

---

## What Is Linear Regression and What Problems Does It Solve?

Linear regression is a **supervised learning algorithm** used to model the relationship between:

* an **input variable** (feature) → e.g. car mileage
* an **output variable** (target) → e.g. car price

It is used for **regression problems**, meaning problems where the output is a **continuous numerical value**.

Typical use cases include:

* Price prediction
* Trend estimation
* Forecasting
* Understanding correlations between variables

---

## The Equation of a Line

Linear regression is based on the equation of a straight line:

```
y = θ0 + θ1 × x
```

Where:

* `x` is the input feature (mileage)
* `y` is the predicted output (price)
* `θ0` is the intercept (bias)
* `θ1` is the slope (weight)

In this project:

```
estimatePrice(mileage) = θ0 + θ1 × mileage
```

---

## Example

Suppose we have:

* `θ0 = 5000`
* `θ1 = -0.05`
* `mileage = 100000`

Then:

```
estimated price = 5000 - (0.05 × 100000) = 0
```

This means the model predicts that a car with 100,000 km has no remaining value.

---

## How Do We Find the Best Line?

The goal of linear regression is to find the values of `θ0` and `θ1` that **minimize the prediction error** across all training examples.

This is done using:

1. A **cost (loss) function**
2. An optimization algorithm called **gradient descent**

---

## The Cost Function (Loss Function)

The cost function measures how wrong the model’s predictions are.

For linear regression, we use the **Mean Squared Error (MSE)**:

```
J(θ0, θ1) = (1 / m) × Σ (estimatePrice(xᵢ) − yᵢ)²
```

Where:

* `m` is the number of training examples
* `xᵢ` is the mileage
* `yᵢ` is the actual price

The smaller the cost, the better the model.

---

## Gradient Descent

Gradient descent is an **iterative optimization algorithm** used to minimize the cost function.

It works by:

* computing the gradient (direction of steepest increase)
* updating parameters in the opposite direction
* repeating until convergence

---

## Update Formulas

At each iteration, the parameters are updated simultaneously:

```
tmpθ0 = learningRate × (1 / m) × Σ (estimatePrice(xᵢ) − yᵢ)

tmpθ1 = learningRate × (1 / m) × Σ (estimatePrice(xᵢ) − yᵢ) × xᵢ
```

Then:

```
θ0 = θ0 − tmpθ0
θ1 = θ1 − tmpθ1
```

---

## The Learning Rate (α)

The **learning rate** controls how big each update step is.

* Too small → training is very slow
* Too large → the model may diverge

Choosing a good learning rate is critical for stable and efficient training.

---

## Normalization (Crucial!)

Normalization rescales input values to a similar range.

Why it matters:

* Mileage values can be very large
* Large values slow down gradient descent
* Normalization improves convergence speed and stability

A common technique is **min-max normalization**:

```
x' = (x − min) / (max − min)
```

---

## Algorithm (Step by Step)

### **Step 1:** Load the dataset
```python
    data = pd.read_csv('data.csv')
    X = data['km'].values      # [240000, 139800, ...]
    y = data['price'].values   # [3650, 3800, ...]
```
___
### **Step 2:** Normalize the mileage values
```python
    X_mean = np.mean(X)        # μₓ = 101,066
    X_std = np.std(X)          # σₓ = 52,674
    X_norm = (X - X_mean) / X_std

    y_mean = np.mean(y)        # μᵧ = 6,332
    y_std = np.std(y)          # σᵧ = 1,320
    y_norm = (y - y_mean) / y_std
```

___
### **Step 3:** Initialize `θ0 = 0` and `θ1 = 0`
```python
    θ₀ = 0.0                   # Intercept
    θ₁ = 0.0                   # Pente
```
___
### **Step 4:** Choose a learning rate
```python
    α = 0.1                    # Learning rate
    iterations = 1000          # Nombre d'itérations
```
___
### **Step 5:** Repeat until convergence:

   * 
   * Compute the cost
   * Update `θ0` and `θ1` using gradient descent
```
For i = 1 to 1000:

    # 1. Compute predictions
    ŷ = θ₀ + θ₁ × X_norm

    # 2. Compute errors
    errors = ŷ - y_norm

    # 3. Compute gradients
    grad_θ₀ = (1/m) × Σ(errors)
    grad_θ₁ = (1/m) × Σ(errors × X_norm)

    # 4. Update parameters
    θ₀ = θ₀ - α × grad_θ₀
    θ₁ = θ₁ - α × grad_θ₁

    # 5. Compute cost
    J = (1 / 2m) × Σ(errors²)
```

___
### **Step 6:** Use the model to predict prices for new mileage values
For a new mileage km_new:
```
    # 1. Normalize
    km_norm = (km_new − X_mean) / X_std

    # 2. Predict (normalized)
    price_norm = θ₀ + θ₁ × km_norm

    # 3. Denormalize
    price = price_norm × y_std + y_mean
```
---

## Project Goal

The objective of this project is to:

* Understand the foundations of machine learning
* Implement linear regression without automated tools
* Learn gradient descent mathematically and practically
* Build intuition before moving to more complex models

This project serves as a solid first step into machine learning.

## Requirements
* Python 3.8 or higher
* NumPy
* Pandas
* Matplotlib

## Ressources:
 - [Normalization - Wikipedia](https://en.wikipedia.org/wiki/Standard_score)

## RUN THE PROJECT
1. Clone the repository
2. Install dependencies
    ``` bash
    pip install -r requirements.txt
    #or
    make install

    ```
3. Run
    ``` bash
    python src/main.py
    #or
    make run
    ```

## Results
After running the project, you should see:
* A plot of the original data (mileage vs price)
![original_data](./plot/original_data_plot.png)
