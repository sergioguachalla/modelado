import numpy as np
from collections import Counter
from scipy.stats import chi2

# Data string (values separated by spaces and newlines)
data_str = """0.39670 0.57861 0.10420 0.50683 0.99599 0.99506 0.75180 0.86573
0.18231 0.77828 0.67768 0.49340 0.99267 0.18774 0.71643 0.81548
0.93019 0.00887 0.43128 0.77992 0.99343 0.81064 0.49640 0.66545
0.17949 0.05265 0.65878 0.91444 0.81309 0.37949 0.23203 0.33195
0.05638 0.59204 0.47730 0.75437 0.80350 0.19447 0.22265 0.66533
0.39081 0.73804 0.03576 0.76359 0.77717 0.07468 0.97661 0.84780
0.07337 0.42493 0.69261 0.18830 0.76361 0.76796 0.02133 0.37448
0.32418 0.85384 0.41356 0.91655 0.42446 0.49268 0.02229 0.57044
0.52238 0.51540 0.35613 0.56161 0.07314 0.90936 0.82914 0.90868
0.35873 0.27916 0.51612 0.07940 0.29996 0.32350 0.24968 0.18188
0.35082 0.43715 0.54395 0.91340 0.26302 0.87738 0.04897 0.01376
0.33147 0.91919 0.02278 0.89232 0.62109 0.20053 0.94825 0.05641"""

# Convert data string to a list of floats
values = []
for line in data_str.strip().split('\n'):
    for num in line.split():
        num = num.replace(',', '.')  # In case commas are used as decimal separators
        values.append(float(num))
values = np.array(values)

# Define the interval [alpha_interval, beta_interval]
alpha_interval = 0.5
beta_interval = 0.6

# p is the probability that a number falls inside the interval, for U(0,1)
p = beta_interval - alpha_interval  # p = 0.6 - 0.5 = 0.1

# Calculate gaps: count consecutive numbers outside the interval until one is found inside
gaps = []
count = 0
for x in values:
    if alpha_interval <= x <= beta_interval:
        gaps.append(count)
        count = 0
    else:
        count += 1
# Do not include the final gap if the sequence ends outside the interval
# (If desired, you could append count here)

# Count observed frequencies for each gap length
counts = Counter(gaps)
max_gap = max(counts.keys()) if counts else 0
obs_freq = [counts.get(k, 0) for k in range(max_gap + 1)]

# Total number of gaps
n_gaps = len(gaps)

# Calculate expected frequencies for each gap length k:
# Expected probability: P(gap = k) = (1-p)^k * p
exp_freq = [n_gaps * ((1 - p) ** k * p) for k in range(max_gap + 1)]

# Group categories if the expected frequency is less than 5
def group_frequencies(obs, exp):
    while len(exp) > 1 and exp[-1] < 5:
        exp[-2] += exp[-1]
        obs[-2] += obs[-1]
        exp.pop()
        obs.pop()
    return obs, exp

obs_grouped, exp_grouped = group_frequencies(obs_freq, exp_freq)

# Calculate chi-square statistic
chi2_stat = 0
for o, e in zip(obs_grouped, exp_grouped):
    if e > 0:
        chi2_stat += (o - e) ** 2 / e

# Degrees of freedom = number of grouped categories - 1
df = len(obs_grouped) - 1

# Compute p-value
p_value = 1 - chi2.cdf(chi2_stat, df)

# Output the results
print("RESULTS OF THE GAP TEST")
print("Interval [alpha, beta] = [{}, {}]".format(alpha_interval, beta_interval))
print("p (beta - alpha) =", p)
print("Total number of gaps =", n_gaps)
print("Observed frequencies (grouped):", obs_grouped)
print("Expected frequencies (grouped):", [round(e, 2) for e in exp_grouped])
print("Chi-square statistic =", round(chi2_stat, 4))
print("Degrees of freedom =", df)
print("p-value =", p_value)

if p_value < 0.05:
    print("Conclusion: Reject H0 (the gaps do not follow the expected uniform distribution).")
else:
    print("Conclusion: Do not reject H0 (the gaps are consistent with a uniform distribution).")
