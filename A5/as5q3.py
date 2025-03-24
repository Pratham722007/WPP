def next_permutation(word):
    word = list(word)
    i = len(word) - 2
    while i >= 0 and word[i] >= word[i + 1]:
        i -= 1
    if i == -1:
        return "no answer"
    j = len(word) - 1
    while word[j] <= word[i]:
        j -= 1
    word[i], word[j] = word[j], word[i]
    word = word[:i + 1] + word[i + 1:][::-1]
    return ''.join(word)

def main():
    t = int(input())
    for i in range(t):
        word = input()
        print(next_permutation(word))

main()