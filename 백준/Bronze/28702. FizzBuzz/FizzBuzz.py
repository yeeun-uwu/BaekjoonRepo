def Fizzbuzz(lists):
    ans = 0
    for i in range(3):
        if lists[i].isdigit():
            ans = int(lists[i]) + (3-i)

    if ans % 3 == 0 and ans % 5 == 0:
        return "FizzBuzz"
    elif ans % 3 == 0:
        return "Fizz"
    elif ans % 5 == 0:
        return "Buzz"
    else:
        return ans

        
#연속해서 3번 숫자없이 나오는 경우는 없는듯. 


strs = []
for i in range(3):
    strs.append(input())

print(Fizzbuzz(strs))