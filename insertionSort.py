n = int(input("Enter number of elements : ")) 
arr = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n] 
def insertionSort(arr):
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 

def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i],end=" ") 
    print() 
  
insertionSort(arr) 
printList (arr)
