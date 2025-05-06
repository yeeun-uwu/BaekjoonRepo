star = [
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0]
]

def is_star_or_space(x, y, l):
    dx = (x // l) % 5
    dy = (y // l) % 5

    if l == 1:
        return star[dy][dx] == 1
    
    if star[dy][dx]: #1이면 별 그려야댐
        return is_star_or_space(x, y, l//5)

    return False

def star_in_star(n):
    if n == 0:
        print("*")
        return #0이면 그리고 돌아감
    
    l = 5 ** n #한 변의 길이
    for y in range(l):
        for x in range(l):
            #조각 한 변의 길이로 바꿔서 보내줘야댐 is star or space에 
            print("*" if is_star_or_space(x, y, l // 5) else " ", end ="")
        print()

n = int(input())
star_in_star(n)
        
