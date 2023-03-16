import sys
def next_smallest(num):
    for i in range (num+1,sys.maxsize):
        if str(i)==str(i)[::-1]:
            return i
print (next_smallest(99))
print(next_smallest(1221))
