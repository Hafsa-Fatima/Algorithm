import time

def mergeSort(A,p,r): 
    if p < r: 
  
        q = int((p+(r-1))/2)
        #recursively call merge sort split array until it contain one item
        mergeSort(A, p, q) 
        mergeSort(A, q+1, r) 
        #merge items
        merge(A, p, q, r) 

def merge(A, p, q, r): 
    n1 = q - p + 1
    n2 = r- q 

    L = [0] * (n1) 
    R = [0] * (n2) 

    for i in range(0 , n1): 
        L[i] = A[p + i ] 
  
    for j in range(0 , n2): 
        R[j] = A[q + j + 1] 
  
     
    i = 0     
    j = 0     
    k = p     
  
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            A[k] = L[i] 
            i += 1
        else: 
            A[k] = R[j] 
            j += 1
        k += 1
  
    while i < n1: 
        A[k] = L[i] 
        i += 1
        k += 1
  
    while j < n2: 
        A[k] = R[j] 
        j += 1
        k += 1

def main():

    A = list()
    #input size of array from the user 
    print("Choose a size of array : ") 
    n=input()
    print("enter array items: ")  
    for i in range(0,int(n)):
        j=input()
        A.append(int(j))
    #CPU start time
    stime=time.clock()
    mergeSort(A,0,int(n)-1) 
    #CPU end time
    etime=time.clock()
    print ("MergeSort result is:") 
    for i in A: 
        print (i,end=' ') 
    #Total time complexity
    Ttime=etime-stime
    print()
    print("computation time = "+str(Ttime))

#call main function
if __name__ == "__main__":
  main()