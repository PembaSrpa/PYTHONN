# Resolving real-world problems
# Counting word frequency in text

text = "the quick brown fox jumps over the lazy dog the dog did not mind"

# Clean and split text into words
words = text.lower().split()

# Dictionary to store word frequencies
word_freq = {}

for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

print("Word frequencies:")
for word, freq in word_freq.items():
    print(f"{word}: {freq}")
