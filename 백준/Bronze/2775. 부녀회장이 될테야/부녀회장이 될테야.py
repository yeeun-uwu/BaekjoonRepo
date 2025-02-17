def numOfPeople(k, n):
    start = [[_+1 for _ in range(n)]]

    for i in range(1, k+1):
        start.append([])
        for j in range(n):
            start[i].append(sum(start[i-1][:j+1]))
    
    print(start[k][n-1])

#0층은 1호 1명, 2호 2명, 3호 3명...
#1층은 1호 1명, 2호 3명, 3호 6명, 4호 10명, ...
#2층은 1호 1명, 2호 4명, 3호 10명, 4호 20명, ...


t = int(input())

for i in range(t): # test case만큼 반복
    k= int(input())
    n = int(input())
    numOfPeople(k, n)