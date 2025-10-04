def function(x,modulus):
    y = (x**3-9*x**2+23*x-5) % modulus
    if y:
        return 0
    else:
        print(f"{x} is a root")
        return 1

def main():
    modulus = int(input("Enter a modulus: "))
    roots = 0
    for x in range(modulus):
        roots += function(x,modulus)
    if roots == 0:
        print("No roots")
if __name__ == "__main__":
    main()
