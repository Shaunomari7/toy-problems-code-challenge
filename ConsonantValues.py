#!/usr/bin/env python3

def highest_consonant_value(word):
    #Define the values of the letters
    values = {chr(i+97): i+1 for i in range(26)}

    #initialize the maximum value and the current sum
    max_value = 0
    current_sum = 0

    #iterate over each of the characters in the string
    for char in word:
        #if the character is a consonant, add its value to the current sum
        if char.lower() not in "aeiou":
            current_sum += values[char]
            #update the maximum value if necessary
            if current_sum > max_value:
                max_value = current_sum
        #if the character is a vowel, read the current sum
        else:
            current_sum = 0

    print(max_value)

highest_consonant_value("cristiano")