import sys
sys.stdin = open('input.txt')

n = int(input())
user = []

for i in range(n):
    age, name = input().split()
    user.append([int(age), name, i])
user.sort(key=lambda x: (x[0], x[2]))
# print(user)

for x, y, z in user:
    print(x, y)