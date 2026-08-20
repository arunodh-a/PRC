m=int(input("Enter the starting number(m):"))
n=int(input("Enter the ending number(n):"))
squares_set={i*i for i in range(m,n+1) if i%2==0}
print("The square of numbers b/w",m,"&",n,":",squares_set)