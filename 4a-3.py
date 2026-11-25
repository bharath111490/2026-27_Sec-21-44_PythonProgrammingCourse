sentence = input("Enter a sentence: ")
words = sentence.split()
count = {}
for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
print("Word Frequencies:")
for word, freq in count.items():
    print(word, ":", freq)