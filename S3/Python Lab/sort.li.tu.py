n=int(input("Enter the no.of tuples:"))
my_list=[]
for i in range(n):
    print(f"Enter the elements of {i+1} tuple:")
    a=int(input("Enter the number:"))
    b=int(input("enter the number:"))
    my_list.append((a,b))
print("The unsorted list is:")
for t in my_list:
    print(t)
for i in range(n):
    for j in range(0,n-i-1):
        if my_list[j][1]>my_list[j+1][1]:
            temp=my_list[j]
            my_list[j]=my_list[j+1]
            my_list[j+1]=temp
print("the sorted list:")
for t in my_list:
    print(t)