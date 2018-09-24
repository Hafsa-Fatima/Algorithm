import time
# Quick sort function 
def quickSort(A,start,end): 

    if start < end: 

        # p is pivot index
        p = partition(A,start,end) 

        #call quicksort recursively
        quickSort(A, start, p-1) 
        quickSort(A, p+1, end) 

# Partion function
def partition(A,start,end): 

    #assign last index array item as pivot    
    pivot = A[end]      
    i = ( start-1 )

    for j in range(start , end): 
        if   A[j] <= pivot: 
            i = i+1 

            #swap ith and jth items
            A[i],A[j] = A[j],A[i]

    #swap the pivot to its correct position
    A[i+1],A[end] = A[end],A[i+1] 

    return ( i+1 ) 

# main function
def main():

    #input size of array from the user 
    print("Choose A size of array : ") 
    n=input()

    print("enter array items: ")  
    for i in range(0,int(n)):
        j=input()
        A.append(int(j))

    #CPU start time
    stime=time.clock()

    quickSort(A,0,int(n)-1) 

    #CPU end time
    etime=time.clock()

    print ("QuickSort result is:") 
    print(A)
    
    #Total time complexity
    Ttime=etime-stime
    print("computation time = "+str(Ttime))

#call main function
A = list()
if __name__ == "__main__":
  main()