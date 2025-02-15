for i in range(1, 101):
    ans = i ** 3
    for j in range(2, 101):
        a = j * j * j
        for p in range(j+1, 101):
            b = p * p * p 
            for q in range(p+1, 101):
                c = q * q * q
                if ans == a + b + c:
                    print("Cube = {}, Triple = ({},{},{})".format(i, j, p, q))
                if ans < a+b+c:
                    break