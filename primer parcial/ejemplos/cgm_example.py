# Parameters
a = int(input("Ingresar multiplicador (a): "))
b = int(input("Ingresar constante (b): "))
m = int(input("Ingresar modulo (m): "))
X0 = int(input("Ingresar valor inicial (X0): "))

# Number of random numbers to generate
n_terms = int(input("Cantidad de números: "))

# Generate the random numbers
X = X0
random_numbers = [X]

for _ in range(n_terms - 1):
    X = ((a * X) * b) % m
    random_numbers.append(X)

# Display the results as an array
print(f"Números generados: {random_numbers}")
