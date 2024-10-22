"""
Write a Python Program to remove the nth index character from a non-empty string.
Input & Output Format:
Input consists of a string and one integer.
The first input consists of a string.
The second input refers to the index position.
The output consists of a string.
Sample Input:
cyfuno
4
Sample Output:
cyfuo
"""
def remove_nth_char(string, n):
    new_string = string[:n] + string[n+1:]
    return new_string

user_input = input("Enter a string: ")
index = int(input("Enter the index of the character to remove: "))

print(f"Modified string: {remove_nth_char(user_input, index)}")
