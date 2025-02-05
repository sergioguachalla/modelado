def lcg(seed, a, c, m, num_terms):
    """
    Generates a sequence of random numbers using the Linear Congruential Generator (LCG) method.

    Parameters:
        seed (int): Initial seed value (X_0).
        a (int): Multiplier.
        c (int): Increment.
        m (int): Modulus.
        num_terms (int): Number of terms to generate.

    Returns:
        list: A list of generated random numbers.
    """
    sequence = []
    X_n = seed  # Initialize with the seed value

    for _ in range(num_terms):
        X_n = (a * X_n + c) % m  # Apply the LCG formula
        sequence.append(X_n)

    return sequence

# Parameters
c = 89
m = 100
X_0 = int(input("Enter the initial seed value (X_0): "))  # User provides the seed
num_terms = int(input("Enter the number of terms to generate: "))
a = 81
# Generate the sequence
random_sequence = lcg(X_0, a, c, m, num_terms)

# Output the sequence
print("Generated sequence:", random_sequence)