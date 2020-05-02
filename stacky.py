#full
#empty
#push
#pop
arr=[-5]*50
top=-1
k="yes"
def stack_full():
    global top
    if (top==50):
        return "full"
    else:
        return "nf"
def stack_empty():
    global top
    if (top==-1):
        return "stack empty"
    else:
        return "ne"


def push_st(val):
    global top
    if(stack_full()=="full"):
        return "sorry stack full"
    elif(stack_full()=="nf"):
        top=top+1
        arr[top]=val

def pop_st():
    global top
    if(stack_empty()=="stack empty"):
        return "empty stack"
    elif(stack_empty()=="ne"):
         arr[top]=-5
         top=top-1
def display():
    print (arr)
        
while(k=="yes"):
    print("enter 1 pop\n 2 for push\n 3 for display")
    n=input("enter your choice")
    if(n==1):
        pop_st()
    elif(n==2):
        val=input("enter the value to be inserted")
        push_st(val)
    elif(n==3):
        display()
    k=raw_input("do you wana continue yes/no")
    print(k)



    




          

    

    
