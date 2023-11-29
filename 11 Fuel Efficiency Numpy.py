import numpy as np

fuel_efficiency = np.array([25, 30, 28, 35, 22, 24, 32, 26, 29])

average_fuel_efficiency = np.mean(fuel_efficiency)

print("Average Fuel Efficiency:", average_fuel_efficiency)

old_model_efficiency = fuel_efficiency[3]
new_model_efficiency = fuel_efficiency[6]

percentage_improvement = ((new_model_efficiency - old_model_efficiency) / old_model_efficiency) * 100

print(f"Percentage Improvement between Model 3 and Model 6: {percentage_improvement:.2f}%")
