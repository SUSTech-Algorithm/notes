def gcd(a, b):
    """Compute the greatest common divisor of a and b using Euclid's algorithm."""
    while b:
        a, b = b, a % b
    return abs(a)              
def lcm(a, b):
    """Compute the least common multiple of a and b."""
    return abs(a * b) // gcd(a, b) if a and b else 0

def prime_factors(n):
    """Return the prime factorization of n as a list of tuples (prime, exponent)."""
    i = 2
    factors = []
    while i * i <= n:
        count = 0
        while (n % i) == 0:
            n //= i
            count += 1
        if count > 0:
            factors.append((i, count))
        i += 1
    if n > 1:
        factors.append((n, 1))
    return factors