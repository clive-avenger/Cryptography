import random

def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while (i * i) <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_prime_list(start, end):
    """Generate a list of prime numbers in a given range."""
    prime_list = []
    for num in range(start, end + 1):
        if is_prime(num):
            prime_list.append(num)
    return prime_list

def select_random_primes(prime_list):
    """Select two random prime numbers from a list."""
    p = random.choice(prime_list)
    q = random.choice(prime_list)
    while p == q:
        q = random.choice(prime_list)
    return p, q

def main():
    start_range = 10  # You can adjust the start of the range
    end_range = 100   # You can adjust the end of the range
    
    # Generate a list of prime numbers within the specified range
    prime_list = generate_prime_list(start_range, end_range)
    
    # Select two random prime numbers
    p, q = select_random_primes(prime_list)
    
    # Output the random prime numbers
    print(f"Selected prime number p: {p}")
    print(f"Selected prime number q: {q}")

if __name__ == "__main__":
    main()
