from os import walk
import sys
import data
import os


def print_ratio(ratio):
    times = len(payload)
    print '[*]got ratio :'
    print '\t',
    for i in range(times):
        print str(i) + '\t',
    for i in range(times):
        print ''
        print str(i) + '\t',
        for j in range(times):
            print str(ratio[i][j]) + '\t',




if __name__=="__main__":
    
    binary_file = sys.argv[1]
    exp_file = sys.argv[2]
    times = int(sys.argv[3])
    payload = data.get_payload(binary_file,exp_file,times=times)
    ratio = data.rat(payload)
    print_ratio(ratio)
