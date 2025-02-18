expected_array = []
observed_array = []
result = 0  # Initialize the result variable

for i in range(7):
    ne = float(input("expected: "))
    ni = float(input("observed: "))
    expected_array.append(ne)
    observed_array.append(ni)

for i in range(len(expected_array)):  # Loop over the indices of the arrays
    sqr = (observed_array[i] - expected_array[i])**2
    chi = (sqr / expected_array[i])  # Dividing by expected value, not observed value
    result += chi  # Accumulate chi-squared value

print(result)
