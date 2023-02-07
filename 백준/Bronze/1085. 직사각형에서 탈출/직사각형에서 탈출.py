x, y, w, h = map(int, input().split())
print(min(abs(x-0),abs(w-x),abs(y-0),abs(y-h)))