
v, e = map(int, input().split())
par = [x for x in range(v+1)]

def find(x):
    if par[x] == x:
        return x
    par[x] = find(par[x])
    return par[x]

def union(x, y):
    x = find(x)
    y = find(y)

    par[x] = y

arr = []
for _ in range(e):
    a, b, c = map(int, input().split())
    arr.append([a, b, c]) # a, b가 c의 가중치를 가지는 간선

arr.sort(key= lambda x: x[2])

ans = 0
for i in arr:
    a, b, c = i
    if find(a) == find(b):
        continue
    union(a, b)
    ans += c

print(ans)