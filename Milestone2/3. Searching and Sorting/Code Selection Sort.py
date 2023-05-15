from sys import stdin

def selectionSort(arr,n):
    for i in range(n):
        
        mini = arr[i]
        miniIndex=i

        for j in range(i,n):
            if mini > arr[j]:
                mini=arr[j]
                miniIndex=j


        tmp=arr[i]
        arr[i]= arr[miniIndex]
        arr[miniIndex]= tmp;
