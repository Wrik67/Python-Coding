word = input("Enter a string to cheak the: ")
letter = input("Enter a later to find a count: ")

count = 0

for i in word:
    if i == letter:
        count = count + 1
print(f"The later '{letter}' occurs {count} times in the sentence")