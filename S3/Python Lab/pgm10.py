with open("source.txt","r") as f1:
    data1=f1.read()
with open("destination.txt","r") as f2:
    data2=f2.read()
with open("merged.txt","w") as f3:
    f3.write(data1)
    f3.write("\n")
    f3.write(data2)
print("File merged successfully")