#arr[]
#ite(not needed)
#pop_front
#push_back
#flag_-1 is empty
k="yes"
arr=[-1]*50#array
front=0
back=0
def empty():
    global back,front#global so that it does not use local variable
    if ((arr[0]==-1) and (front==back)):
        return 'e'
    else :
        return 'ne'    
     
def full():
    global back,front
    if (back == 50):
        return 'f'
    else :
        return 'nf'
        
def pop_front():
    global back,front
    if(empty()=='e'):
        print("queue empty")
    elif(empty()=='ne'):
        arr[front]=-1
        front=front+1

def push_back(val):
    global back,front
    if (full()=='f'):
        print("queue full")
    elif(full()=='nf'):
        if back==0:
            arr[ back]=val
            back=back+1
        else:
            arr[back]=val
            back=back+1
def display():
     print (arr)


while(k=="yes"):
    print("1 for pop \n 2 for push \n 3 for print")
    ans=input("enter your choice")
    if (ans==1):
        pop_front()
    elif (ans==2):
        val=input("enter a value to push")
        push_back(val)
    elif (ans==3):
        display()
    k=raw_input("do you wana conitnue yes/no")#raw_input to enter string as input
    print(k)







    

    
