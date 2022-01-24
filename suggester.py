from collections import defaultdict


def read_words(words):
    f = open('5-letter-words.txt', 'r')
    for line in f:
        line_list = list(line)
        line_list.pop()
        words.add(tuple(line_list))

    f.close()


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


def find_suggestion(words):
    green = defaultdict(int)  # exact position
    # unknowSuggestionn position but the letters must have same frequency
    yellow = defaultdict(int)
    red = set()  # cannot have these letters
    greenSet = set()  # this set contains values of green dictionary
    cnt = 0
    while len(words) > 0:
        nowSuggestion = next(iter(words))
        if greenOk(nowSuggestion, green) and redOk(nowSuggestion, red) and yellowOk(nowSuggestion, yellow):
            print(nowSuggestion)
            feedback = list(input())
            print(feedback)
            # this part is crucial
            newY = defaultdict(int)
            for i in range(len(nowSuggestion)):
                if feedback[i] == 'G':
                    green[i] = nowSuggestion[i]
                    greenSet.add(nowSuggestion[i])
                if feedback[i] == 'Y':
                    newY[nowSuggestion[i]] += 1
                if feedback[i] == 'R':
                    red.add(nowSuggestion[i])
            for key in newY:
                yellow[key] = max(yellow[key], newY[key])
            for el in red:
                if el in yellow or el in greenSet:
                    red.remove(el)
            # print(green)
            # print(yellow)
            # print(red)
            # v = input()
        words.remove(nowSuggestion)
        cnt += 1
        if cnt % 100 == 0:
            print(f'{cnt} words seen')


if __name__ == "__main__":
    words = set()
    read_words(words)
    find_suggestion(words)
    print("End of Code")
