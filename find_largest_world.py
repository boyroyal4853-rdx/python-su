text = input("Enter Sentence: ")

words = text.split()

largest = max(words, key=len)

print("Largest Word =", largest)