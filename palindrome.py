def is_palindrome(s):
    # Convert to string and lower case
    s = str(s).lower()
    # Remove spaces
    s = s.replace(" ", "")
    # Check palindrome
    return s == s[::-1]

# Example usage
word = input("Enter a word or number: ")
if is_palindrome(word):
    print(f"'{word}' is a Palindrome!")
else:
    print(f"'{word}' is NOT a Palindrome!")