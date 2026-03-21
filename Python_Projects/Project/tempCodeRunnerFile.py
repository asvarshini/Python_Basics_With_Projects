fi = open("File.txt", 'r')#opening file
contents = fi.read()      #Read whole file
print("Output using read():")
print(contents)
fi.close() #closing file