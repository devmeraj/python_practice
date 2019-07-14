#Write a Python program to append text to a file and display the text.

with open('test.txt', 'a+') as myFile:
    myFile.write('\nThis is a new Line.')
    myFile.seek(0)
    print(myFile.read())