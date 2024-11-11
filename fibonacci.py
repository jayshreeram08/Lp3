def fibonacci(n):
    stepCount = 0
    if n==0:
        stepCount +=1
        return 0, stepCount
    elif n==1:
        stepCount +=1
        return 1, stepCount
    
    a,b = 0,1
    stepCount +=2
    
    for _ in range (2,n+1):
        a,b = b,a+b
        stepCount += 2
    
    stepCount +=1
    return b,stepCount
    
n=int(input("Enter the fibonacci term to find : "))
fib_no,steps = fibonacci(n)
print(f"Fibonacci({n}) = {fib_no}")
print(f"Step Count = {steps}")
