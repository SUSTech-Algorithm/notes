from euclid import gcd, lcm, prime_factors
a, b = map(int, input("Enter two numbers: ").split())
if gcd(a, b) == 1:
    print(f"{a} and {b} are **coprime**.")
else:
    print(f"The GCD of {a} and {b} is {gcd(a, b)}")
print(f"The LCM of {a} and {b} is {lcm(a, b)}")
print(f"The prime factors of {a} are {prime_factors(a)}")
print(f"The prime factors of {b} are {prime_factors(b)}")