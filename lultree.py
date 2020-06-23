#input tree T from user in llist
#N<L<R
def root_node:
     left=null
     right=null
    if (root_node==null):
        root_node=input("enter the root node")
        return root_node
    elif(root_node!=null):
        n1=input("enter the first data")
        if(n1<root_node):
            if(left==null):
                left=n1   
        n2=input("enter the second data")
        if(n2<n1):
            left=n2
            right=n1
            #if n2 is gretaer than node error message


        

        
        
        


