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
<<<<<<< HEAD
print(fibonachi(num))

=======
>>>>>>> 8a5b0d3783f5f1b5f265ea136b8824d4b3f21333
