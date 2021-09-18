import os
import time

path = input('Enter path of folder to cleanup: ')
print('Enter threshold age for file deletion')
print('For example, an input of 3 will delete any files older than, and old as 3 days')
threshold = input()

while threshold == '0':
    new_threshold = input('Cannot enter a value of 0, please enter a new value: ')
    if new_threshold != '0':
        threshold = new_threshold
        break

if os.path.exists(path):
    path = path + '/'
    directory_list = os.listdir(path)

for file in directory_list:
    name, ext = os.path.splitext(file)
    age = time.time() - os.stat(path + file).st_ctime

    minutes = age / 60
    hours = age / 3600
    days = age / 86400

    if minutes >= 60:
        if hours >= 24:
            if str(days) >= threshold:
                os.remove(path + file)
                print('files removed')
            else:
                print(name + ext + ' is only ' + str(days) + ' days old')
        else:
            print(name + ext + ' is only ' + str(hours) + ' hours old')
    elif minutes < 1:
        print(name + ext + ' is only ' + str(age) + ' seconds old')
    else:
        print(name + ext + ' is only ' + str(age / 60) + ' minutes old')