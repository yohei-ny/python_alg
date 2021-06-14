#memo ={1:1,2:2}
#def fibonachi(n):
#    if n in memo:
#        return memo[n]
   # if (n==1)or(n==2):
    #    return 1
    #return fibonachi(n-2)+ fibonachi(n-1)
#    memo[n] =fibonachi(n-2)+ fibonachi(n-1)
#    return memo[n]
#num i=int(input())
#print(fibonachi(num))
##practice


def fibonachi(n):
    fib =[1,1]
    for i in range(2,n):
        fib.append(fib[i-2]+fib[i-1])
    return fib[n-1]

num =int(input())
print(fibonachi(num))



