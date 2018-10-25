import time
import sys
#Global declaration
substr='' 
index=[]

#formation of Longest repeating subsequence matrix
def LRSMatrix(s,n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if s[i-1]==s[j-1] and i!=j:
                matrix [i][j]= 1+ matrix [i-1][j-1]
            else:
                matrix [i][j] = max(matrix[i-1][j],matrix[i][j-1])
    

#retracing the LRS Matrix to get Longest repeating subsequence
def LRS(s,m,n):
    global substr
    global index
    #base case
    if (m==0 or n==0):
        #print the LRS output 
       return 
    # check for nonoverlapping conditions
    if (s[m-1]==s[n-1] and m!=n and m-1 not in index and n-1 not in index):
        index.append(n-1)
        index.append(m-1)
        substr=substr+s[m-1]
        return LRS(s,m-1,n-1)
    else:
        if(matrix[m-1][n]>matrix[m][n-1]):
            return LRS(s,m-1,n)
        else:
            return LRS(s,m,n-1)

# check format of input
if len(sys.argv)==2 :
    # input from commandline
    s=sys.argv[1]
    n = int(len(s))
    # create a n+1 by n+1 matrix with all initial data as zeroes
    matrix = [[0 for i in range(n+1)] for j in range(n+1)] 
    # start time
    stime=time.clock()
    LRSMatrix(s,n)
    LRS(s,n,n)
    # end time
    print("Output= "+substr[::-1])
    etime=time.clock()
    tTime=1000*(etime-stime)
    print("Time taken = "+str(tTime)+" milliseconds")
else:
    print("invalid input")
