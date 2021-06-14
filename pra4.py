memo ={1:1,2:2}
def fibonachi(n):
    if n in memo:
        return memo[n]
   # if (n==1)or(n==2):
    #    return 1
    #return fibonachi(n-2)+ fibonachi(n-1)
    memo[n] =fibonachi(n-2)+ fibonachi(n-1)
    return memo[n]
num =int(input())
print(fibonachi(num))
##practice
