import sys
sys.stdin = open('input.txt')

n, m, l = map(int, input().split())

if n == m == l:
    print(10000 + (n*1000))
elif n != m and n != l and m != l:
    print(max(n, m, l)*100)
else:
    if n == m:
        print(1000 + (n*100))
    elif n == l:
        print(1000 + (n*100))
    elif m == l:
        print(1000 + (m*100))