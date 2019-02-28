
import os

def walk(path):
    result= []
    for item in os.listdir(path):
        fullpath =os.path.join(path,item)
        if os.path.isdir(fullpath):
            result.extend(walk(fullpath))
        else:
            result.append(fullpath)

    return result

for item in walk('/Users/jerry.kim/workspaces'):
    print item
