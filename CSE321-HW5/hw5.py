#NEVRA GÜRSES
#161044071

#This function turns the cost of an optimal plan in Question-1 in Homework.
def optimalPlan(NY,SF,m,n):
    optNY = [0] * n
    optSF=[0]*n
    optNY[0]=NY[0]
    optSF[0]=SF[0]
    i=1
    while i < n:
        optNY[i]=NY[i]+ min(optNY[i-1],m+optSF[i-1])
        optSF[i]=SF[i]+ min(optSF[i-1],m+optNY[i-1]) 
        i=i+1
    result=(min(optNY[n-1],optSF[n-1]))
    return  result

# This function finds the optimal list of sessions with the maximum number of sessions Question-2 in Homework.
def selectSession(start,finish,size ): 
    optimalList = []  #for optimal list of sessions.
    i = 0
    optimalList.append(i) #first activity is selected.
    for j in range(size): 
        if start[j] >= finish[i]: 
            optimalList.append(j)
            i = j 
    return optimalList
#Function for  check whether there is a subset with the total sum of elements equal to zero or not for Question-3 in Homework.
maxSum= 50
size = 25 
subsetArr= [ [0]*(maxSum) for _ in range(size)]
visit= [ [0]*(maxSum) for _ in range(size)]      
def zeroSumSubset(i,j, arr) :    
    n=len(arr)  
    if (i == n) : # Base cases
        if (j == 0) : 
            return 1 
        else : 
            return 0     
    if (visit[i][j + size]) : 
        return subsetArr[i][j + size]    
    visit[i][j + size] = 1  
    subsetArr[i][j + size ] = (zeroSumSubset(i + 1, j + arr[i], arr) + zeroSumSubset(i + 1, j, arr))  
    return subsetArr[i][j + size]
      
#This function finds  an alignment between two strings with minimum cost in Question-4 in Homework.
def alignment(str1,str2,missMatch,gap,match) :
    i=j=0   
    m = len (str1)
    n = len(str2)   
    alignmentArr= [ [0]*(m+n+1) for _ in range(n+m+1) ]
    i=0
    while i<=n+m:
        alignmentArr[i][0] = i * gap
        alignmentArr[0][i] = i * gap 
        i=i+1    
    i=1
    while i<=m:
        j=1
        while j<=n:
            if str1[i - 1] == str2[j - 1]:
                alignmentArr[i][j] = alignmentArr[i - 1][j - 1] +match
            else:
                alignmentArr[i][j] = max(alignmentArr[i - 1][j - 1] + missMatch ,alignmentArr[i - 1][j] + gap , alignmentArr[i][j - 1] + gap )  
            j=j+1
        i=i+1

    i = m 
    j = n          
    length = n + m  

    resX=[0]*(length+1)
    resY=[0]*(length+1)
      
    posX = length
    posY = length 
  
    while (not (i==0 or j==0)):
        if str1[i - 1] == str2[j - 1]:
            resX[posX]=str1[i-1]
            posX=posX-1 
            resY[posY] = str2[j-1]
            posY=posY-1
            i=i-1 
            j=j-1 
        elif alignmentArr[i - 1][j - 1] + missMatch == alignmentArr[i][j] :
            resX[posX] = str1[i-1]
            posX=posX-1
            resY[posY] = str2[j-1]
            posY=posY-1
            i=i-1
            j=j-1
        elif alignmentArr[i - 1][j] + gap == alignmentArr[i][j]: 
            resX[posX] = str1[i - 1]
            posX=posX-1
            resY[posY] = '_'
            posY=posY-1
            i=i-1
        elif alignmentArr[i][j - 1] + gap == alignmentArr[i][j]:
            resX[posX] = '_'
            posX=posX-1
            resY[posY] = str2[j-1] 
            posY=posY-1
            j=j-1
    while posX > 0 :
        if i > 0:
            i=i-1
            resX[posX] = str1[i] 
            posX=posX-1 
        else :
            resX[posX] = '_'
            posX=posX-1      
    while posY > 0: 
        if j > 0:
            j=j-1
            resY[posY] = str1[j]
            posY=posY-1
        else:
            resY[posY]='_' 
            posY=posY-1
   
    identity = 1
    for i in range(length,0,-1):
        if(resX[i]=='_' and resY[i]== '_'):
            identity=i+1
            break
   
    end= min(len(str1),len(str2))       
    cost=calculateCost(resX,resY,identity,length,end)
    i=j=identity
    while i<=length:
        i=i+1
    print(" ")          
    while j<=length:
        j=j+1
    print("\n")
   
    print("The cost is:",cost)
#This function for calculating max cost  in Question-4 in Homework.This is helper function for alignment function.
def calculateCost(str1,str2,identity,length,end):
    cost=0
    count=0
    i=identity
    while i<=length:
        print(str1[i],end='') 
        i=i+1
    print(" ")    
    i=identity   
    while i<=length:
        if(count!=end):
            print(str2[i],end='')
            if(str1[i]!='_' and str2[i]!='_' ):
                if str1[i]!=str2[i]:
                    cost=cost-2 #for unmatching.
                else:
                    cost=cost+2 #for matching.
                count=count+1      
            else:
                cost=cost-1 #for gap.
        i=i+1
    return cost 


#This function  to calculate the sum of the array with the minimum number of operations  for Question-5 in Homework.
def ancientSystem(arr):
    n=len(arr)
    minFirst=min(arr)
    arr.remove(minFirst)
    minSecond=min(arr)
    arr.remove(minSecond)
    temp=minFirst+minSecond
    total=temp
    operation=total
    i=n-1
    while i>=2:
        minimum=min(arr)
        total=total+minimum
        arr.remove(minimum)
        operation=operation+total
        i=i-1 
    return operation
#arr=[7,8]
           

#This is  driver function for testing all functions.   
def driver ():
    print("\n-------Testing for cost of an optimal plan for Question-1 in Homework------- ")
    NY= [1,3,20,30]
    SF=[50,20,2,4]
    print ("NY Costs: ",NY)
    print ("SF Costs: ",SF)
    print ("Cost of optimal plan is:",optimalPlan(NY,SF,10,len(NY)))
    print("\n-------Testing for  maximum number of sessions for Question-2 in Homework------- ")
    start = [1, 3, 0, 5, 8, 5] 
    finish = [2, 4, 6, 7, 9, 9] 
    print("Optimal sessions list is:",selectSession(start, finish,6) )
    print("\n-------Testing to check whether there is a subset that is sum of elements equal to zero for Question-3  ------- ")
    arr = [ 2, 2, 2, -4, -4 ] 
    print ("Array is: ",arr)
    if(zeroSumSubset(0, 0, arr)>1):
        print("Found a subset with the total sum of elements equal to zero.")     
    else:
        print("Not found a subset with the total sum of elements equal to zero. ")    
    print("\n-------Testing for string alignment cost  for  Question-4 in Homework------- ")
    missMatch=-2
    gap=-1
    match=2    
    alignment("ALIGNMENT","SLIME",missMatch,gap,match)   
    print("\n-------Testing for the sum of the array with the minimum number of operations for Question-5 in Homework------- ")
    arr=[30,3,10,9,2,8]
    print("Integer Array is: ", arr)
    print("Minimum number of operation is: ",ancientSystem(arr))
    
driver()


