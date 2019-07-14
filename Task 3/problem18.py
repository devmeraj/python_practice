newList = ['Hello', 'World', 'in', 'a', 'frame']

lenList = []
for i in newList:
    lenList += [len(i)]

maxEl = max(lenList)

def rectFrame(newList):
    print('*********')
    for l in newList:
        print('* {0:{1}} *'.format(l, maxEl))
    print('*********')


rectFrame(newList)