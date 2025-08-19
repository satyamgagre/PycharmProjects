# Example dataset
import pandas as pd
from numpy.ma.extras import median

data = pd.Series([10, 20, 20, 30, 40, 50, 50, 50, 60])

print("Data:")
print(data.values)

# Measures of Central Tendency
# Mean
mean_value = data.mean()
print("Mean : ", mean_value)

# Median
median_value = data.median()
print("Median : ", median_value)

# Mode
mode_value = data.mode()
print("Mode : ", mode_value[0])
print("Mode : ", mode_value)