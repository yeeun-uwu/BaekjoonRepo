def ass_room(h, w, n):
    floor = (n-1) % h + 1
    room = (n-1) // h + 1
    return f"{floor}{room:02d}"

t = int(input())

for i in range(t):

    h, w, n = map(int, input().split())
    print(ass_room(h, w, n))

    
