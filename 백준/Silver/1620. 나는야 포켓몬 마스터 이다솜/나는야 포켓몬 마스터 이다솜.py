n, m = map(int, input().split())

pokemon = {}

for i in range(1, n+1):
    name = input()
    pokemon[name] = i
    pokemon[str(i)] = name

for j in range(m):
    query = input()
    print(pokemon[query])