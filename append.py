data=input("enter some text to write to the file: ")
file=open("output.txt","w")
file.write(data)
file.close()

more_data=input("enter some text to append to the file: ")
file=open("output.txt","a")
file.write(more_data)
file.close()

print("final content of the file: ")
file=open("output.txt","r")
print(file.read())
file.close()