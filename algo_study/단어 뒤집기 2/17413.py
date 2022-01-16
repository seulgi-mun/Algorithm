import sys
sys.stdin = open('input.txt')

word = list(input())
# print(word)

temp = []
stack = []
# print(word[-1])

# while word:
#     t = word.pop(0)
#     if t == '<':
#         temp.append(t)
#     print(t)
# print(temp)

for i in range(len(word)):
    if word[i] == '<':
        if len(temp) != 0:
            stack.append(temp)
            temp = ''
        temp += '<'
        # stack.append(temp[:-1])
    elif word[i] == '>':
        temp += '>'
        stack.append(temp)
        temp = ''
    else:
        if word[i] != ' ':
            temp += word[i]

        if word[i] == ' ':
            temp += ' '
            stack.append(temp)
            temp = ''
        if i == len(word)-1:
            stack.append(temp[::-1])
            temp = ''

print(*stack, sep='')