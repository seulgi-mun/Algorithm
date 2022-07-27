import sys
sys.stdin = open('input.txt')


T = int(input())

# check = {'25': 0, '10': 0, '5': 0, '1': 0}
change = [25, 10, 5, 1]
check = [0, 0, 0, 0]

for _ in range(T):
    money = int(input())
# print(money)

    for i in range(len(change)):
        check[i] = money // change[i]
        money = money % change[i]

    print(' '.join(map(str, check)))


# T = int(input())

# for _ in range(T):
#     money = int(input())        
#     coin = {25: 0, 10: 0, 5: 0, 1: 0}
    
#     while money:
#         for num in [25, 10, 5, 1]:
#             while money >= num:
#                 money -= num
#                 coin[num] += 1
                
#     print(coin[25], coin[10], coin[5], coin[1]) 