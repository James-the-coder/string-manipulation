
words = []

loops = int(input("how many words do you want to enter?: "))

for i in range(loops):
    word = input("Enter the word: ")
    words.append(word)
print(words)


letter = input("Enter the desired letter that the word begins with: ")

for i in words:
    if letter == i[0]:
        print(i)

