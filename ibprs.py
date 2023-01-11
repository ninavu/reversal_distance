from cmath import inf
import sys
import math

# this function loads the input file and returns an array of numbers
def load(fileName):
    fin = open(fileName, "r")
    lines = fin.readlines()

    a, l = [], []
    for line in range(len(lines)):
        a = lines[line].strip().split()
        for num in range(len(a)):
            l.append(int(a[num]))

    fin.close()
    return l

# this function turns an array into a string
def to_string(arr):
    s = ""
    for i in range(len(arr)):
        s += str(arr[i]) + " "
    return s

# this function does reversals all segments between k to (k-1)
def reversals(arr, left, right):
    arr[left+1:right+1] = arr[right:left:-1]
    return arr

# this functiion adds breakpoints to the arrays and put increasing and decreasing strips in separate arrays
def breakpoints(arr, fout):
    bp = "|"
    bps, DS, IS = [], [], []

    num = 0
    while (num < len(arr)-1):
        cur = arr[num]
        next = arr[num+1]
        bps.append(cur)
        L1, L2 = [],[]
        while (next - cur == 1):
            bps.append(next)
            if cur not in L1:
                L1.append(cur)
            cur = next
            L1.append(cur)
            num += 1 
            if cur != arr[-1]:
                next = arr[num+1]

        while (cur - next == 1):
            bps.append(next)
            if cur not in DS:
                L2.append(cur)
            cur = next
            L2.append(cur)
            num += 1
            next = arr[num+1]
        
        if bps[-1] != len(arr)-1:
            bps.append(bp)

        # single strips will be put in the dstrip
        if len(bps) > 3:
            if bps[-3] == bp and bps[-1] == bp:
                L2.append(bps[-2])

        num += 1
        IS.append(L1)
        DS.append(L2)
        if bps[-1] == bp and bps[-2] == arr[-2]:
            bps.append(arr[num])        
    return bps, IS, DS

# this function returns the total length of sub-lists of a list
def lenList(arr):
    count = 0
    for i in range(len(arr)):
        count += len(arr[i])        
    return count

# this function returns the smallest number in a list of list
def smallestInt(arr, min):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if min > arr[i][j]:
                min = arr[i][j]
    return min

# this function reverses an increasing strip with the shortest length
def reverseIS(L, arr):
    min = math.inf
    for i in range(len(arr)):
        if len(arr[i]) != 0 and min > len(arr[i]):
            min = len(arr[i])

    begin = L.index(arr[min][0])
    end = L.index(arr[min][-1])
    L[begin:end+1] = L[end:begin-1:-1]
    return L

# this function executes the improved breakpoint reversal sort algorithm 
def ibprs(arr, fout):
    arr.append(len(arr)+1)
    arr.insert(0, 0)
    fout.write("EXTENDING PERMUTATIONS... \n")
    fout.write(to_string(arr) + "\n \n")

    fout.write("ADDING BREAKPOINTS... \n")
    bps = breakpoints(arr, fout)
    bps_list = bps[0]
    bps_count = bps_list.count("|")
    istrip = bps[1]
    dstrip = bps[2]
    fout.write("Number of breakpoints: " + str(bps_count) + "\n")
    fout.write(to_string(bps_list) + "\n \n")

    count = 0
    while (bps_count > 0):
        if lenList(dstrip) != 0:
            num_strip = smallestInt(dstrip, len(arr))
            min_idx = arr.index(num_strip)
            swap_idx = arr.index(num_strip-1)
            if (min_idx > swap_idx):
                arr = reversals(arr, swap_idx, min_idx)
            else:
                arr = reversals(arr, min_idx, swap_idx)
        elif lenList(istrip) != 0:
            arr = reverseIS(arr, istrip)
        
        bps = breakpoints(arr, fout)
        bps_list = bps[0]
        bps_count = bps_list.count("|")
        istrip = bps[1]
        dstrip = bps[2]
        count += 1
        fout.write("Number of breakpoints: " + str(bps_count) + "\n")
        fout.write(to_string(bps_list) + "\n \n")
    fout.write("Reversal distance to the identity permutation: " + str(count) + "\n")
    fout.write("Sorted array: " + to_string(arr[1:-2])  + "\n")
    return arr

def main():
    input = sys.argv[1]
    output = sys.argv[2]
    fout = open(output, "w")
    fout.write("ORIGINAL LIST \n")
    L = load(input)
    fout.write(to_string(L) + "\n")

    fout.write("BEGIN SORTING... \n \n")
    L = ibprs(L, fout)
main()