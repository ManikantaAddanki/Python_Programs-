n = int(input("Enter a number: "))

while True:
    n += 1
    is_prime = True

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"The nearest prime number is: {n}")
        break