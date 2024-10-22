"""
Write a  Python Program to calculate the number of words and characters present in a string.
Input & Output Format:
Input consists of a string.
Output consists of two integers.
First output refers to the count of the words.
Second output refers to the count of the characters in a given string,
Sample Input:
Cyfuno
Sample Output:
Words: 1
Letters: 6
"""
user_input = input("Enter a string: ")
word_count = len(user_input.split())
char_count = len(user_input)
print(f"Words: {word_count}")
print(f"Letters: {char_count}")
