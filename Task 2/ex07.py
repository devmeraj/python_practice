#fileName = input('Type a file name with it\'s extension. ')

#print(fileName[fileName.find('.')+1:])

filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))