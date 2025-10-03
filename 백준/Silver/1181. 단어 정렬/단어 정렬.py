import sys

N = int(sys.stdin.readline())

word_set = set()
    
for _ in range(N):
    input_text = str(sys.stdin.readline().strip())
    word_set.add(input_text)

word_list = sorted(word_set, key = lambda word: (len(word), word))
    
for word in word_list:
    print(word)