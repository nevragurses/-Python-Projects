#161044071
#Nevra Gürses

from itertools import combinations #This tool is for taking combination.

#This function is implementation of alteration boxes as bwbw format  for 1. Question in Homework.
def boxes(boxArr):
    helperBoxes(boxArr,1,len(boxArr)-2)   #helper function that does alterating is calling.
    return boxArr

#This is helper function of boxes function for 1. Question in Homework.
def helperBoxes (boxArr,low,high):
    if low>=high:
        return boxArr 
    else:    
        boxArr[low],boxArr[high] = boxArr[high],boxArr[low] # left and right boxes alterating,so in every step bw -- bw format is occuring.
        helperBoxes(boxArr,low+2,high-2) #in every recursive call size is decrese by 4 (2 from start point,2 from end point)


#This function is implementation of finding fake coin in 2. Question for Homework.
def findFakeCoin(coinArr):
    fake= helperFakeCoin(coinArr,len(coinArr)) #helper function that does operation is calling.
    return fake

#This is helper function of findfakecoin function for 2. Question in Homework.
def helperFakeCoin(coinArr,size):
    if size==1:
        return coinArr #returning finded fake coin.
    elif size==2: #if size is 2,coin that amount less one is fake coin.
        middle=(int)(size/2)
        if sum(coinArr[0:middle]) < sum (coinArr[middle: size]):
            return helperFakeCoin (coinArr[0:middle],len(coinArr[middle : size ]))
        else:
            return helperFakeCoin (coinArr[middle:size],len(coinArr[middle : size ]))    
        
    else: #if size is 3 or more,divide coin array 3 part and make recursive call on part that is sum of coin amount less one.
        divided=(int)(size/3)       
        if sum(coinArr[0:divided])==sum (coinArr[divided: 2*divided]):
            return helperFakeCoin (coinArr[2*divided : size],len(coinArr[2*divided : size]))
        elif sum(coinArr[0:divided])<sum (coinArr[divided: 2*divided]):
            return helperFakeCoin (coinArr[0:divided],len(coinArr[0:divided]))
        elif sum(coinArr[0:divided])>sum (coinArr[divided: 2*divided]):    
            return helperFakeCoin (coinArr[divided: 2*divided],len(coinArr[divided: 2*divided]))


#This function is implementation of Insertion Sort for 3. Question in Homework.
counterSwapInsertion=0  #to keep number of swap in insertion sort.
numOfBasicOpInsertion=0 #to keep number of basic operations in insertion sort.
def insertionSort(array):   
    global counterSwapInsertion
    global numOfBasicOpInsertion
    for i in range(1, len(array)): 
        current = array[i] 
        position = i-1
        while position >=0 and current < array[position] : 
                array[position+1] = array[position] 
                counterSwapInsertion+=1
                numOfBasicOpInsertion +=1
                position -=1
        array [position+1] = current 
        numOfBasicOpInsertion+=1
    return array

counterSwapQuick=0  #to keep number of swap in quick sort.
numOfBasicOp=0 #to keep number of basic operations in quick sort.
#This function is implementation of Quick Sort for 3. Question in Homework.
def quickSort(arr,low,high): 
    if low < high: 
        pivIndex = partition(arr,low,high)
        quickSort(arr, low, pivIndex-1) 
        quickSort(arr, pivIndex+1, high) 
    return arr       

#This function is partition part of quick sort.        
def partition(arr,low,high):
    global counterSwapQuick 
    global numOfBasicOp
    up= low
    down = high      
    pivot = arr[low]     
    while up < down :
        while up < high and pivot >= arr[up]:
            numOfBasicOp += 1
            up = up+1
        while pivot < arr[down]:
            numOfBasicOp += 1
            down =down-1
        if up < down :
            arr[up],arr[down]=arr[down],arr[up]  #swaping operation.
            counterSwapQuick += 1
           
    pivotIndex=down #determine new pivot index.
    arr[low],arr[pivotIndex] = arr[pivotIndex],pivot 
    counterSwapQuick += 1
                    
    return pivotIndex

