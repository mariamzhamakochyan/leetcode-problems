def arr(num1, m, num2, n):
    while n > 0 and m > 0:
        l = m+n-1
        if num1[m -1] > num2[n-1]:
            num1[l] = num1[m-1]
            m-=1
        else:
            num1[l] = num2[n-1]
            n -=1
            l -=1
    while n > 0:
        num1[l] = num2[n-1]
        l -= 1
        n -=1
    return num1
num1 = [1,2,3,0,0,0]
m = 3
num2 = [2,5,6]
n = 3
print(arr(num1, m, num2, n))
