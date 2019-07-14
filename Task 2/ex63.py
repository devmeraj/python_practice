import os.path, time
open('test.txt', 'w')
print('Last modified: %s' % time.ctime(os.path.getmtime('test.txt')))
print('Created: %s' % time.ctime(os.path.getctime('test.txt')))