## Class to define a Node
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

## Class to define a linkedlist
class LinkedList:

    def __init__(self):
        self.head=None ## Set the head of the empty list to none.

    ## Insert a new node into the list
    def insert(self,new_data):
        new_node=Node(new_data)  ## Create a Node object using the new data
        new_node.next=self.head  ## link the new node to the head of the list
        self.head=new_node ## set the new head.

    ## Print the list
    def printList(self):
        temp=self.head  ## Start from the head of the node and iterate until next node is None
        lstString=''
        while temp:
            #print ("Data =", temp.val)
            lstString+=str(temp.val)
            temp=temp.next
        print(lstString)

    ## delete the node using the position of the node
    def deleteNode(self,posi):
        if self.head==None: ## if the list is empty then return
            return
        ## Stroing the head of the node
        temp=self.head

        ## If Removing Head
        if posi==0:
            self.head=temp.next
            temp=None
            return

        ##  Find the previous node of the node to be deleted
        for i in range(posi-1):
            temp=temp.next
            if temp is None:
                break

        ## if Position is more than number of records
        if temp is None:
            return
        if temp.next is None:
            return

        ## unlink the node from the linked list
        next=temp.next.next
        temp.next=None
        temp.next=next

    def find_and_delete(self,findVal):
        temp=self.head
        j=0
        while temp :
            if temp.val==findVal:
               break
            j+=1
            temp=temp.next
        self.deleteNode(j)


print("Create the linked List..")
lnkdlist = LinkedList() ## Create a Linked List Object
print("Insert data into Linked List")
for i in range(9):  ## insert 10 numbers into the list list
    lnkdlist.insert(i)
lnkdlist.printList() ## Print the linked list



print("After Deleting Node by position......")
lnkdlist.deleteNode(4)  ## Delete the node in position
lnkdlist.printList() ## Print the linked list


print("Afer Deleting by Value.......")
lnkdlist.find_and_delete(5)  ## Delete the node in position
lnkdlist.printList() ## Print the linked list

