import sys
input = sys.stdin.readline

n, m = map(int, input().split())

parent = list(range(n+1))
rank = [1]*(n+1)


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    p1, p2 = find(a), find(b)
    if rank[p1] > rank[p2]:
        parent[p2] = p1
    else:
        parent[p1] = p2
        if rank[p1] == rank[p2]:
            rank[o2] += 1


def same(a, b): return find(a) == find(b)


print(same)
