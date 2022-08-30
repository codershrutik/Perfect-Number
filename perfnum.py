def isPerfect(num):
    # To store sum of divisors
    sum = 1

    # Find all divisors and add them
    i = 2
    while i * i <= num:
        if num % i == 0:
            sum = sum + i + num / i
        i += 1

    # If sum of divisors is equal to
    # n, then n is a perfect number

    return (True if sum == num and num != 1 else False)


# Driver program
print("Below are all perfect numbers till 10000")
num = 2
for num in range(10000):
    if isPerfect(num):
        print(num, " is a perfect number")
