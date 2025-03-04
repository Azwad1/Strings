"""
There are 50 students in the class. The teacher wants to arrange them in the height order. So help the teacher to find the smallest person and tallest to arrange.(count the number of lowercase letters and uppercase letters in a string.)
Problem Description:
The program takes a string and counts the number of lowercase letters and uppercase letters in the string.
Problem Solution:
1. Take a string from the user and store it in a variable.
2. Initialize the two count variables to 0.
3. Use a for loop to traverse through the characters in the string and increment the first count variable each time a lowercase character is encountered and increment the second count variable each time a uppercase character is encountered.
4. Print the total count of both the variables.
5. Exit.
Input & Output Format:
Input consists of one string.
Output consists of two integers.
First output consists of count of the uppercase.
Second output consists of count of the lowercase.
Sample Input:
Cyfuno
Sample Output:
Uppercase: 1
Lowercase: 5
"""
user_input = input()
uppercase_count = 0
lowercase_count = 0
for char in user_input:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1

print(f"Uppercase: {uppercase_count}")
print(f"Lowercase: {lowercase_count}")
