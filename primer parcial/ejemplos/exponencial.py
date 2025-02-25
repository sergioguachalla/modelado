import pandas as pd
import numpy as np
import scipy.stats as stats


# Data
data = {
    "X": ["10-15", "15-20", "20-25", "25-30", "30-35", "35-40", "40-45"],
    "ni": [30, 25, 22, 18, 19, 12, 8],
    "midpoint": [12.5, 17.5, 22.5, 27.5, 32.5, 37.5, 42.5],
    "lower_bound": [10, 15, 20, 25, 30, 35, 40],
    "upper_bound": [15, 20, 25, 30, 35, 40, 45]
}

df = pd.DataFrame(data)

# Total sample size
n = sum(df["ni"])

# Compute lambda (mean)
lambda_mean = sum(df["ni"] * df["midpoint"]) / n
rounded_lambda = round(lambda_mean, 2)

# Compute expected frequencies
df["expected_ni"] = n * (np.exp(-df["lower_bound"] / rounded_lambda) - np.exp(-df["upper_bound"] / rounded_lambda))
# Calculate Chi-Square statistic
df["chi_sq_term"] = ((df["ni"] - df["expected_ni"]) ** 2) / df["expected_ni"]
chi_square = df["chi_sq_term"].sum()



k = 7  
r = 1  
alpha = 0.05 

# Degrees of freedom
df = k - r - 1
chi_critical = stats.chi2.ppf(1 - alpha, df)

print(f"Chi-Square Critical Value (χ²_{df}, {1-alpha}): {round(chi_critical, 4)}")

# Display results
print(f"Chi-Square value: {round(chi_square, 4)}")
# Display DataFrame with expected frequencies
