###############################################
# have to confess, mb 'with open' is a better choice for this
# well, dont mind that
#     - form 'stupid' Linzh
###############################################

import sys

# def a swap function


def swap(a=[]):
    for i in range(len(a)):
        tmp = a[i][0]
        a[i][0] = a[i][1]
        a[i][1] = tmp


# open users dict, modify file name as urs
f1 = open("./flypy_user.txt", "r")
f2 = open("./flypy_user_out.txt", "w")

data = f1.readlines()

# init output dict
dicts = []

# read and detect which line is suppose to be cp to new file
for i in range(len(data)):
    if ('#' in data[i]) or (data[i] == '\n'):
        continue
    dicts.append(data[i].split())

# prepare for sort
swap(dicts)

# sort!
dicts.sort

# then format into the official form of Rime & write this into new file
for i in range(len(dum)):
    print("{}\t{}".format(dum[i][0], dum[i][1]), file=f2)

# close file r&w
f1.close()
f2.close()
