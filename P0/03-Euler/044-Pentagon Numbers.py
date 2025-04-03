import math

# Function to generate the nth pentagonal number
def pentagonal(n):
    return n * (3 * n - 1) // 2

# Function to check if a number is pentagonal
def is_pentagonal(x):
    n = (math.sqrt(24 * x + 1) + 1) / 6
    return n.is_integer()

# Searching for the pair with the minimal difference
min_D = float('inf')  # Initialize to infinity
n = 1
pentagonals = set()  # To store generated pentagonal numbers

while True:
    P_n = pentagonal(n)
    pentagonals.add(P_n)

    # Compare with all previous pentagonal numbers
    for P_j in pentagonals:
        if P_n != P_j:
            sum_p = P_n + P_j
            diff_p = abs(P_n - P_j)

            if is_pentagonal(sum_p) and is_pentagonal(diff_p):
                min_D = min(min_D, diff_p)
                print(f"Found: P_j = {P_j}, P_k = {P_n}, D = {min_D}")

                # Since we need the smallest D, we can stop early
                print("Answer:", min_D)
                exit()

    n += 1  # Increment n to check the next pentagonal number
