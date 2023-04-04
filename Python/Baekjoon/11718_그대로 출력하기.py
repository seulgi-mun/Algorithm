import sys
sys.stdin = open('input.txt')

while True:
    try:
        n = input()
        print(n)
    except:
        break