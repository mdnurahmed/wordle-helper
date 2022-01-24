# Opening file
allWordFile = open('english3.txt', 'r')
count = 0
res = []
for line in allWordFile:
    count += 1
    if len(line) == 6:
        res.append(line)

allWordFile.close()

print(f"5 letter words found {len(res)} out of {count}")

f = open("5-letter-words.txt", "a")
for word in res:
    f.write(word)
f.close()
