def fib(n):
    zeros = [0] * (n + 1)
    ones = [0] * (n + 1 )

    zeros[0] = 1 #0일때 1 호출
    ones[1] = 1 #1일때 1 호출출

    for i in range(2, n+1):
        zeros[i] = zeros[i-1] + zeros[i-2] #0, 1 호출횟수도 피보나치 수열처럼 숫자 계산될거임
        ones[i] = ones[i-1] + ones[i-2] #왜냐하면 피보나치 수열 자체가 그런 방식으로 합해서 계산되니까
        #최종적으로는 0이랑 1 호출횟수도 같은 방식 따라갈듯

    return zeros, ones
    
t = int(input())
tests= []

for i in range(t):
    tests.append(int(input()))

max_n = max(tests)
zeros, ones = fib(max_n+1)
for i in tests:
    print(zeros[i], ones[i])