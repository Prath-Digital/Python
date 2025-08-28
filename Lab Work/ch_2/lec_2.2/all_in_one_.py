# For loop to print numbers from 1 to 20, skipping numbers divisible by 4
for i in range(1, 21):
    if i % 4 == 0:
        continue
    print(i)

# While loop to print numbers from 1 to 10, stopping at 7
num = 1
while num <= 10:
    if num == 7:
        break
    print(num)
    num += 1

# Iterate over string "PYTHON", skip vowels, print consonants
word = "PYTHON"
vowels = "AEIOU"
for char in word:
    if char in vowels:
        continue
    print(char)

# List comprehension for cubes of numbers 1 to 10
cubes = [x**3 for x in range(1, 11)]
print("Cubes:", cubes)

# List comprehension for even numbers from 1 to 50
evens = [x for x in range(1, 51) if x % 2 == 0]
print("Even numbers:", evens)

# List comprehension for words starting with a vowel
words = ["apple", "banana", "orange", "grape", "umbrella", "kiwi"]
vowel_words = [word for word in words if word[0].lower() in "aeiou"]
print("Words starting with a vowel:", vowel_words)

# Nested loops for multiplication table (1 to 5)
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i}x{j}={i*j}")