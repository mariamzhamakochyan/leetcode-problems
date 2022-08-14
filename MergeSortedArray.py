def mergeSort(num1, m, num2, n):
    while m >= 0 and n >= 0:
        if num1[m -1] >= num2[n - 1]:
            num1[m + n - 1] = num1[m - 1]
            m -= 1
        else:
            num1[m + n - 1] = num2[n - 1]
            n -= 1
    for i in range(0, n):
        num1[i] = num2[i]
    return num1
    
num1 = [1,2,3,0,0,0]
num2 = [2,5,6]
m = 3
n = 3
print(mergeSort(num1, m, num2, n))
