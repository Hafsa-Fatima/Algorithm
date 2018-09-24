import time

# Quick sort function 
def quickSort(a,start,end): 

    # start is starting index 
    # end is last index 
    if start < end: 
        # p is pivot index
        p = partition(a,start,end) 
        #call quicksort recursively
        quickSort(a, start, p-1) 
        quickSort(a, p+1, end) 

# Partion function
def partition(a,start,end): 

    i = ( start-1 )    
    #assign last index array item as pivot    
    pivot = a[end]      
    for j in range(start , end): 
        if   a[j] <= pivot: 
            i = i+1 
            #swap ith and jth items
            a[i],a[j] = a[j],a[i] 
    #swap the pivot to its correct position
    a[i+1],a[end] = a[end],a[i+1] 
    return ( i+1 ) 

# main function
def main():

    a = list()
    #input size of array from the user 
    print("Choose a size of array : ") 
    n=input()
    
   
    for i in range(0,int(n)):
        #generating sorted ascending order array
        a.append(i)

     #CPU start time
    stime=time.clock()
    quickSort(a,0,int(n)-1) 
    #CPU end time
    etime=time.clock()
    print ("QuickSort result is:") 
    #for i in a: 
     #   print (i,end=' ') 
    #Total time complexity
    Ttime=etime-stime
    print()
    print("computation time = "+str(Ttime))

#call main function
if __name__ == "__main__":
  main()