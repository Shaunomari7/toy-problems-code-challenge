#!/usr/bin/env python3

def exactly_two_positive(a, b, c):
    #initialize counter
    positive_count = 0
    # Check if each number is positive.
    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1
    # Return True if the count of positive numbers is exactly 2, False otherwise.
    return positive_count == 2

# Example usage:
result = exactly_two_positive(23, 15, -3)
print(result) 
