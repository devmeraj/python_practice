#  Write a Python program to read first n lines of a file

def readLine(fileName, nLine):
    with open(fileName, 'r') as myFile:
        for i in range(1, nLine + 1):
            print(myFile.readlines(i)[0], '\n')


readLine('test.txt', 4)