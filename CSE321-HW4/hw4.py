# AUTHOR: NEVRA GÜRSES
# NO : 161044071

#This function for first question in homework.
# Converts a 2D array into the special array only if it can be done with changing one single element in the array
def convert2DtoSpecial(arr): 
    for i in range(len(arr)-1):
        for j in range(len(arr[i])-1):
            if arr[i][j]+arr[i+1][j+1]>arr[i][j+1]+arr[i+1][j]:
                arr[i][j+1]=arr[i][j+1]+(arr[i][j]+arr[i+1][j+1]-(arr[i][j+1]+arr[i+1][j]))

    return arr

# This below 2 function for implementing merge sort.
# These are helper functions.Merge sort is using in another functions in homework.
def merge(arr,leftArr,rightArr):   #For merging arrays.
        i = j = k = 0
        while i < len(leftArr) and j < len(rightArr): 
            if leftArr[i] < rightArr[j]: 
                arr[k] = leftArr[i] 
                i+=1
            else: 
                arr[k] = rightArr[j] 
                j+=1
            k+=1
        # Checking whether there are any element was left or not. 
        while i < len(leftArr): 
            arr[k] = leftArr[i] 
            i+=1
            k+=1
         # Checking whether there are any element was rigth or not.  
        while j < len(rightArr): 
            arr[k] = rightArr[j] 
            j+=1
            k+=1
def mergeSort(arr):
    if(len(arr)>1):
        middle=(int)(len(arr)/2) #middle point
        left=arr[0:middle]  #left part of array.
        right=arr[middle : len(arr)]  #left part of array.
        mergeSort(left)
        mergeSort(right)
        merge(arr,left,right)
    return arr 

#This function is for finding the leftmost minimum element in each row in 1. Question of Homework.
#In this function I used merge sort for sorting each row.So this function is divide and conquer algorithm.
def leftMostMinimum(array):
    i=0 
    for row in array:
        print(" leftmost min element in ",i,". row is ", (mergeSort(row)[0])) #After sorting leftmost min element is first elemet of each row.
        i+=1 
# This function  for finding  the kth element of the merged array of given two sorted arrays.
def kthElement(arrA, arrB, k):
    if not arrA:
        return arrB[k]
    if not arrB:
        return arrA[k]
    midIndexA=len(arrA) // 2  # middle index of array A. 
    midIndexB = len(arrB) // 2   # middle index of array B. 
    midElemA =arrA[midIndexA]   # middle element of array A. 
    midElemB= arrB[midIndexB] # middle element of array B. 

    # when k is bigger than  sum of median indices of array A and array B.
    if midIndexA  +  midIndexB < k:
        # if  median  of array A is bigger than median of array B ,  first half of array B doesn't include k.
        if midElemA > midElemB:
            return kthElement(arrA, arrB[midIndexB + 1:], k - midIndexB - 1)   
        else:
            return kthElement(arrA[midIndexA + 1:], arrB, k - midIndexA - 1)
    #when k is smaller than  sum of median indices of array A and array B.
    else:
        # if  median  of array A is bigger than median of array B , second half of array A doesn't include k.
        if midElemA > midElemB:
            return kthElement(arrA[:midIndexA], arrB, k)
        else:
            return kthElement(arrA, arrB[:midIndexB], k)             
 
#This function for find the maximum possible sum in array.This is a helper function for maxSumSubArray function in 3. Question in Homework.
def leftAndRightSum(arr, left, mid, h,maxSubArr) :    
    # for including elements on left part of middle point of array. 
    total = 0
    leftSum =  float('-inf')
    i=mid  
    for i in range(mid, left-1, -1) : 
        total +=  arr[i] 
        if (total > leftSum) :
            leftSum = total 
            maxSubArr.append(arr[i])
    # for including elements on right part of middle point of array. 
    total = 0 
    rightSum =  float('-inf')
    i=mid+1
    for i in range(mid + 1, h + 1) : 
        total = total + arr[i] 
          
        if (total > rightSum) : 
            rightSum = total
            maxSubArr.append(arr[i])
               
    # Return sum of elements on left part  and right part  of middle point. 
    return leftSum + rightSum

#This function for finding  a contiguous subset that having the largest sum in 3. Question of homework.
def maxSumSubArray(arr, low, high) : 
    maxSubArr=[]  #This array for keep  sub array  that has largest sum.

    if (low == high) : #base case
        return arr[low], 
  
    middle = (low + high) // 2 #middle point.
 
    return max( maxSumSubArray(arr, low, middle)[0], 
                maxSumSubArray(arr, middle+1, high)[0], 
                leftAndRightSum(arr, low, middle, high,maxSubArr)),maxSubArr
                
