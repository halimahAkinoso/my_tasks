# 9 print vowel in words
sentence = input("Enter a sentence: ")

vowels = ["a","e","i","o","u"]
count = 0
for char in sentence:
  if char in vowels:
    count += 1

print("Number of vowels in the given string is: ", count)
