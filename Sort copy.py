###############################################
# have to confess, mb 'with open' is a better choice for this
# well, dont mind that
#     - form 'stupid' Linzh
###############################################
import sys

def swap(a=[]): # def a swap function
    for i in range(len(a)):
        tmp = a[i][0]
        a[i][0] = a[i][1]
        a[i][1] = tmp

# open users dict, modify file name as urs
with open("./flypy_user.txt", "w+") as f:
    data = f.readlines()
    dicts = []  # init output dict
    for i in range(len(data)):  # read and detect which line is suppose to be cp to new file
        if ('#' in data[i]) or (data[i] == '\n'):
            continue
        tmp = data[i].split()
        if len(tmp) == 1:
            continue
        dicts.append(tmp)
    swap(dicts)   # prepare for sort
    dicts.sort()  # sort!
    swap(dicts)   # return to row order
    for i in range(len(dicts)): # then format into the official form of Rime & write this into new file
        print("{}\t{}".format(dicts[i][0], dicts[i][1]), file=f)
