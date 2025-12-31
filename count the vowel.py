sentence = str(input("Enter a sentence: "))

count = 0

for i in sentence:
    if i in "AEIOUaeiou":
     count = count + 1
 
print("Total vowel count:", count) 