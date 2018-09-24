import time
import sys
sys.setrecursionlimit(10000)
def mergeSort(A):
    if len(A)>1:
        q = len(A)//2
        L = A[:q]
        R = A[q:]

        #recursively calling mergesort 
        mergeSort(L)
        mergeSort(R)
        merge(A,L,R)

def merge(A,L,R):
    i=0
    j=0
    k=0
    
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            A[k]=L[i]
            i=i+1
        else:
            A[k]=R[j]
            j=j+1
        k=k+1

    while i < len(L):
        A[k]=L[i]
        i=i+1
        k=k+1

    while j < len(R):
        A[k]=R[j]
        j=j+1
        k=k+1

def main():
 
    for size in range(1000,2001,500):
        A = [x for x in range(size)]
        #CPU start time
        stime=time.time()

        mergeSort(A) 

        #CPU end time
        etime=time.time()
        Ttime=etime-stime

        print("Time taken for array size = "+str(len(A)))
        print("computation time = "+str(Ttime)+" seconds")

#call main function
A = list()
if __name__ == "__main__":
  main()