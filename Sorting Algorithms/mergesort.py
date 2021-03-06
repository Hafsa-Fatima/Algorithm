import time
def mergeSort(A):
    if len(A)>1:
        q = len(A)//2
        L = A[:q]
        R = A[q:]

        #recursively calling mergesort 
        mergeSort(L)
        mergeSort(R)

        #merging the subarrays
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

    #merging left and right subarrays
    while i < len(L):
        A[k]=L[i]
        i=i+1
        k=k+1

    while j < len(R):
        A[k]=R[j]
        j=j+1
        k=k+1

def main():

    #input size of array from the user 
    print("Choose a size of array : ") 
    n=input()

    print("enter array items: ")  
    for i in range(0,int(n)):
        j=input()
        A.append(int(j))

    #CPU start time
    stime=time.clock()

    mergeSort(A) 

    #CPU end time
    etime=time.clock()

    print ("MergeSort result is:") 
    print (A) 
    
    #Total time complexity in milliseconds
    Ttime=(etime-stime)*1000

    print("computation time = "+str(Ttime)+" milliseconds")

#call main function
A = list()
if __name__ == "__main__":
  main()