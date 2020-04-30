import pandas as pd
import math
df=pd.read_csv("input.csv")#csv file in dataframe not in array
#print(df)
arr=df['number'].values
n=len(arr)
#print(type(arr))
#print(arr[0])
#print(arr)
#sort the array-1
#T from user
#n is len of arr


def sort():
    global arr,n
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] 
    print(arr)

def b_search(T):
    #print("here")
    l=0
    r=n-1
    while(l<=r):
        m=int(math.floor((l+r)/2))
        if(arr[m]<T):
            l=m+1
        elif(arr[m]>T):
            r=m-1
        else:
            return m #return index of the element in the arr
    return "unsuccesful"
print(arr)
T=input("enter the value to be searched")
sort()
loc=b_search(T)
print(loc)
if (loc=="unsuccesful"):
    print("are you kidding me")
else:
    print(arr[:loc+1],"*",arr[loc+1:])


    







