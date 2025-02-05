def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):  # Only check up to sqrt(n)
        if n % i == 0:
            return False
    return True

def print_primes_between(start, end):
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")

# Input two numbers
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print(f"Prime numbers between {start} and {end}:")
print_primes_between(start, end)
