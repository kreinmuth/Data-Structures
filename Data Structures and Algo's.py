
        
from tempfile import tempdir


board = [['x','o','x'],
         ['o','o','x'],
         ['o','o','o']]

board_length=len(board)
board_height=len(board)

string_column=""
x="xxx"
o='ooo'
count=0

for w in range(board_length): #w=['x','o','x']
    for v in range(board_height):#v='x'
        for loop in board:
            string_column+=loop[w][v]
            count+=1
            if o in string_column:
                print("o_won")
                break
            if x in string_column:
                print("x_won")
                break
            if count ==3:
                count=0
                string_column=""



#LINKED LISTS and REVERSE LINKED LISTS

class Node: #This class is used for creating all the stuff in each Node
    def __init__(self,value):
        self.head=value     #This makes the head equal to the vale
        self.next=None      #This is the end of LINKED LIST if there is another Node it will point to it

class LinkedList:
    def __init__(self,value):
        new_node=Node(value) #This creates the Node
        self.head=new_node   #This makes the head equal to the new Node
        self.tail=new_node   #This makes the tail equal to the new Node
        self.length+=1

    def append(self,value):#This function is adding a new node(dict value) to the end of the list
        new_node=Node(value)
        if self.length==0:#THIS checks if the list and empty and if it is makes the head and tail equal to the new node
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node #This sets the previous tail to point towards the new node
            self.tail=new_node #This updates the tail to the new node.
        self.length+=1

    def pop(self,value):#This function is used to pop the last element of a list
        if self.length==0:
            return None
        temp=self.head #creating two variable so one can be returned to get the value and another used to remove the node
        pre=self.head

        while (temp.next):#this walks through the list until there is no next
            pre=temp
            temp=temp.next

        self.tail=pre #This acts as the last node since the temp.next is none and broke the While loop
        self.tail.next=None
        self.length-=1

        if self.length==0:#This is checking if the node that was popped was the last node
            self.head=None
            self.tail=None
        return temp.value

    def prepend(self,value): #This function is used to add a node to the begining of a linked list
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head #This is setting the new first to point at the prior head
            self.head=new_node #This is updating the list head
        self.length+=1
        return True

    def pop_first(self,value):#This function is used to pop the first element of a list
        if self.length == 0: #This checks if the list is already 0
            return None

        temp = self.head #This sets the temp to the head
        self.head=self.head.next #This moves the head to the next list item so we can pop the old head
        temp.next=None #This pops the old head
        self.length-= 1 #This removes it from the list
        
        if self.length==0: #This checks if after popping the item the list becomes empty
            self.tail=None
        return temp.value

    #If you want to pop an item from the middle of the list implement a counter with a while loop that returns the current count and function to then use

    def get (self,index): #This returns the value of a linked list from a given index like a regular list
        if index <0 or index >= self.length:#This checks the index value is in the list
            return None
        
        temp=self.head #Set the temporary object equal to the current head
        
        for _ in range(index): #This goes to the index value provided so if 2 it will go from 0 to 2
            temp=temp.next #This moves the temp value to the next node each time the for loop iterates through
        
        return temp.value #This returns the temp value
    
    def change_value(self, index, value): #This is changing the value of a node in a list
        
        temp = self.get(index) #This locates the head with the get function and the index provided by the user and creates an object
        
        if temp:
            temp.value=value #This sets the value to the new provided value
            return True
        
        return False #This is if the index provided is not in the list

    def insert(self,index,value):
        if index <0 or index> self.length: #This checks whether the index provided is in the list
            return False

        if index == 0: #This is if the index wants to be inserted at the begining of the list
            return self.prepend(value)

        if index == self.length: #This is if the index wants to be inserted at the end of the list
            return self.append(value)

        #BELOW IS INSERTING AT A SPECIFIC POINT MIDDLE OF THE LIST
        new_node=Node(value)#This is creating a new node with the value provided
        temp = self.get(index-1)#This creates an object located at the spot before the index so it can connect to the next of the prior node

        new_node.next = temp.next #This sets the pointer of the new node to the Node at the index the new node will occupy
        temp.next = new_node #This moves the the pointer from the node before the index # to the new node
        self.length += 1
        
        return True

    def remove(self,index):
        if index <0 or index >=self.length: #This checks if the index is in the range
            return None
        
        if index == 0:#This removes the Node if it is the begining item
            return self.pop_first()
        
        if index == self.length-1:#This removes the Node if it is the last Node in the List
            return self.pop()
        
        pre = self.get(index -1) #This is getting the Node before the one that will be removed
        temp = pre.next #This is the Node that will get removed
        pre.next=temp.next# This moves the pointer of the Node that is before the temp equal to the same Node as the index being removed
        temp.next=None #This removes the Node
        self.length-=1 #This updates the length
        
        return temp.value

    def reverse(self):#This function reverses the linked list
        temp = self.head
        self.head=self.tail#This moves the current head to the tail
        self.tail=temp #This moves the current tail to the former head position by utilizing the temp object
        
        after = temp.next #This is
        before = None #this is the last spot in the list

        for _ in range(self.length):#This function is reversing all of the pointers in the list
            after = temp.next
            temp.next=before #This flips the pointer from left to right to right to left
            before=temp #This updates before to the prior head
            temp=after #This moves the temp to the after Node. The after gets moved the next time the for loop runs.

class NodeDoubly:
    def __init__(self,value): #This node will point both forward to the next node to the right and to the left
        self.value=value
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self, value):
        new_node=NodeDoubly(value)
        self.head=new_node
        self.tail=new_node
        self.length = 1

    def append (self,value): #Adding a new node to the end of the Node
        new_node=NodeDoubly(value)
        if self.length==0:#THIS checks if the list and empty and if it is makes the head and tail equal to the new node
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node #This sets the previous tail to point towards the new node
            new_node.prev=self.tail #Since this is a new node at the end of the list need to connect it to previous node since DOUBLY
            self.tail=new_node #This updates the tail to the new node.
        self.length+=1

    def pop(self,value):#This function is used to pop the last element of a list
        if self.length==0:
            return None
        temp=self.tail #creating a variable so one can be returned to get the value and another used to remove the node
        if self.length==1:#checks if there is only one item in the list
            self.head=None
            self.tail=None
        
        #LESS STEPS THAN LINKED LIST SINCE WE CAN GO RIGHT TO LEFT AND NOT BE STUCK GOING RIGHT TO LEFT

        else: 
            self.tail=self.tail.prev #This moves the tail to the previous Node
            self.tail.next=None #This disconnects the next pointer to the prior tail Node
            temp.prev=None #This disconnects the previous pointer from the prioer tail Node
        self.length-=1
        return temp.value

    def prepend(self,value): #This function is used to add a node to the begining of a linked list
        new_node=NodeDoubly(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        
        else:
            new_node.next=self.head #This is setting the new first to point at the prior head
            self.head.prev=new_node #This tells the prior head to now point to the new head
            self.head=new_node #This is updating the list head
        
        self.length+=1
        return True

    def pop_first(self,value):#This function is used to pop the first element of a list
        if self.length == 0: #This checks if the list is already 0
            return None

        temp = self.head #This sets the temp to the head
        
        if self.length ==1:#If there is only one item it pops it
            self.head=None
            self.tail=None
        
        else:
            self.head=self.head.next #This moves the head to the next Node
            self.head.prev=None #This disconnects the new head from the head being popped
            temp.next=None #This disconnets the old head from the new head
        
        self.length-=1
        return temp.value
