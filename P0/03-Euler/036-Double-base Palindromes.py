def is_palindrome(s):
    return s == s[::-1]  # Check if string is the same forwards and backwards

def sum_palindromes(limit):
    total_sum = 0
    
    for num in range(1, limit):
        # Check if the number is a palindrome in decimal
        if is_palindrome(str(num)):
            # Convert the number to binary and check if it's a palindrome in binary
            if is_palindrome(bin(num)[2:]):  # bin(num) returns a string like '0b101', so [2:] removes the '0b'
                total_sum += num
    
    return total_sum

# Example: Find sum of all palindromes less than 1,000,000
limit = 1000000
result = sum_palindromes(limit)
print(result)  # This will print the sum of all palindromic numbers in both bases
