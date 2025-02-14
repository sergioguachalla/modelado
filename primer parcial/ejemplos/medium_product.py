def medium_product(seed1, seed2, digits):
    """
    Generate a random number using the medium product method.
    :param seed1: First seed number.
    :param seed2: Second seed number.
    :param digits: Number of digits in the seeds.
    :return: Next random number and updated seeds.
    """
    product = seed1 * seed2
    product_str = str(product).zfill(2 * digits)  # Pad with zeros to ensure 2*digits length
    middle = len(product_str) // 2 - digits // 2
    next_number = int(product_str[middle:middle + digits])
    
    # Update seeds for the next iteration
    seed1 = seed2
    seed2 = next_number
    
    return next_number, seed1, seed2

def generate_random_numbers(seed1, seed2, digits, count):
    """
    Generate a sequence of random numbers using the medium product method.
    :param seed1: First initial seed.
    :param seed2: Second initial seed.
    :param digits: Number of digits in the seeds.
    :param count: Number of random numbers to generate.
    :return: List of generated random numbers.
    """
    random_numbers = []
    current_seed1 = seed1
    current_seed2 = seed2
    
    for _ in range(count):
        next_number, current_seed1, current_seed2 = medium_product(current_seed1, current_seed2, digits)
        random_numbers.append(next_number)
    
    return random_numbers

# Example usage
if __name__ == "__main__":
    seed1 = 5015  # First initial seed
    seed2 = 5734  # Second initial seed
    digits = 4    # Number of digits in the seeds
    count = 10    # Number of random numbers to generate

    random_numbers = generate_random_numbers(seed1, seed2, digits, count)
    print("Generated random numbers:", random_numbers)