n=int(input("Enter the no.of elements in the list:"))
number=[]
for i in range(n):
    num=int(input(f"Enter the element{i+1}:"))
    number.append(num)
even_numbers=[]
for num in number:
    if num%2==0:
        even_numbers.append(num)
print("Original list:",number)
print("Even number list:",even_numbers)



