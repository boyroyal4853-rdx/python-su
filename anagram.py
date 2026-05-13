str1 = input("Enter First String: ")
str2 = input("Enter Second String: ")

if sorted(str1) == sorted(str2):
    print("Anagram")
else:
    print("Not Anagram")