import sys
sys.stdin = open('input.txt')

hap = 0
sub_hap = 0
for i in range(20):
    sub, score, grade = input().split()
    score = float(score)

    if grade == 'P':
        continue
    else:
        sub_hap += score

    if grade == 'A+':
        hap += score * 4.5
    elif grade == 'A0':
        hap += score * 4.0
    elif grade == 'B+':
        hap += score * 3.5
    elif grade == 'B0':
        hap += score * 3.0
    elif grade == 'C+':
        hap += score * 2.5
    elif grade == 'C0':
        hap += score * 2.0
    elif grade == 'D+':
        hap += score * 1.5
    elif grade == 'D0':
        hap += score * 1.0

print(round(hap/sub_hap, 6))
print('{:.6f}'.format(hap/sub_hap))
print(f'{hap/sub_hap:.6f}')