import sys
sys.stdin = open('input.txt')

n = int(input())
name = [input() for _ in range(n)]
# print(name)

asc_name = sorted(name)
des_name = sorted(name, reverse=True)
# print(asc_name)
# print(des_name)

if name == asc_name:
    print('INCREASING')
elif name == des_name:
    print('DECREASING')
else:
    print('NEITHER')