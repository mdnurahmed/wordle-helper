import random
from collections import defaultdict

f = open('5-letter-words.txt', 'r')
words = set()
for line in f:
    line_list = list(line)
    line_list.pop()
    words.add(tuple(line_list))

f.close()


green = defaultdict(int)  # exact position
yellow = defaultdict(int)  # unknown position but the must have same frequency
red = set()  # cannot have these letters
greenSet = set()


def greenOk(word, green):
    for key in green:
        if word[key] != green[key]:
            return False
    return True


def redOk(word, red):
    for ch in word:
        if ch in red:
            return False
    return True


def yellowOk(word, yellow):
    f = defaultdict(int)
    for ch in word:
        f[ch] += 1
    for ch in yellow:
        if yellow[ch] != f[ch]:
            return False
    return True


cnt = 0

while len(words) > 0:
    now = next(iter(words))
    if greenOk(now, green) and redOk(now, red) and yellowOk(now, yellow):
        print(now)
        feedback = list(input())
        print(feedback)
        # this part is crucial
        newY = defaultdict(int)
        for i in range(len(now)):
            if feedback[i] == 'G':
                green[i] = now[i]
                greenSet.add(now[i])
            if feedback[i] == 'Y':
                newY[now[i]] += 1
            if feedback[i] == 'R':
                red.add(now[i])
        for key in newY:
            yellow[key] = max(yellow[key], newY[key])
        for el in red:
            if el in yellow or el in greenSet:
                red.remove(el)
        # print(green)
        # print(yellow)
        # print(red)
        # v = input()
    words.remove(now)
    cnt += 1
    if cnt % 100 == 0:
        print(f'{cnt} word seen')
