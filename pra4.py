def fibonachi(n):
    if (n==1)or(n==2):
        return 1
    return fibonachi(n-2)+ fibonachi(n-1)

num =int(input())
print(fibonachi(num))
