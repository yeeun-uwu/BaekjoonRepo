def calc(n, k):
    round = [i for i in range(1, n+1)] #사람들 숫자로 리스트 생성
    i = 0
    ans = []
    for _ in range(n-1):
        i = (i + k - 1) 
        while i >= len(round):
            i -= len(round)
        #print(i)
        ans.append(round.pop(i))
    ans.append(round.pop())
    return ans


n, k = map(int, input().split())
answer = calc(n, k)
print("<"+ ", ".join(map(str, answer))+">")