#This function is implementation of finding median  for 4. Question in Homework.
def findMedian (arr):
    sortedArray = insertionSort(arr) #for sorting elements,calling insertion sort that is a decrease and conquer algorithm.
    length = len (arr)
    midd=(int)(length/2)
    if length % 2 ==  0 :  #if size is even,median is (middle 2 element / 2)
        median =  (sortedArray[(int)((length/2) -1)] + sortedArray[midd] )/ 2 
    else: #if size is odd,median is middle element.
        median = sortedArray[ midd ]  

    return median

#This function is finding optimal sub-array  for 5. Question in Homework.
def optimalArr(arr):
    value= (min(arr)+max(arr) )*len(arr)/4 
    i=1
    j=0
    comblist = []
    while i<=len(arr): 
        comb = list (combinations(arr, i) ) #takes combination for each i.
        while j<len(comb):
            if  sum(comb[j])>= value:
                comblist.append(comb[j]) #sub-arrays list that are satisfy the condition SUM(B)>=(𝑚𝑎𝑥(𝐴) + 𝑚in(A)) x n/4
            j+=1
        i+=1
        j=0

    last=len(comblist)-1
    result=exhaustiveSearch(comblist,last,multElements(comblist[last]),comblist[last])
    return result

#This is exhaustive search function that finds optimal sub-array in sub-arrays lists that are satisfy the condition.          
def exhaustiveSearch(combArr,n,optimalMult,optimalArr):
    multResult = multElements(combArr[n])
    if multResult <= optimalMult:
        optimalMult=multResult
        optimalArr=combArr[n]
    if n==0 :
        return optimalArr
    else:
        return exhaustiveSearch(combArr,n-1,optimalMult,optimalArr) #recursive calling for another sub-array searching.

# This function is multiplication of items in the one subarray.  
def multElements (combArr) :
    mult=1
    i=0
    while i<len(combArr):
        mult=mult*combArr[i]   
        i+=1  
    return mult


#This is driver function to test all parts in homework.
def driver ():
    print("-------Testing boxes alternate in a black-white-black-white pattern function for 1. Question in Homework ------- ")
    boxArray = ["B","B","B","B","W","W","W","W"]
    print ("Before alterating: ", boxArray)
    print ("After alterating: ", boxes(boxArray))
    print ("\n")
    boxArray2 = ["B","B","B","W","W","W"]
    print ("Before alterating: ", boxArray2)
    print ("After alterating: ", boxes(boxArray2))

    print("\n-------Testing find fake coin function for  2. Question in Homework ------- ")
    arrfake =[2,1,2,2,2]
    print("Coin array:" , arrfake)
    print("Returning fake coin: " , findFakeCoin(arrfake))

    print("\n-------Testing Insertion Sort function for  3. Question in Homework ------- ")
    arr = [12,11,8,5,1,3,6,2,4,7,9] 
    #arr = [10,5,8,6,1,7,3,2,4,9]
    print("Before Sorting: ",arr)
    print("After sorting: ", insertionSort(arr))
    print("Number of basic operations in insertion sort for " , len(arr), " elements is: ", numOfBasicOpInsertion)
    print("Number of swap operations in insertion sort for " , len(arr), " elements is: ", counterSwapInsertion)


    print("\n-------Testing Quick Sort function for  3. Question in Homework ------- ")
    #arr = [10,5,8,6,1,7,3,2,4,9]
    arr = [12,11,8,5,1,3,6,2,4,7,9] 
    n = len(arr)
    print("Before Sorting: ",arr)
    print("After sorting: ", quickSort(arr,0,n-1 ))
    print("Number of basic operations in quick sort for " , len(arr), " elements is: ", numOfBasicOp)
    print("Number of swap operations in quick sort for " , len(arr), " elements is: ", counterSwapQuick)  

    print("\n-------Testing Finding Median function for  4. Question in Homework ------- ")
    arr = [ 9,8,7,6,5,4] 
    print("Given array is: ",arr)
    print("Median is: ", findMedian (arr ))
    arr = [ 5,6,4,3,1] 
    print("Given array is: ",arr)
    print("Median is: ", findMedian (arr ))

    print("\n-------Testing Finding Optimal Sub-Array function for  5. Question in Homework ------- ")
    arr = [2, 4, 7, 5, 22, 11]
    print("Given array is: ",arr)
    print("Optimal sub-array is: ", optimalArr(arr))

driver()