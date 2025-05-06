def tower_ans(n):
    if n == 2:
        return 3
    
    return tower_ans(n-1) * 2 + 1

def towers(n, str, btw, end):
    if n == 1:
        print(f"{str} {end}")
        return 
    towers(n-1, str, end, btw) 
    #n-1을 사이로 옮기고
    print(f"{str} {end}")
    #맨 밑 판 옮기고
    towers(n-1, btw, str, end)
    #나머지 사이에서 도착점으로 옮김  
    

n = int(input())
print(tower_ans(n))

if n <= 20:
    towers(n, 1, 2, 3)