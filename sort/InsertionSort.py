
def insertSort(array):
    n= len(array)

    for i in range(n):
        key = array[i]
        #insert index of array[i] into the sorted subarray A[1:i-1], swaping places 
        j=i-1
        print(j,key)
        while j>0 & array[j]>key:
            array[j+1]=array[j]
            j=j-1
            array[j+1]=key
        print("step",i,":",array)   

myarr=[4,3,5,1,2]
insertSort(myarr)
print("sorted :",myarr)


#you are a failure