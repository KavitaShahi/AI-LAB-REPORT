import math
import random
import matplotlib.pyplot as plt

# Define the objective function (e.g., sum of squares)
def objective_function(x):
    return x**2

# Temperature schedule function (cooling schedule)
def temperature_schedule(initial_temp, cooling_rate, iteration):
    return initial_temp * (cooling_rate ** iteration)

# Acceptance probability function based on the temperature
def acceptance_probability(current_value, new_value, temperature):
    if new_value < current_value:
        return 1.0  # Always accept better solutions
    else:
        # Accept worse solution with probability
        return math.exp(-(new_value - current_value) / temperature)

# Simulated Annealing Demonstration: Plot the probability of accepting an inferior node
def simulated_annealing_demo(initial_temp, cooling_rate, iterations):
    probabilities = []
    
    # Start with a random initial state
    current_value = random.uniform(-10, 10)
    
    for iteration in range(iterations):
        # Generate a neighboring solution (random step)
        new_value = current_value + random.uniform(-1, 1)
        
        # Compute the objective function values
        current_obj = objective_function(current_value)
        new_obj = objective_function(new_value)
        
        # Calculate the temperature at this iteration
        temperature = temperature_schedule(initial_temp, cooling_rate, iteration)
        
        # Calculate the probability of accepting the new state (if worse)
        prob_accept = acceptance_probability(current_obj, new_obj, temperature)
        probabilities.append(prob_accept)
        
        # Decide whether to move to the new state
        if random.random() < prob_accept:
            current_value = new_value
    
    return probabilities

# Set parameters for the simulation
initial_temp = 100  # Initial temperature
cooling_rate = 0.99  # Cooling rate
iterations = 100  # Number of iterations

# Run the simulation
probabilities = simulated_annealing_demo(initial_temp, cooling_rate, iterations)

# Plot the effect of temperature on the probability of accepting an inferior node
plt.plot(probabilities)
plt.title('Effect of Temperature on Probability of Accepting Inferior Node')
plt.xlabel('Iterations')
plt.ylabel('Probability of Accepting Inferior Solution')
plt.grid(True)
plt.show()
