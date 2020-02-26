import os

path = r'/Volumes/三星 1T/moving/z/'
print(os.listdir(path))
a = 0
for i in os.listdir(path):
    if i.startswith('.'):
        os.remove(path + i)
for i in os.listdir(path):
    os.rename(path + i, path + 'z%s.mp4' % (str(a).zfill(4)))
    a += 1
