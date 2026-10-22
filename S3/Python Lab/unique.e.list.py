n=int(input("enter the elements in list:"))
my_list=[]
for i in range(n):
    elements=int(input(f"enter the element {i+1}:"))
    my_list.append(elements)
unique_elements=[]
for item in my_list:
    if item not in unique_elements:
        unique_elements.append(item)
print("Original List:",my_list)
print("Unique Elements:",unique_elements)