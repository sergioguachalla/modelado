# Parameters
a = 211       # Multiplier
b = 16       # Added constant
m = 10 ** 8      # Modulus
X0 = 13   # Initial value

# Number of random numbers to generate
n_terms = int(input("Cantidad de números: "))

# Generate the random numbers
X = X0
random_numbers = [X]

for _ in range(n_terms - 1):
    X = ((a * X) * b) % m
    random_numbers.append(X)

# Display the results as an array
print(f"Generated random numbers: {random_numbers}")
