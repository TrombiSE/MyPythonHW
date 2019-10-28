n = int(input("Enter number of elements : ")) 
arr = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n] 
def bubbleSort(arr):
	n = len(arr)
	for i in range(n):
		for j in range(0, n-i-1):
			if arr[j] > arr[j+1] :
				arr[j], arr[j+1] = arr[j+1], arr[j]
def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i],end=" ") 
    print() 
bubbleSort(arr)
printList (arr)
