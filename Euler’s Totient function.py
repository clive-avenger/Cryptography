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

def euler_totient(p, q):
    """Calculate the Euler Totient Function value for n = p * q."""
    n = p * q
    phi_n = (p - 1) * (q - 1)
    return phi_n

def main():
    start_range = 10  # You can adjust the start of the range
    end_range = 100   # You can adjust the end of the range
    
    # Generate a list of prime numbers within the specified range
    prime_list = generate_prime_list(start_range, end_range)
    
    # Select two random prime numbers
    p, q = select_random_primes(prime_list)
    
    # Calculate the Euler Totient Function value
    phi_n = euler_totient(p, q)
    
    # Output the random prime numbers and the Euler Totient Function value
    print(f"Selected prime number p: {p}")
    print(f"Selected prime number q: {q}")
    print(f"Euler Totient Function value φ(n) for n = p * q: {phi_n}")

if __name__ == "__main__":
    main()

