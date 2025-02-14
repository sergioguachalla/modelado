def constant_multiplier(seed, multiplier, digits):
    """
    Generate a random number using the constant multiplier method.
    :param seed: The current seed.
    :param multiplier: The constant multiplier.
    :param digits: The number of digits to extract from the middle of the product.
    :return: The next random number and the updated seed.
    """
    product = seed * multiplier
    product_str = str(product).zfill(2 * digits)  # Pad with zeros to ensure 2*digits length
    middle = len(product_str) // 2 - digits // 2
    next_number = int(product_str[middle:middle + digits])
    
    return next_number, next_number

def generate_random_numbers(seed, multiplier, digits, count):
    """
    Generate a sequence of random numbers using the constant multiplier method.
    :param seed: The initial seed.
    :param multiplier: The constant multiplier.
    :param digits: The number of digits to extract from the middle of the product.
    :param count: The number of random numbers to generate.
    :return: A list of generated random numbers.
    """
    random_numbers = []
    current_seed = seed
    
    for _ in range(count):
        next_number, current_seed = constant_multiplier(current_seed, multiplier, digits)
        random_numbers.append(next_number)
    
    return random_numbers

# Example usage
if __name__ == "__main__":
    seed = 9803          # Initial seed
    multiplier = 6965   # Constant multiplier (commonly used in LCGs)
    digits = 4           # Number of digits to extract
    count = 10           # Number of random numbers to generate

    random_numbers = generate_random_numbers(seed, multiplier, digits, count)
    print("Generated random numbers:", random_numbers)