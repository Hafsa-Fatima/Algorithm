import time
import sys
import math

#Global declaration
substr=''

#  Longest repeating subsequence
def LRS(s,n):
    global substr
    # total number of subsequence
    t_Subseq = int( (math.pow(2, n)))
    a=[]
    a_ind=[]
    l=0
    for counter in range(0, t_Subseq): 
        subseq=''
        ind=[]
        for j in range(0, n): 
            if((counter & (1 << j)) > 0): 
                # generate different subsequence 
                subseq+=s[j]
                ind.append(j)
        # store all subsequence in list a
        a.append(subseq)
        # store the index of subsequence in a_ind
        a_ind.append(ind)
        for c in range(0,counter):
            # check if the sequence repeated
            if a[c]==a[counter] :
                # check if indices non-overlap and next repeating subsequence is longer than previous 
                if common_index(a_ind[c],a_ind[counter])==False and l<int(len(subseq)):
                    l=int(len(subseq))
                    substr=a[counter]
                    
# check overlapping conditions : True if overlap and false if non overlap
def common_index(index1, index2): 
    res = False 
    for x in index1:   
        for y in index2: 
            # if one common 
            if x == y: 
                res = True
                return res                 
    return res

# check format of input
if len(sys.argv)==2 :
    # input from commandline
    s=sys.argv[1]
    n = int(len(s))
    # start time
    stime=time.clock()
    LRS(s,n)
    print("Output =  "+str(substr))
    etime=time.clock()
    tTime=1000*(etime-stime)
    print("Time taken = "+str(tTime)+" milliseconds")
else:
    print("invalid input")