# This function is helper function of isBipartite function for 4. Question in homework. 
#This is for coloring graph for controlling.
# -1 is for no assigned,1 assigned first color,0 assigned 2. color. 
def colorGraph(graph, colorArr, pos, firstColored,vertex):  
    if colorArr[pos] != -1 and colorArr[pos] != firstColored:  
        return False 
    # color this pos as c and all its neighbours and 1-c  
    colorArr[pos] =  firstColored  
    ans = True 
    i=0
    while(i<vertex): 
        if graph[pos][i]:  
            if colorArr[i] == -1:  
                ans = ans & colorGraph(graph, colorArr, i, 1- firstColored,vertex)  
                  
            if colorArr[i] !=-1 and colorArr[i] != 1-firstColored:  
                return False    
        if not ans:  
            return False 
        i+=1
    return True 
#This function is finding a graph is bipartite or not in 4. Question in homework.
# It uses helper function colorGraph for coloring graph.   
def isBipartite(graph,vertex):  
    colorArr = [-1] * vertex         
    pos = 0  
    return colorGraph(graph, colorArr, pos, 1,vertex)  
    
#This function for finding  best day to buy the goods for 5. Question in Homework.
# In this function I used merge sort that is divide and conquer algorithm for finding max gained day by sorting gains of days. 
def bestDay(cost,price):
    gain=[None]*(len(price)-1) #For keep gain of each day.
    gainDay=[None]*(len(price)-1) #For keep days for each gain.
    i=0
    while i<len(price)-1: #This loop for determining gains according to price and cost.
        gain[i]=price[i+1]-cost[i]   
        gainDay[i]=price[i+1]-cost[i]   
        i+=1   
    print("\nGain array that is found in function:")
    print(gain) 
    mergeSort(gain) #Calling merge sort for sorting gains.
   
    print("\nMax gain is:" ,max(gain)) #Max gain is
    print("Best day to buy goods:",gainDay.index(max(gain))+1) #Best day is max gain after sorted.

#This function for printing array on screen.
def printArr(arr): 
    for i in range(len(arr)):         
        print(arr[i],end=" ") 
    print()

#This is  driver function for testing all functions.   
def driver ():
    print("\n-------Testing for converting a 2D array into the special array  for 1. Question in Homework ------- ")
    arr=[[37,23,22,32],[21,6,7,10],[53,34,30,31],[32,13,9,6],[43,21,15,8]]
    print("\nBefore changing 2d Array is :",arr)
    print("\nAfter 2d Array is:",convert2DtoSpecial(arr))
    print("\n-------Testing  for  finding leftmost minimum element in each row for 1. Question in Homework ------- ")
    arr= [[10, 17, 13, 28,23], [17, 22,16,29,23], [24, 28, 22, 34,24], [11,13,6,17,7], [45,44,32,37,23], [36,33,19,21,6], [75,66,51,53,34]]
    print("\n2d Array is :",arr)
    leftMostMinimum(arr)
    print("\n-------Testing for finding the kth element of the merged arrays for 2. Question in Homework ------- ")
    arrA=[2,8,9,12]
    arrB=[1,3,5,11 ]
    print ("Array A is:")
    printArr(arrA)
    print ("\nArray B is:")
    printArr(arrB) 
    k=1
    print ("\n")
    while  k<= len(arrA)+len(arrB):
        print (k , "th element is: " ,kthElement(arrA, arrB, k-1))
        k+=3
    print("\n-------Testing for finding contiguous subset that having the largest sum for 3. Question in Homework ------- ")
    arr = [5, -6, 6, 7, -6, 7, -4, 3]
    print ("\nArray is:")
    printArr(arr)
    n = len(arr) 
    max_sum = maxSumSubArray(arr, 0,n-1)[0] 
    arr=maxSumSubArray(arr, 0,n-1)[1] 
    print("\nContinious subset having the largest sum :", arr, "Whose sum is:" ,max_sum) 
    print ("\nArray is:")
    arr=[-2, -3,4,-1,-2,1,5,-3 ]
    printArr(arr)
    n = len(arr) 
    max_sum = maxSumSubArray(arr, 0,n-1)[0] 
    arr=maxSumSubArray(arr, 0,n-1)[1] 
    print("\nContinious subset having the largest sum :", arr, "Whose sum is:" ,max_sum) 
    print("\n-------Testing for checking whether a given graph is a bipartite graph or not for 4. Question in Homework ------- ")
    graph = [[0, 1, 0, 0, 0, 1],
            [1, 0, 1, 0 ,0 ,0],
            [0, 1 ,0, 1, 0, 0],
            [0, 0, 1, 0 ,1 ,0],
            [0 ,0, 0, 1, 0, 1],
            [1, 0, 0, 0, 1 ,0]]
      
    if isBipartite(graph,6):
         print("\nYes,This graph is bipartite.")  
    else: print("\n No,This graph is not bipartite.")   

    print("\n-------Testing for finding  best day to buy the goods for 5. Question in Homework. ------- ")
    cost=[5,11,2,21,5,7,8,12,13,0]
    price=[0,7,9,5,21,7,13,10,14,20]
    print ("\nCost array is:")
    printArr(cost)
    print ("\nPrice array is:")
    printArr(price)

    bestDay(cost,price)
      

driver()