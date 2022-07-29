import sys, math
sys.stdin = open('input.txt')

t = int(input())
# words = [input() for _ in range(t)]
# print(words)

for _ in range(t):
    words = input()
    # print(words)

    if words == words[::-1]:
        print(0)
    else:
        original_words = list(words)
        change_words = list(words)

        # 홀수인 경우 올림으로 받아서 진행해야 빼먹지 않음
        for i in range(math.ceil(int(len(words)/2))):
            # 다른경우 앞에서 뺄 것인지 뒤에서 뺄 것인지
            if words[i] != words[-(i+1)]:
                original_words.pop(i)
                change_words.pop(-(i+1))

                # 앞에서 뺀다면
                if original_words == original_words[::-1]:
                    print(1)
                    break

                # 뒤에서 뺀다면
                if change_words == change_words[::-1]:
                    print(1)
                    break

                # 둘 다 아니면
                print(2)
                break