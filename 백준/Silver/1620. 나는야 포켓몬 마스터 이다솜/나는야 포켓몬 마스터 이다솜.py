n, m = map(int, input().split())
pokemons = {}
for i in range(1, n+1):
    name = input().strip()
    pokemons[name] = i
    pokemons[str(i)] = name
for j in range(m):
    query = input().strip()
    print(pokemons[query])
